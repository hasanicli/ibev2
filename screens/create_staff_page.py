from PyQt5.QtWidgets import QApplication, QWidget, QAction, QCheckBox
import sys
from screens.add_staff_python import Ui_Form
from connectionDB import DbManager
from control_page import *
from helper_function import *


class StaffWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Öğretmen Ekle")

        self.connection = DbManager()

        self.first_state_of_days = set()
        self.old_id_number = ""

        locale.setlocale(locale.LC_COLLATE, ('tr_TR', 'UTF8'))

        get_out = QAction("Quit", self)
        get_out.triggered.connect(self.closeEvent)

        self.branch_loader()
        self.degree_loader()
        self.staff_loader()

        self.ui.btn_save.clicked.connect(lambda: self.generate_value(self.recorder))
        self.ui.btn_edit.clicked.connect(lambda: self.obj_control(self.updater, self.ui.lw_staff))
        self.ui.btn_delete.clicked.connect(lambda: self.obj_control(self.deleter, self.ui.lw_staff))
        self.ui.lw_staff.currentRowChanged.connect(lambda: self.obj_control(self.data_loader, self.ui.lw_staff))
        self.ui.le_identity_number.textChanged.connect(self.text_change_control)

    def text_change_control(self):
        if self.ui.le_identity_number.text() == "":
            self.cleaner()

    def obj_control(self, func, obj):
        if func.__name__ != "data_loader" and obj.currentItem() is None:
            message_box("Önce seçim yapmalısınız!")
        elif func.__name__ == "data_loader" and obj.currentItem() is not None:
            id_number = find_id_number(obj.currentItem().text())
            func(id_number)
        elif func.__name__ == "deleter" and obj.currentItem() is not None:
            id_number = find_id_number(obj.currentItem().text())
            func(id_number)
        elif func.__name__ == "updater" and obj.currentItem() is not None:
            self.generate_value(func)

    def generate_value(self, func):
        dict_kw = {"id_number": self.ui.le_identity_number.text(), "name": tr_capitalize(stripper(self.ui.le_name.text())), "surname": tr_capitalize(stripper(self.ui.le_surname.text())),
                   "branch_name": self.ui.cmb_staff_branch.currentText(),
                   "branch_id": self.connection.find(f"""SELECT id FROM staff_branches WHERE name="{self.ui.cmb_staff_branch.currentText()}" """),
                   "degree_name": self.ui.cmb_staff_degree.currentText(), "degree_id": self.connection.find(f"""SELECT id FROM staff_degrees WHERE name="{self.ui.cmb_staff_degree.currentText()}" """),
                   "phone": self.ui.le_phone_number.text(), "email": self.ui.le_mail.text()}

        li_days = [i.text() for i in self.ui.groupBox.findChildren(QCheckBox) if i.isChecked()]

        func(li_days, **dict_kw)

    def cleaner(self):
        self.ui.lw_staff.setCurrentItem(None)
        self.ui.le_name.setText(None)
        self.ui.le_surname.setText(None)
        self.ui.le_phone_number.setText(None)
        self.ui.le_mail.setText(None)
        self.ui.cmb_staff_branch.setCurrentIndex(0)
        self.ui.cmb_staff_degree.setCurrentIndex(0)
        self.unset_checkbox()

    def recorder(self, day_list, **kwargs):
        id_numbers = find_id_numbers(self.ui.lw_staff)
        day_id_list = [self.connection.find(f""" SELECT id FROM days WHERE name="{i}" """) for i in day_list]
        control_list = [identity_number_control(kwargs["id_number"], id_numbers), name_control(kwargs["name"]), surname_control(kwargs["surname"])]
        if False not in control_list:
            self.connection.recorder(f"""INSERT INTO staffs VALUES("{kwargs["id_number"]}", "{kwargs["name"]}", "{kwargs["surname"]}", {kwargs["branch_id"]}, {kwargs["degree_id"]},
                                        "{kwargs["phone"]}", "{kwargs["email"]}")""")
            for day_id in day_id_list:
                self.connection.recorder(f"""INSERT INTO staffs_days(staffID,dayID) VALUES("{kwargs["id_number"]}", {day_id})""")
            self.staff_loader()
        self.ui.le_identity_number.clear()

    def updater(self, day_list, **kwargs):
        id_numbers = find_id_numbers(self.ui.lw_staff)

        if self.old_id_number == kwargs["id_number"]:
            control_list = [name_control(kwargs["name"]), surname_control(kwargs["surname"])]
        else:
            control_list = [identity_number_control(kwargs["id_number"], id_numbers), name_control(kwargs["name"]), surname_control(kwargs["surname"])]

        if False not in control_list:
            self.connection.updater(f"""UPDATE staffs SET id_number = "{kwargs["id_number"]}", name = "{kwargs["name"]}", surname="{kwargs["surname"]}", staff_branchID= {kwargs["branch_id"]},
                                    staff_degreeID={kwargs["degree_id"]}, phone_number="{kwargs["phone"]}", email="{kwargs["email"]}" WHERE id_number="{self.old_id_number}"  """)
            last_state_of_days = set([self.connection.find(f""" SELECT id FROM days WHERE name="{i}" """) for i in day_list])
            add_days = list(last_state_of_days.difference(self.first_state_of_days))
            sub_days = list(self.first_state_of_days.difference(last_state_of_days))
            if len(add_days) > 0:
                for day_id in add_days:
                    self.connection.recorder(f"""INSERT INTO staffs_days(staffID, dayID) VALUES("{kwargs["id_number"]}", {day_id})""")
            if len(sub_days) > 0:
                for day_id in sub_days:
                    self.connection.deleter(f"""DELETE FROM staffs_days WHERE dayID = {day_id} AND staffID = "{kwargs["id_number"]}" """)
                    number_of_wp = self.connection.selector(f""" SELECT COUNT(staffID) FROM workplaces  WHERE staffID = {kwargs["id_number"]} AND dayID={day_id} """)[0][0]
                    if number_of_wp > 0:
                        wp_name = self.connection.find(f"""SELECT name FROM workplaces WHERE staffID="{kwargs["id_number"]}" and dayID={day_id}""")
                        self.connection.updater(f"""UPDATE workplaces SET staffID = NULL, dayID = NULL WHERE staffID="{kwargs["id_number"]}" and dayID={day_id} """)
                        day_name = self.connection.find(f"""SELECT name FROM days WHERE id={day_id}""")
                        message_box(f"""{kwargs["name"]} {kwargs["surname"]} 'nin {wp_name} işletmesinde\n{day_name} günü olan görevi sona ermiştir.""")
            self.ui.le_identity_number.clear()
            self.staff_loader()

    def deleter(self, id_number):
        self.connection.updater(f"""UPDATE workplaces SET staffID = NULL, dayID = NULL WHERE staffID="{id_number}" """)
        self.connection.updater(f"""UPDATE temp_workplace SET staffID = NULL WHERE staffID="{id_number}" """)
        self.connection.updater(f"""UPDATE school_info SET managerID = NULL WHERE managerID="{id_number}" """)
        self.connection.updater(f"""UPDATE school_info SET coordinator_managerID = NULL WHERE coordinator_managerID="{id_number}" """)
        self.connection.deleter(f"""DELETE FROM staffs_days WHERE staffID = "{id_number}"  """)
        self.connection.deleter(f"""DELETE FROM staffs WHERE id_number = "{id_number}" """)
        self.staff_loader()
        self.ui.le_identity_number.clear()

    def unset_checkbox(self):
        for day in self.ui.groupBox.findChildren(QCheckBox):
            day.setChecked(False)

    def data_loader(self, id_number):
        self.first_state_of_days.clear()
        staff_info = list(self.connection.selector(f""" SELECT * FROM staffs WHERE id_number="{id_number}" """)[0])
        days_id_list = [i[0] for i in self.connection.selector(f""" SELECT dayID FROM staffs_days WHERE staffID="{id_number}" """)]
        days_name_list = [self.connection.find(f"""SELECT name FROM days WHERE id = {j} """) for j in days_id_list]

        branch = self.connection.find(f"""SELECT name FROM staff_branches WHERE id = "{staff_info[3]}" """)
        degree = self.connection.find(f"""SELECT name FROM staff_degrees WHERE id = "{staff_info[4]}" """)
        self.ui.le_identity_number.setText(staff_info[0])
        self.ui.le_name.setText(staff_info[1])
        self.ui.le_surname.setText(staff_info[2])
        self.ui.cmb_staff_branch.setCurrentText(branch)
        self.ui.cmb_staff_degree.setCurrentText(degree)
        self.ui.le_phone_number.setText(staff_info[5])
        self.ui.le_mail.setText(staff_info[6])

        self.unset_checkbox()
        day_item_list = self.ui.groupBox.findChildren(QCheckBox)
        for i in day_item_list:
            if i.text() in days_name_list:
                i.setChecked(True)
        self.old_id_number = id_number
        self.first_state_of_days = set(days_id_list)

    def branch_loader(self):
        self.ui.cmb_staff_branch.clear()
        data = self.connection.selector(f"""SELECT name FROM staff_branches """)
        self.ui.cmb_staff_branch.addItems(get_list_general(data))

    def degree_loader(self):
        self.ui.cmb_staff_degree.clear()
        data = self.connection.selector("SELECT name FROM staff_degrees")
        self.ui.cmb_staff_degree.addItems(get_list_general(data))

    def staff_loader(self):
        self.ui.lw_staff.clear()
        data = self.connection.selector(f""" SELECT name, surname, id_number FROM staffs """)
        self.ui.lw_staff.addItems(get_list_personal(data))
        for day in self.ui.groupBox.findChildren(QCheckBox):
            day.setChecked(False)

    def closeEvent(self, event):
        self.connection.db_closer()


if __name__ == "__main__":
    app = QApplication([])
    window = StaffWindow()
    window.show()
    sys.exit(app.exec())
