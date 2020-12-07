from datetime import datetime
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QWidget, QAction, QLineEdit
import sys
from screens.add_change_workplace_python import Ui_Form
from connectionDB import DbManager
from helper_function import *


class ChangeWorkplaceWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Unvan Ekle")

        self.connection = DbManager()
        print(self.connection.connection_state())

        locale.setlocale(locale.LC_COLLATE, ('tr_TR', 'UTF8'))

        get_out = QAction("Quit", self)
        get_out.triggered.connect(self.closeEvent)

        self.student_loader()
        self.workplace_loader()

        self.ui.lw_students.doubleClicked.connect(self.data_loader)
        self.ui.lw_workplaces.doubleClicked.connect(self.workplace_selection)

        self.ui.btn_save.clicked.connect(self.recorder)
        self.ui.btn_delete.clicked.connect(self.data_clear)

    def recorder(self):
        pass
        # new_wp_name = self.ui.le_new_workplace.text()
        # old_wp_name = self.ui.le_old_workplace.text()
        # if new_wp_name != old_wp_name and new_wp_name != "" and old_wp_name != "":
        #     student_id = self.ui.le_id_number.text()
        #     class_name = self.ui.le_class.text()
        #     intersection_date = datetime.date(datetime(*QDate.getDate(self.ui.date_starting.date())))
        #
        #     if class_name == "":
        #         class_day_id_list = [day[0] for day in self.connection.selector(f""" SELECT id FROM days""")]
        #     else:
        #         class_id = self.connection.find(f"""SELECT id FROM classes WHERE name = "{class_name}" """)
        #         class_day_id_list = [day[0] for day in self.connection.selector(f""" SELECT dayID FROM classes_days WHERE classID={class_id}""")]
        #
        #     if new_wp_name != "Okul" and old_wp_name != "Okul":
        #         new_wp_id = self.connection.find(f""" SELECT id FROM workplaces WHERE name = "{new_wp_name}" """)
        #         old_wp_id = self.connection.find(f""" SELECT id FROM workplaces WHERE name = "{old_wp_name}" """)
        #         old_wp_stu_number = self.connection.find(f"""SELECT COUNT(workplaceID) from history WHERE workplaceID={old_wp_id} AND leaving_date IS NULL """)
        #         new_wp_staff_id, new_wp_day_id = self.connection.selector(f"""SELECT staffID, dayID FROM workplaces WHERE id = {new_wp_id}""")[0]
        #         self.connection.updater(
        #             f"""UPDATE history SET leaving_date="{intersection_date}" WHERE studentID="{student_id}" AND workplaceID={old_wp_id} AND leaving_date IS NULL """)
        #         self.connection.recorder(f"""INSERT INTO history (studentID, workplaceID, starting_date) VALUES("{student_id}", {new_wp_id}, "{intersection_date}")""")
        #         if old_wp_stu_number == 1:
        #             self.connection.updater(f"""UPDATE workplaces SET staffID=NULL, dayID = NULL WHERE id={old_wp_id}""")
        #         if new_wp_day_id not in class_day_id_list:
        #             self.connection.updater(f"""UPDATE workplaces SET staffID=NULL, dayID = NULL WHERE id={new_wp_id}""")
        #
        #     elif new_wp_name == "Okul" and old_wp_name != "Okul":
        #         old_wp_id = self.connection.find(f""" SELECT id FROM workplaces WHERE name = "{old_wp_name}" """)
        #         old_wp_stu_number = self.connection.find(f"""SELECT COUNT(workplaceID) from history WHERE workplaceID={old_wp_id} AND leaving_date IS NULL """)
        #         old_wp_staff_id = self.connection.find(f"""SELECT staffID FROM workplaces WHERE id = {old_wp_id}""")
        #         if old_wp_staff_id is None:
        #             self.connection.recorder(f"""INSERT INTO temp_workplace(studentID, starting_date) VALUES("{student_id}", "{intersection_date}")""")
        #         else:
        #             self.connection.recorder(f"""INSERT INTO temp_workplace(studentID, staffID, starting_date) VALUES("{student_id}", "{old_wp_staff_id}", "{intersection_date}")""")
        #
        #         self.connection.updater(f"""UPDATE students SET is_going= "H" WHERE id_number="{student_id}" """)
        #         self.connection.updater(f"""UPDATE history SET leaving_date="{intersection_date}" WHERE studentID="{student_id}" AND workplaceID={old_wp_id} AND leaving_date IS NULL """)
        #
        #         if old_wp_stu_number == 1:
        #             self.connection.updater(f"""UPDATE workplaces SET staffID=NULL, dayID = NULL WHERE id={old_wp_id}""")
        #     elif new_wp_name != "Okul" and old_wp_name == "Okul":
        #         new_wp_id = self.connection.find(f""" SELECT id FROM workplaces WHERE name = "{new_wp_name}" """)
        #         new_wp_staff_id, new_wp_day_id = self.connection.selector(f"""SELECT staffID, dayID FROM workplaces WHERE id = {new_wp_id}""")[0]
        #
        #         self.connection.deleter(f"""DELETE FROM temp_workplace WHERE studentID="{student_id}" """)
        #         self.connection.recorder(f"""INSERT INTO history (studentID, workplaceID, starting_date) VALUES("{student_id}", {new_wp_id}, "{intersection_date}")""")
        #         self.connection.updater(f"""UPDATE students SET is_going="{"E"}" WHERE id_number="{student_id}" """)
        #
        #         if new_wp_day_id not in class_day_id_list:
        #             self.connection.updater(f"""UPDATE workplaces SET staffID=NULL, dayID = NULL WHERE id={new_wp_id}""")
        #     else:
        #         pass
        # self.data_clear()

    def student_loader(self):
        pass
        # self.ui.lw_students.clear()
        # data = self.connection.selector(f""" SELECT name, surname, id_number FROM students WHERE is_active="E" """)
        # self.ui.lw_students.addItems(get_list_personal(data))
        # self.ui.date_starting.setDate(datetime.date(datetime.now()))

    def workplace_loader(self):
        pass
        # self.ui.lw_workplaces.clear()
        # data = self.connection.selector("SELECT name FROM workplaces")
        # self.ui.lw_workplaces.addItems(get_list_general(data))
        # self.ui.lw_workplaces.insertItem(0, "Okul")

    def data_clear(self):
        pass
        # self.ui.le_id_number.setText(None)
        # self.ui.le_number.setText(None)
        # self.ui.le_name.setText(None)
        # self.ui.le_class.setText(None)
        # self.ui.le_old_workplace.setText(None)
        # self.ui.le_coordinator.setText(None)
        # self.ui.le_new_workplace.setText(None)

    def data_loader(self):
        pass
        # item = self.ui.lw_students.currentItem()
        # if item is not None:
        #     id_number = find_id_number(item.text())
        #     info = self.connection.selector(f"""SELECT * FROM students WHERE id_number = "{id_number}" AND is_active="{"E"}" """)
        #     name = info[0][1]
        #     surname = info[0][2]
        #     full_name = " ".join([name, surname])
        #     school_number = info[0][3]
        #     class_id = info[0][5]
        #     class_name = ""
        #     if class_id is not None:
        #         class_name = self.connection.find(f"""SELECT name FROM classes WHERE id = {class_id}""")
        #     is_going = info[0][11]
        #     workplace_name = "Okul"
        #     coordinator_name = ""
        #
        #
        #     if is_going == "E":
        #         workplace_id = self.connection.find(f"""SELECT workplaceID FROM history WHERE studentID = "{id_number}" AND leaving_date IS NULL""")
        #         workplace_name, coordinator_id = self.connection.selector(f"""SELECT name, staffID FROM workplaces WHERE id = {workplace_id}""")[0]
        #         if coordinator_id is not None:
        #             first, second = self.connection.selector(f"""SELECT name, surname FROM staffs WHERE id_number = "{coordinator_id}" """)[0]
        #             coordinator_name = " ".join([first, second])
        #         else:
        #             pass
        #
        #     else:
        #         coordinator_id = self.connection.find(f"""SELECT staffID FROM temp_workplace WHERE studentID = "{id_number}" """)
        #         if coordinator_id is None:
        #             coordinator_name = ""
        #         else:
        #             first, second = self.connection.selector(f"""SELECT name, surname FROM staffs WHERE id_number = "{coordinator_id}" """)
        #             coordinator_name = " ".join([first, second])
        #     self.ui.le_id_number.setText(id_number)
        #     self.ui.le_number.setText(school_number)
        #     self.ui.le_name.setText(full_name)
        #
        #     self.ui.le_class.setText(class_name)
        #     self.ui.le_old_workplace.setText(workplace_name)
        #     self.ui.le_coordinator.setText(coordinator_name)

    def workplace_selection(self):
        pass
        # item = self.ui.lw_workplaces.currentItem()
        # if item is not None:
        #     self.ui.le_new_workplace.setText(item.text())

    def closeEvent(self, event):
        self.connection.db_closer()


if __name__ == "__main__":
    app = QApplication([])
    window = ChangeWorkplaceWindow()
    window.show()
    sys.exit(app.exec())
