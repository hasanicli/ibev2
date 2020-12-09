from PyQt5.QtWidgets import QApplication, QWidget, QAction, QMessageBox
import sys
from screens.add_workplace_to_staff_python import Ui_Form
from connectionDB import DbManager
from helper_function import *


class AddWorkplaceToStaff(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Üst sınıfa alt sınıf ekle")
        self.connection = DbManager()
        get_out = QAction("Quit", self)
        get_out.triggered.connect(self.closeEvent)
        self.first_load()

        self.ui.cmb_staff_branch.currentTextChanged.connect(self.staff_loader)

        self.ui.cmb_department.currentTextChanged.connect(self.suitable_wp_loader)
        self.ui.cmb_neighborhood.currentTextChanged.connect(self.suitable_wp_loader)

        self.ui.lw_staff.currentRowChanged.connect(self.staff_day_loader)
        self.ui.lw_staff_day.currentRowChanged.connect(self.suitable_wp_loader)
        self.ui.btn_add.clicked.connect(self.adding)
        self.ui.btn_sub.clicked.connect(self.subbing)
        self.ui.btn_neigh_staff.clicked.connect(self.show_wp_with_neighborhood)
        self.ui.btn_staff_wp_num.clicked.connect(self.show_number_of_wp_for_staffs)

    def show_wp_with_neighborhood(self):
        neighborhood = self.ui.cmb_neighborhood.currentText()
        if neighborhood != "Hepsi":
            neighborhood_id = self.connection.find(f"""SELECT id FROM neighborhoods WHERE name = "{neighborhood}" """)
            data = self.connection.selector(f"""SELECT name, departmentID, staffID FROM workplaces WHERE neighborhoodID={neighborhood_id} AND staffID IS NOT NULL AND dayID IS NOT NULL""")
            info = ""
            for wp_name, department_id, staff_id in data:
                staff_name = [" ".join(name_surname) for name_surname in self.connection.selector(f"""SELECT name, surname FROM staffs WHERE id_number="{staff_id}" """)]
                department_name = self.connection.find(f"""SELECT name FROM departments WHERE id={department_id} """)
                info += wp_name + "--" + department_name + "--" + str(*staff_name) + "\n"
            QMessageBox.information(self, "Bilgi", info)

    def show_number_of_wp_for_staffs(self):
        wp_list = []
        for i in range(self.ui.lw_staff.count()):
            staff_name = self.ui.lw_staff.item(i).text()[:-2]
            staff_id = find_id_number(self.ui.lw_staff.item(i).text())
            number = self.connection.find(f"""SELECT COUNT(name) FROM workplaces WHERE staffID="{staff_id}" """)
            print(staff_id, staff_name)
            wp_list.append(str(number) + "--" + staff_name + "\n")
            # text += staff_name + "--" + str(number) + "\n"

        wp_list.sort()
        text = ""
        for i in wp_list:
            text += i
        QMessageBox.information(self, "Bilgi", text)

    def first_load(self):
        self.department_loader()
        self.staff_branch_loader()
        self.neighborhood_loader()
        self.staff_loader()
        self.remaining_wp_loader()

    def adding(self):
        staff_item = self.ui.lw_staff.currentItem()
        staff_day_item = self.ui.lw_staff_day.currentItem()
        workplace_item = self.ui.lw_appropriate_wp.currentItem()
        if workplace_item is not None:
            staff_id_number = find_id_number(staff_item.text())
            day_id = self.connection.find(f"""SELECT id FROM days WHERE name = "{staff_day_item.text()}" """)
            self.connection.updater(f"""UPDATE workplaces SET staffID = "{staff_id_number}", dayID = {day_id} WHERE name="{workplace_item.text()}" """)
            self.remaining_wp_loader()
            self.staff_day_loader()

    def subbing(self):
        workplace_item = self.ui.lw_assigned_wp.currentItem()
        if workplace_item is not None:
            self.connection.updater(f"""UPDATE workplaces SET staffID = NULL, dayID = NULL WHERE name="{workplace_item.text()}" """)
            self.remaining_wp_loader()
            self.staff_day_loader()

    def department_loader(self):
        self.ui.cmb_department.clear()
        data = [i[0] for i in self.connection.selector(f"""SELECT name FROM departments """)]
        self.ui.cmb_department.insertItem(0, "Hepsi")
        self.ui.cmb_department.addItems(data)

    def staff_branch_loader(self):
        self.ui.cmb_staff_branch.clear()
        data = [i[0] for i in self.connection.selector(f"""SELECT name FROM staff_branches """)]
        self.ui.cmb_staff_branch.insertItem(0, "Hepsi")
        self.ui.cmb_staff_branch.addItems(data)

    def neighborhood_loader(self):
        self.ui.cmb_neighborhood.clear()
        data = [i[0] for i in self.connection.selector(f"""SELECT name FROM neighborhoods """)]
        self.ui.cmb_neighborhood.insertItem(0, "Hepsi")
        self.ui.cmb_neighborhood.addItems(data)

    def staff_loader(self):
        self.ui.lw_staff.clear()
        self.ui.lw_staff_day.clear()
        branch_name = self.ui.cmb_staff_branch.currentText()
        if branch_name == "Hepsi":
            data = self.connection.selector(f""" SELECT name, surname, id_number FROM staffs """)
            self.ui.lw_staff.addItems(get_list_personal(data))
        else:
            staff_branch_id = self.connection.find(f"""SELECT id FROM staff_branches WHERE name = "{branch_name}" """)
            data = self.connection.selector(f"""SELECT name, surname, id_number FROM staffs WHERE staff_branchID={staff_branch_id}""")
            self.ui.lw_staff.addItems(get_list_personal(data))

    def staff_day_loader(self):
        staff_item = self.ui.lw_staff.currentItem()
        if staff_item is not None:
            self.ui.lw_staff_day.clear()
            self.ui.lw_assigned_wp.clear()
            staff_id = find_id_number(staff_item.text())
            days = [i[0] for i in self.connection.selector(f"""SELECT name FROM staffs_days JOIN days ON days.id = staffs_days.dayID WHERE staffs_days.staffID = "{staff_id}" """)]
            self.ui.lw_staff_day.addItems(days)
            workplaces = self.connection.selector(f"""SELECT name FROM workplaces WHERE staffID = "{staff_id}" """)
            self.ui.lw_assigned_wp.addItems(get_list_general(workplaces))

    def suitable_wp_loader(self):
        self.ui.lw_appropriate_wp.clear()
        staff_item = self.ui.lw_staff.currentItem()
        staff_day_item = self.ui.lw_staff_day.currentItem()
        department_name = self.ui.cmb_department.currentText()
        neighborhood_name = self.ui.cmb_neighborhood.currentText()

        if department_name == "Hepsi" and neighborhood_name == "Hepsi" and staff_item is not None and staff_day_item is not None:
            staff_day_id = self.connection.find(f"""SELECT id FROM days WHERE name = "{staff_day_item.text()}" """)
            data = self.connection.selector(f"""SELECT workplaces.name, history.studentID FROM history JOIN workplaces ON workplaces.id = history.workplaceID
            WHERE workplaces.staffID IS NULL AND workplaces.dayID IS NULL AND history.leaving_date IS NULL""")
            self.settle(staff_day_id, data)

        elif department_name == "Hepsi" and neighborhood_name != "Hepsi" and staff_item is not None and staff_day_item is not None:
            neighborhood_id = self.connection.find(f"""SELECT id FROM neighborhoods WHERE name = "{self.ui.cmb_neighborhood.currentText()}" """)
            staff_day_id = self.connection.find(f"""SELECT id FROM days WHERE name = "{staff_day_item.text()}" """)
            data = self.connection.selector(f"""SELECT workplaces.name, history.studentID FROM history JOIN workplaces ON workplaces.id = history.workplaceID
            WHERE workplaces.neighborhoodID = {neighborhood_id} AND workplaces.staffID IS NULL AND workplaces.dayID IS NULL AND history.leaving_date IS NULL""")
            self.settle(staff_day_id, data)

        elif department_name != "Hepsi" and neighborhood_name == "Hepsi" and staff_item is not None and staff_day_item is not None:
            department_id = self.connection.find(f"""SELECT id FROM departments WHERE name = "{self.ui.cmb_department.currentText()}" """)
            staff_day_id = self.connection.find(f"""SELECT id FROM days WHERE name = "{staff_day_item.text()}" """)
            data = self.connection.selector(f"""SELECT workplaces.name, history.studentID FROM history JOIN workplaces ON workplaces.id = history.workplaceID
                        WHERE workplaces.departmentID = {department_id} AND workplaces.staffID IS NULL AND workplaces.dayID IS NULL AND history.leaving_date IS NULL""")
            self.settle(staff_day_id, data)

        elif department_name != "Hepsi" and neighborhood_name != "Hepsi" and staff_item is not None and staff_day_item is not None:
            neighborhood_id = self.connection.find(f"""SELECT id FROM neighborhoods WHERE name = "{self.ui.cmb_neighborhood.currentText()}" """)
            department_id = self.connection.find(f"""SELECT id FROM departments WHERE name = "{self.ui.cmb_department.currentText()}" """)
            staff_day_id = self.connection.find(f"""SELECT id FROM days WHERE name = "{staff_day_item.text()}" """)
            data = self.connection.selector(f"""SELECT workplaces.name, history.studentID FROM history JOIN workplaces ON workplaces.id = history.workplaceID
            WHERE workplaces.neighborhoodID = {neighborhood_id} AND workplaces.departmentID = {department_id}
            AND workplaces.staffID IS NULL AND workplaces.dayID IS NULL AND history.leaving_date IS NULL""")
            self.settle(staff_day_id, data)

    def settle(self, p_staff_day_id, p_data):
        staff_day_id = p_staff_day_id
        data = p_data
        all_days = {day[0] for day in self.connection.selector(f"""SELECT id FROM days""")}

        wp_day_dict = {}
        wp_names = {i[0] for i in data}
        for i in wp_names:
            wp_day_dict[i] = all_days

        for wp, tc in data:
            class_id = self.connection.find(f"""SELECT classID FROM students WHERE id_number = "{tc}" """)
            wp_day_id_list = all_days
            if class_id is not None:
                wp_day_id_list = {day[0] for day in self.connection.selector(f"""SELECT dayID FROM classes_days WHERE classID = "{class_id}" """)}
            wp_day_dict[wp] = wp_day_id_list.intersection(wp_day_dict[wp])

        appropriate_wp_list = []
        for wp, days in wp_day_dict.items():
            if staff_day_id in days:
                appropriate_wp_list.append(wp)

        self.ui.lw_appropriate_wp.addItems(appropriate_wp_list)

    # workplace has to students. if you use the set statement, list widget(remaining workplace) show only one student even if workplace has more than one student
    def remaining_wp_loader(self):
        self.ui.lw_remaining_wp.clear()
        # data = set(self.connection.selector(f"""SELECT workplaces.name FROM workplaces JOIN history ON history.workplaceID = workplaces.id WHERE leaving_date IS NULL"""))
        data = self.connection.selector(f"""SELECT workplaces.name FROM workplaces JOIN history ON history.workplaceID = workplaces.id 
                                            WHERE history.leaving_date IS NULL AND workplaces.staffID IS NULL AND workplaces.dayID IS NULL """)
        self.ui.lw_remaining_wp.addItems(get_list_general(data))

    def closeEvent(self, event):
        self.connection.db_closer()


if __name__ == "__main__":
    app = QApplication([])
    window = AddWorkplaceToStaff()
    window.show()
    sys.exit(app.exec())
