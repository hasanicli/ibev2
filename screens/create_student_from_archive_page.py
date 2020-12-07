from PyQt5.QtCore import QDate
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QAction, QMainWindow
import sys
from datetime import datetime
from screens.add_student_from_arhcive_python import Ui_MainWindow
from connectionDB import DbManager
from control_page import *
from helper_function import *
from screens.create_student_page import StudentWindow


class StudentFromArchiveWindow(QMainWindow):
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
        self.ui.btn_delete.clicked.connect(lambda: message_box("şimdilik silemezsiniz\nsilersek işletme kayıtları da silinir"))
        self.ui.btn_edit.clicked.connect(lambda: self.obj_control(self.updater, self.ui.lw_students))
        self.ui.btn_clear_all.clicked.connect(lambda: self.ui.lw_students.setCurrentItem(None))

    def obj_control(self, func, obj):
        if func.__name__ != "data_loader" and obj.currentItem() is None:
            message_box("Önce seçim yapmalısınız!")
        elif func.__name__ == "data_loader" and obj.currentItem() is not None:
            id_number = find_id_number(obj.currentItem().text())
            func(id_number)
        elif func.__name__ == "data_loader" and obj.currentItem() is None:
            self.clean_data()
        elif func.__name__ == "updater" and obj.currentItem() is not None:
            self.generate_value(func)

    def generate_value(self, func):
        class_id_temp = "NULL"
        if self.ui.cmb_class.currentText() != "":
            class_id_temp = self.connection.find(f""" SELECT id FROM classes WHERE name = "{self.ui.cmb_class.currentText()}" """)
        li_kw = {"id_number": self.ui.le_id_number.text(), "branch_id": self.connection.find(f""" SELECT id FROM branches WHERE name = "{self.ui.cmb_branch.currentText()}" """),
                 "class_id": class_id_temp, "record_date": datetime.date(datetime(*QDate.getDate(self.ui.date_record.date()))), "wp_name": self.ui.cmb_workplace.currentText(),
                 "starting_date": datetime.date(datetime(*QDate.getDate(self.ui.date_starting_work.date())))}
        func(**li_kw)

    def updater(self, **kwargs):
        self.connection.recorder(f"""UPDATE students SET branchID={kwargs["branch_id"]}, classID={kwargs["class_id"]}, record_date="{kwargs["record_date"]}", is_going="E", is_active="E"
                                    WHERE id_number="{kwargs["id_number"]}" """)
        if kwargs["wp_name"] != "Okul":
            wp_id = self.connection.find(f""" SELECT id FROM workplaces WHERE name = "{kwargs["wp_name"]}" """)
            self.connection.recorder(f"""INSERT INTO history(studentID, workplaceID, starting_date) VALUES ("{kwargs["id_number"]}", {wp_id}, "{kwargs["starting_date"]}") """)
            number_of_student_in_new_wp = self.connection.selector(f""" SELECT COUNT(studentID) FROM history  WHERE workplaceID = {wp_id} AND leaving_date IS NULL """)[0][0]
            if number_of_student_in_new_wp > 1:
                StudentWindow().settle_workplace(kwargs["wp_name"], kwargs["id_number"])
            else:
                message_box("işletmedeki ilk öğrenci")
        else:
            self.connection.updater(f"""UPDATE students SET is_going="H" WHERE id_number="{kwargs["id_number"]}" """)
            self.connection.recorder(f""" INSERT INTO temp_workplace(studentID, staffID, starting_date) VALUES ("{kwargs["id_number"]}", NULL, "{kwargs["starting_date"]}") """)
        self.student_loader()

    def data_loader(self, id_number):
        info = list(self.connection.selector(f"""SELECT * FROM students WHERE id_number = "{id_number}" """)[0])
        name = info[1]
        surname = info[2]
        school_number = info[3]
        father_name = info[7]
        mother_name = info[8]
        birthdate = info[9]
        birth_place = info[10]
        self_phone = info[12]
        parent_phone1 = info[13]
        parent_phone2 = info[14]
        email = info[15]
        self.file_address = info[16]
        gender = info[18]

        self.ui.le_id_number.setText(info[0])
        self.ui.le_name.setText(name)
        self.ui.le_surname.setText(surname)
        self.ui.le_number.setText(school_number)
        self.ui.le_father_name.setText(father_name)
        self.ui.le_mother_name.setText(mother_name)
        self.ui.date_of_birth.setDate(birthdate)
        self.ui.le_birth_place.setText(birth_place)
        self.ui.le_self_phone.setText(self_phone)
        self.ui.le_father_phone.setText(parent_phone1)
        self.ui.le_mother_phone.setText(parent_phone2)
        self.ui.le_email.setText(email)
        self.ui.lbl_photo.setPixmap(QPixmap(self.file_address))
        self.ui.rb_male.setChecked(True)
        if gender == "K":
            self.ui.rb_female.setChecked(True)

    def date_loader(self):
        self.ui.date_record.setDate(datetime.date(datetime.now()))
        self.ui.date_starting_work.setDate(datetime.date(datetime.now()))
        self.ui.date_of_birth.setDate(datetime(datetime.now().year - 13, 1, 1))

    def student_loader(self):
        self.ui.lw_students.clear()
        data = self.connection.selector(f"""SELECT name, surname, id_number FROM students WHERE is_active="H" """)
        self.ui.lw_students.addItems(get_list_personal(data))

    def department_loader(self):
        self.ui.cmb_department.clear()
        data = self.connection.selector(f"""SELECT name FROM departments""")
        self.ui.cmb_department.addItems(get_list_general(data))

    def branch_loader(self):
        department_name = self.ui.cmb_department.currentText()
        department_id = self.connection.find(f"""SELECT id FROM departments WHERE name = "{department_name}" """)
        self.ui.cmb_branch.clear()
        data = self.connection.selector(f"SELECT name FROM branches WHERE departmentID={department_id}")
        self.ui.cmb_branch.addItems(get_list_general(data))

    def class_loader(self):
        department_name = self.ui.cmb_department.currentText()
        department_id = self.connection.find(f"""SELECT id FROM departments WHERE name = "{department_name}" """)
        self.ui.cmb_class.clear()
        data = self.connection.selector(f"""SELECT name FROM classes WHERE departmentID={department_id}""")
        self.ui.cmb_class.addItem("")
        self.ui.cmb_class.addItems(get_list_general(data))

    def workplace_loader(self):
        self.ui.cmb_workplace.clear()
        data = self.connection.selector(f"""SELECT workplaces.name FROM workplaces JOIN branches ON branches.departmentID = workplaces.departmentID
                                            WHERE branches.name = "{self.ui.cmb_branch.currentText()}" """)
        self.ui.cmb_workplace.addItem("Okul")
        self.ui.cmb_workplace.addItems(get_list_general(data))

    def clean_data(self):
        self.ui.le_id_number.clear()
        self.ui.le_name.clear()
        self.ui.le_surname.clear()
        self.ui.le_number.clear()
        self.ui.le_father_name.clear()
        self.ui.le_mother_name.clear()
        self.ui.le_birth_place.clear()
        self.ui.cmb_department.setCurrentIndex(0)
        self.ui.cmb_workplace.setCurrentIndex(0)
        self.ui.le_coordinator.clear()
        self.ui.le_self_phone.clear()
        self.ui.le_father_phone.clear()
        self.ui.le_mother_phone.clear()
        self.ui.le_email.clear()
        self.ui.lbl_photo.clear()
        self.file_address = ""
        self.date_loader()
        self.branch_loader()
        self.class_loader()

    def closeEvent(self, event):
        self.connection.db_closer()


if __name__ == "__main__":
    app = QApplication([])
    window = StudentFromArchiveWindow()
    window.show()
    sys.exit(app.exec())
