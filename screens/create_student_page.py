from PyQt5.QtCore import QDate
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QAction, QMainWindow, QFileDialog, QInputDialog, QLineEdit
import sys
from datetime import datetime
from screens.add_student_python import Ui_MainWindow
from connectionDB import DbManager
from control_page import *
from helper_function import *


class StudentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Öğrenci Bilgileri Ekle")
        self.connection = DbManager()
        get_out = QAction("Quit", self)
        get_out.triggered.connect(self.closeEvent)
        self.file_address = ""
        self.student_loader()
        self.department_loader()
        self.branch_loader()
        self.class_loader()
        self.workplace_loader()
        self.date_loader()
        self.ui.cmb_department.currentTextChanged.connect(self.branch_loader)
        self.ui.cmb_department.currentTextChanged.connect(self.class_loader)
        self.ui.cmb_branch.currentTextChanged.connect(self.workplace_loader)
        self.ui.lw_students.currentRowChanged.connect(lambda: self.obj_control(self.data_loader, self.ui.lw_students))
        self.ui.btn_save.clicked.connect(lambda: self.generate_value(self.recorder))
        self.ui.btn_edit.clicked.connect(lambda: self.obj_control(self.updater, self.ui.lw_students))
        self.ui.btn_change_id.clicked.connect(lambda: self.obj_control(self.change_id_number, self.ui.lw_students))
        self.ui.btn_clear_all.clicked.connect(self.clean_data)
        self.ui.btn_take_photo.clicked.connect(self.get_photo_address)
        self.ui.le_id_number.textChanged.connect(self.clean_data)

    def obj_control(self, func, obj):
        if func.__name__ != "data_loader" and obj.currentItem() is None:
            message_box("Önce seçim yapmalısınız!")
        elif func.__name__ == "data_loader" and obj.currentItem() is not None:
            id_number = find_id_number(obj.currentItem().text())
            func(id_number)
        elif func.__name__ == "change_id_number" and obj.currentItem() is not None:
            id_number = find_id_number(obj.currentItem().text())
            func(id_number)
        elif func.__name__ == "updater" and obj.currentItem() is not None:
            self.generate_value(func)
        focus_item(self.ui.le_id_number)

    def generate_value(self, func):
        class_idm = "NULL"
        if self.ui.cmb_class.currentText() != "":
            class_idm = self.connection.find(f""" SELECT id FROM classes WHERE name = "{self.ui.cmb_class.currentText()}" """)
        genderm = "E"
        if self.ui.rb_female.isChecked():
            genderm = "K"
        li_kw = {"id_number": self.ui.le_id_number.text(), "name": tr_capitalize(stripper(self.ui.le_name.text())), "surname": tr_capitalize(stripper(self.ui.le_surname.text())),
                 "number": self.ui.le_number.text(), "branch_id": self.connection.find(f""" SELECT id FROM branches WHERE name = "{self.ui.cmb_branch.currentText()}" """),
                 "class_id": class_idm, "record_date": datetime.date(datetime(*QDate.getDate(self.ui.date_record.date()))), "father": tr_capitalize(stripper(self.ui.le_father_name.text())),
                 "mother": tr_capitalize(stripper(self.ui.le_mother_name.text())), "birth_date": datetime.date(datetime(*QDate.getDate(self.ui.date_of_birth.date()))),
                 "birth_place": self.ui.le_birth_place.text(), "workplace_name": self.ui.cmb_workplace.currentText(),
                 "starting_date": datetime.date(datetime(*QDate.getDate(self.ui.date_starting_work.date()))), "self_phone": self.ui.le_self_phone.text(),
                 "father_phone": self.ui.le_father_phone.text(), "mother_phone": self.ui.le_mother_phone.text(), "email": self.ui.le_email.text(), "photo_address": self.file_address,
                 "gender": genderm}
        func(**li_kw)

    def recorder(self, **kwargs):
        id_numbers = find_id_numbers(self.ui.lw_students)
        passive_id_numbers = [i[0] for i in self.connection.selector(f"""SELECT id_number FROM students WHERE is_active = "H" """)]
        control_list = [identity_number_control(kwargs["id_number"], id_numbers), name_control(kwargs["name"]), surname_control(kwargs["surname"]), number_control(kwargs["number"]),
                        archive_identity_number_control(kwargs["id_number"], passive_id_numbers)]
        if False not in control_list:
            self.connection.recorder(f""" INSERT INTO students VALUES ("{kwargs["id_number"]}", "{kwargs["name"]}", "{kwargs["surname"]}", "{kwargs["number"]}", {kwargs["branch_id"]},
                                {kwargs["class_id"]}, "{kwargs["record_date"]}", "{kwargs["father"]}", "{kwargs["mother"]}", "{kwargs["birth_date"]}", "{kwargs["birth_place"]}", "E",
                                "{kwargs["self_phone"]}", "{kwargs["father_phone"]}", "{kwargs["mother_phone"]}", "{kwargs["email"]}", "{kwargs["photo_address"]}", "E","{kwargs["gender"]}") """)
            if kwargs["workplace_name"] != "Okul":
                wp_id = self.connection.find(f""" SELECT id FROM workplaces WHERE name = "{self.ui.cmb_workplace.currentText()}" """)
                self.connection.recorder(f""" INSERT INTO history (studentID, workplaceID, starting_date) VALUES ("{kwargs["id_number"]}", {wp_id}, "{kwargs["starting_date"]}") """)

                number_of_student_in_new_wp = self.connection.selector(f""" SELECT COUNT(studentID) FROM history  WHERE workplaceID = {wp_id} AND leaving_date IS NULL """)[0][0]
                if number_of_student_in_new_wp > 1:
                    self.settle_workplace(kwargs["workplace_name"], kwargs["id_number"])
                else:
                    message_box("işletmedeki ilk öğrenci")
            else:
                self.connection.updater(f"""UPDATE students SET is_going="H" WHERE id_number="{kwargs["id_number"]}" """)
                self.connection.recorder(f""" INSERT INTO temp_workplace(studentID, staffID, starting_date) VALUES ("{kwargs["id_number"]}", NULL, "{kwargs["starting_date"]}") """)
            self.student_loader()
            self.clean_data()
            focus_item(self.ui.le_id_number)
        else:
            pass

    def updater(self, **kwargs):
        id_number = find_id_number(self.ui.lw_students.currentItem().text())
        control_list = [name_control(kwargs["name"]), surname_control(kwargs["surname"]), number_control(kwargs["number"])]
        if False not in control_list:
            self.connection.updater(f"""UPDATE students SET name="{kwargs["name"]}", surname="{kwargs["surname"]}", school_number="{kwargs["number"]}", branchID={kwargs["branch_id"]},
                                    record_date="{kwargs["record_date"]}", father_name="{kwargs["father"]}", mother_name="{kwargs["mother"]}", birthdate="{kwargs["birth_date"]}",
                                    birth_place="{kwargs["birth_place"]}", self_phone="{kwargs["self_phone"]}", parent_phone1="{kwargs["father_phone"]}", parent_phone2="{kwargs["mother_phone"]}",
                                    email="{kwargs["email"]}", photo_address="{kwargs["photo_address"]}", gender="{kwargs["gender"]}" WHERE id_number="{id_number}" """)

        is_going = self.connection.find(f"""SELECT is_going FROM students WHERE id_number = "{id_number}" """)
        old_wp_id = None
        old_wp_name = "Okul"
        if is_going == "E":
            old_wp_id = self.connection.find(f"""SELECT workplaceID FROM history WHERE studentID = "{id_number}" AND leaving_date IS NULL""")
            old_wp_name = self.connection.find(f"""SELECT name FROM workplaces WHERE id = {old_wp_id}""")
        new_wp_name = kwargs["workplace_name"]
        new_class_id = kwargs["class_id"]
        old_class_id = self.connection.find(f"""SELECT classID FROM students WHERE id_number = "{id_number}" """)

        if new_class_id != "NULL" and old_class_id != new_class_id and is_going == "E":
            self.connection.updater(f"""UPDATE students SET classID={new_class_id}  WHERE id_number="{id_number}" """)
            self.settle_workplace(old_wp_name, id_number)
        elif new_class_id != "NULL" and old_class_id != new_class_id and is_going == "H":
            self.connection.updater(f"""UPDATE students SET classID={new_class_id}  WHERE id_number="{id_number}" """)
        elif new_class_id == "NULL" and old_class_id is not None:
            self.connection.updater(f"""UPDATE students SET classID=NULL WHERE id_number="{id_number}" """)
        else:
            pass

        if is_going == "H" and new_wp_name != "Okul":
            new_wp_id = self.connection.find(f""" SELECT id FROM workplaces WHERE name = "{new_wp_name}" """)
            self.connection.deleter(f"""DELETE FROM temp_workplace WHERE studentID="{id_number}" """)
            self.connection.recorder(f"""INSERT INTO history (studentID, workplaceID, starting_date) VALUES("{id_number}", {new_wp_id}, "{kwargs["starting_date"]}")""")
            self.connection.updater(f"""UPDATE students SET is_going="E" WHERE id_number="{id_number}" """)
            number_of_student_in_new_wp = self.connection.selector(f""" SELECT COUNT(studentID) FROM history  WHERE workplaceID = {new_wp_id} AND leaving_date IS NULL """)[0][0]
            if number_of_student_in_new_wp > 1:
                self.settle_workplace(kwargs["workplace_name"], id_number)
        elif is_going == "E" and new_wp_name == "Okul":
            old_wp_id = self.connection.find(f"""SELECT workplaceID FROM history WHERE studentID = "{id_number}" AND leaving_date IS NULL""")
            old_wp_name, old_staff_id, old_day_id = self.connection.selector(f"""SELECT name, staffID, dayID FROM workplaces WHERE id = {old_wp_id}""")[0]
            if old_staff_id is not None and old_day_id is not None:
                self.connection.recorder(f"""INSERT INTO temp_workplace(studentID, staffID, starting_date) VALUES("{id_number}", "{old_staff_id}", "{kwargs["starting_date"]}")""")
            else:
                self.connection.recorder(f"""INSERT INTO temp_workplace(studentID, staffID, starting_date) VALUES("{id_number}", NULL, "{kwargs["starting_date"]}")""")
            self.connection.updater(f"""UPDATE students SET is_going="H" WHERE id_number="{id_number}" """)
            self.connection.updater(f"""UPDATE history SET leaving_date="{kwargs["starting_date"]}" WHERE studentID="{id_number}" AND workplaceID={old_wp_id} AND leaving_date IS NULL """)
            number_of_student_in_old_wp = self.connection.selector(f""" SELECT COUNT(studentID) FROM history WHERE workplaceID = {old_wp_id} AND leaving_date IS NULL """)[0][0]
            if number_of_student_in_old_wp == 0:
                self.connection.updater(f"""UPDATE workplaces SET staffID = NULL, dayID = NULL WHERE name="{old_wp_id}" """)
        elif is_going == "E" and new_wp_name != "Okul" and old_wp_name != new_wp_name:
            old_wp_id = self.connection.find(f"""SELECT workplaceID FROM history WHERE studentID = "{id_number}" AND leaving_date IS NULL""")
            new_wp_id = self.connection.find(f""" SELECT id FROM workplaces WHERE name = "{new_wp_name}" """)
            self.connection.updater(f"""UPDATE history SET leaving_date="{kwargs["starting_date"]}" WHERE studentID="{id_number}" AND workplaceID={old_wp_id} AND leaving_date IS NULL """)
            self.connection.recorder(f"""INSERT INTO history (studentID, workplaceID, starting_date) VALUES("{id_number}", {new_wp_id}, "{kwargs["starting_date"]}")""")
            number_of_student_in_old_wp = self.connection.selector(f""" SELECT COUNT(studentID) FROM history  WHERE workplaceID = {old_wp_id} AND leaving_date IS NULL """)[0][0]
            number_of_student_in_new_wp = self.connection.selector(f""" SELECT COUNT(studentID) FROM history  WHERE workplaceID = {new_wp_id} AND leaving_date IS NULL """)[0][0]
            if number_of_student_in_old_wp == 0:
                self.connection.updater(f"""UPDATE workplaces SET staffID = NULL, dayID = NULL WHERE name="{old_wp_id}" """)
            if number_of_student_in_new_wp > 1:
                self.settle_workplace(new_wp_id, id_number)

    def change_id_number(self, id_number):
        id_numbers = find_id_numbers(self.ui.lw_students)
        new_id_number, ok_pressed = QInputDialog.getText(self, "Cevap ver", "Yeni Değer:", QLineEdit.Normal, id_number)
        if ok_pressed:
            control_list = [identity_number_control(new_id_number, id_numbers)]
            if False not in control_list:
                self.connection.updater(f"""UPDATE students SET id_number={new_id_number}  WHERE id_number="{id_number}" """)
        self.student_loader()
        self.clean_data()

    def settle_workplace(self, p_wp_name, p_id_number):
        wp_id = self.connection.find(f""" SELECT id FROM workplaces WHERE name = "{p_wp_name}" """)
        wp_day_id = self.connection.find(f""" SELECT dayID FROM workplaces WHERE id = {wp_id} """)
        wp_staff_id = self.connection.find(f""" SELECT staffID FROM workplaces WHERE id = {wp_id} """)
        class_id = self.connection.find(f"""SELECT classID FROM students WHERE id_number = "{p_id_number}" """)
        if class_id is not None:
            class_days_id_list = [day[0] for day in self.connection.selector(f""" SELECT dayID FROM classes_days WHERE classID={class_id}""")]
        else:
            class_days_id_list = [day[0] for day in self.connection.selector(f""" SELECT dayID FROM classes_days""")]
        if wp_day_id is not None and wp_staff_id is not None:
            if wp_day_id not in class_days_id_list:
                wp_name = self.connection.find(f""" SELECT name FROM workplaces WHERE id = {wp_id} """)
                day_name = self.connection.find(f""" SELECT name FROM days WHERE id = {wp_day_id} """)
                staff_name = " ".join(self.connection.selector(f""" SELECT name, surname FROM staffs WHERE id_number = "{wp_staff_id}" """)[0])
                self.connection.updater(f""" UPDATE workplaces  SET staffID = NULL, dayID=NULL WHERE id = {wp_id} """)
                message_box(f"""{staff_name}'in {day_name} günü {wp_name} işletmesindeki görevi sıfırlanmıştır.""")

    def get_photo_address(self):
        self.file_address = QFileDialog.getOpenFileName(self, "Foto ekle")[0]
        self.ui.lbl_photo.setPixmap(QPixmap(self.file_address))

    def data_loader(self, id_number):
        info_list = list(self.connection.selector(f"""SELECT * FROM students WHERE id_number = "{id_number}" """)[0])
        obj_list = [None, self.ui.le_name, self.ui.le_surname, self.ui.le_number, self.ui.cmb_branch, self.ui.cmb_class, self.ui.date_record, self.ui.le_father_name, self.ui.le_mother_name,
                    self.ui.date_of_birth, self.ui.le_birth_place, None, self.ui.le_self_phone, self.ui.le_father_phone, self.ui.le_mother_phone, self.ui.le_email, self.ui.lbl_photo, None,
                    self.ui.rb_male]
        for number, obj in enumerate(obj_list):
            if obj is None:
                continue
            elif obj.objectName().startswith("le"):
                obj.setText(info_list[number])
            elif obj.objectName().startswith("cmb_class"):
                obj_name = ""
                if info_list[number] is not None:
                    obj_name = self.connection.find(f"""SELECT name FROM classes WHERE id = {info_list[number]} """)
                obj.setCurrentText(obj_name)
            elif obj.objectName().startswith("cmb_branch"):
                obj_name = self.connection.find(f"""SELECT name FROM branches WHERE id = {info_list[number]} """)
                department_id = self.connection.find(f"""SELECT departmentID FROM branches WHERE id = {info_list[number]} """)
                department_name = self.connection.find(f"""SELECT name FROM departments WHERE id = {department_id} """)
                self.ui.cmb_department.setCurrentText(department_name)
                obj.setCurrentText(obj_name)
            elif obj.objectName().startswith("date"):
                obj.setDate(info_list[number])
            elif obj.objectName().startswith("lbl"):
                obj.setPixmap(QPixmap(info_list[number]))
                self.file_address = info_list[number]
            elif obj.objectName().startswith("rb"):
                if info_list[number] == "E":
                    self.ui.rb_male.setChecked(True)
                else:
                    self.ui.rb_female.setChecked(True)
            else:
                pass
        is_going, is_active = self.connection.selector(f""" SELECT is_going, is_active FROM students WHERE id_number = "{id_number}" """)[0]
        if is_going == "E":
            wp_id = self.connection.find(f"""SELECT workplaceID FROM history WHERE studentID = "{id_number}" AND leaving_date IS NULL """)
            wp_name = self.connection.find(f"""SELECT name FROM workplaces WHERE id = {wp_id} """)
            starting_date = self.connection.find(f"""SELECT starting_date FROM history WHERE studentID = "{id_number}" AND leaving_date IS NULL """)
            coordinator_id = self.connection.find(f"""SELECT staffID FROM workplaces JOIN history ON history.workplaceID = workplaces.id JOIN students ON history.studentID = students.id_number
                                                WHERE history.workplaceID = {wp_id} AND history.studentID = "{id_number}" AND history.leaving_date IS NULL """)
        else:
            wp_name = "Okul"
            coordinator_id, starting_date = self.connection.selector(f"""SELECT staffID, starting_date FROM temp_workplace WHERE studentID = "{id_number}" """)[0]
        coordinator_name = ""
        if coordinator_id is not None:
            coordinator_name = " ".join(self.connection.selector(f"""SELECT name, surname FROM staffs WHERE id_number = "{coordinator_id}" """)[0])
        self.ui.le_coordinator.setText(coordinator_name)
        self.ui.cmb_workplace.setCurrentText(wp_name)
        self.ui.date_starting_work.setDate(starting_date)

    def date_loader(self):
        self.ui.date_record.setDate(datetime.date(datetime.now()))
        self.ui.date_starting_work.setDate(datetime.date(datetime.now()))
        self.ui.date_of_birth.setDate(datetime(datetime.now().year - 13, 1, 1))

    def student_loader(self):
        self.ui.lw_students.clear()
        data = self.connection.selector(f"""SELECT name, surname, id_number FROM students WHERE is_active="E" """)
        self.ui.lw_students.addItems(get_list_personal(data))

    def department_loader(self):
        self.ui.cmb_department.clear()
        data = self.connection.selector(f"""SELECT name FROM departments""")
        self.ui.cmb_department.addItems(get_list_general(data))

    def branch_loader(self):
        department_id = self.connection.find(f"""SELECT id FROM departments WHERE name = "{self.ui.cmb_department.currentText()}" """)
        self.ui.cmb_branch.clear()
        data = self.connection.selector(f"SELECT name FROM branches WHERE departmentID={department_id}")
        self.ui.cmb_branch.addItems(get_list_general(data))

    def class_loader(self):
        department_id = self.connection.find(f"""SELECT id FROM departments WHERE name = "{self.ui.cmb_department.currentText()}" """)
        self.ui.cmb_class.clear()
        data = self.connection.selector(f"""SELECT name FROM classes WHERE departmentID={department_id}""")
        self.ui.cmb_class.addItem("")
        self.ui.cmb_class.addItems(get_list_general(data))

    def workplace_loader(self):
        self.ui.cmb_workplace.clear()
        data = self.connection.selector(
            f"""SELECT workplaces.name FROM workplaces JOIN branches ON branches.departmentID = workplaces.departmentID WHERE branches.name = "{self.ui.cmb_branch.currentText()}" """)
        self.ui.cmb_workplace.addItem("Okul")
        self.ui.cmb_workplace.addItems(get_list_general(data))

    def clean_data(self):
        obj_list = [self.ui.lw_students, self.ui.le_name, self.ui.le_surname, self.ui.le_number, self.ui.cmb_department, self.ui.le_father_name, self.ui.le_mother_name, self.ui.le_birth_place,
                    self.ui.cmb_workplace, self.ui.le_coordinator, self.ui.le_self_phone, self.ui.le_father_phone, self.ui.le_mother_phone, self.ui.le_email, self.ui.lbl_photo, self.ui.rb_male]
        for number, obj in enumerate(obj_list):
            if obj.objectName().startswith("le") or obj.objectName().startswith("lbl"):
                obj.clear()
            elif obj.objectName().startswith("cmb"):
                obj.setCurrentIndex(0)
            elif obj.objectName().startswith("lw"):
                obj.setCurrentItem(None)
            elif obj.objectName().startswith("rb"):
                obj.setChecked(True)
        self.file_address = ""
        self.class_loader()
        self.date_loader()

    def closeEvent(self, event):
        self.connection.db_closer()


if __name__ == "__main__":
    app = QApplication([])
    window = StudentWindow()
    window.show()
    sys.exit(app.exec())
