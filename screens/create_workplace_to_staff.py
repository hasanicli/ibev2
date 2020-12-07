from PyQt5.QtWidgets import QApplication, QWidget, QAction
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

        self.ui.cmb_department.currentTextChanged.connect(lambda: self.ui.lw_staff_day.setCurrentItem(None))
        self.ui.cmb_neighborhood.currentTextChanged.connect(lambda: self.ui.lw_staff_day.setCurrentItem(None))

        self.ui.lw_staff.currentRowChanged.connect(self.staff_day_loader)
        self.ui.lw_staff_day.currentRowChanged.connect(self.suitable_wp_loader)
        self.ui.btn_add.clicked.connect(self.adding)
        self.ui.btn_sub.clicked.connect(self.subbing)

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

    # Burada text üzerinde oynama yapılabilir
    def suitable_wp_loader(self):
        self.ui.lw_appropriate_wp.clear()
        staff_item = self.ui.lw_staff.currentItem()
        staff_day_item = self.ui.lw_staff_day.currentItem()
        department_name = self.ui.cmb_department.currentText()
        neighborhood_name = self.ui.cmb_neighborhood.currentText()

        if department_name == "Hepsi" and neighborhood_name == "Hepsi" and staff_item is not None and staff_day_item is not None:
            # burada sınıfı olmayanlardan ötürü hata alıyoruz ve bunu sql ile halledilimek gerekiyor.
            pass
            # data = self.connection.selector(f"""SELECT workplaces.name, students.id_number, days.name FROM history
            #                                 JOIN workplaces ON workplaces.id = history.workplaceID
            #                                 JOIN students ON students.id_number = history.studentID
            #                                 JOIN classes_days ON students.classID = classes_days.classID
            #                                 JOIN days ON days.id = classes_days.dayID
            #                                 WHERE workplaces.staffID IS NULL AND workplaces.dayID IS NULL AND history.leaving_date IS NULL""")
            # appropriate_wp = self.intersection_day(data, staff_day_item.text())
            # self.ui.lw_appropriate_wp.addItems(appropriate_wp)

        # elif department_name == "Hepsi" and neighborhood_name != "Hepsi" and staff_item is not None and staff_day_item is not None:
        #     neighborhood_id = self.connection.find(f"""SELECT id FROM neighborhoods WHERE name = "{neighborhood_name}" """)
        #     data = self.connection.selector(f"""SELECT workplaces.name, students.id_number, days.name FROM history
        #                                                 JOIN workplaces ON workplaces.id = history.workplaceID
        #                                                 JOIN neighborhoods ON workplaces.neighborhoodID = neighborhoods.id
        #                                                 JOIN students ON students.id_number = history.studentID
        #                                                 JOIN classes_days ON students.classID = classes_days.classID
        #                                                 JOIN days ON days.id = classes_days.dayID
        #                                                 WHERE workplaces.staffID IS NULL AND workplaces.dayID IS NULL AND history.leaving_date IS NULL
        #                                                 AND workplaces.neighborhoodID = {neighborhood_id}""")
        #     appropriate_wp = self.intersection_day(data, staff_day_item.text())
        #     self.ui.lw_appropriate_wp.addItems(appropriate_wp)
        # elif department_name != "Hepsi" and neighborhood_name == "Hepsi" and staff_item is not None and staff_day_item is not None:
        #     department_id = self.connection.find(f"""SELECT id FROM departments WHERE name = "{department_name}" """)
        #     data = self.connection.selector(f"""SELECT workplaces.name, students.id_number, days.name FROM history
        #                                     JOIN workplaces ON workplaces.id = history.workplaceID
        #                                     JOIN students ON students.id_number = history.studentID
        #                                     JOIN classes_days ON students.classID = classes_days.classID
        #                                     JOIN days ON days.id = classes_days.dayID
        #                                     WHERE workplaces.staffID IS NULL
        #                                     AND workplaces.dayID IS NULL
        #                                     AND history.leaving_date IS NULL
        #                                     AND workplaces.departmentID = {department_id}
        #                                     """)
        #     appropriate_wp = self.intersection_day(data, staff_day_item.text())
        #     self.ui.lw_appropriate_wp.addItems(appropriate_wp)
        # elif department_name != "Hepsi" and neighborhood_name != "Hepsi" and staff_item is not None and staff_day_item is not None:
        #     neighborhood_id = self.connection.find(f"""SELECT id FROM neighborhoods WHERE name = "{neighborhood_name}" """)
        #     department_id = self.connection.find(f"""SELECT id FROM departments WHERE name = "{department_name}" """)
        #     data = self.connection.selector(f"""SELECT workplaces.name, students.id_number, days.name FROM history
        #                                                                         JOIN workplaces ON workplaces.id = history.workplaceID
        #                                                                         JOIN neighborhoods ON workplaces.neighborhoodID = neighborhoods.id
        #                                                                         JOIN departments ON workplaces.departmentID = departments.id
        #                                                                         JOIN students ON students.id_number = history.studentID
        #                                                                         JOIN classes_days ON students.classID = classes_days.classID
        #                                                                         JOIN days ON days.id = classes_days.dayID
        #                                                                         WHERE workplaces.staffID IS NULL
        #                                                                         AND workplaces.dayID IS NULL
        #                                                                         AND history.leaving_date IS NULL
        #                                                                         AND workplaces.neighborhoodID = {neighborhood_id}
        #                                                                         AND workplaces.departmentID = {department_id}
        #                                                                         """)
        #     appropriate_wp = self.intersection_day(data, staff_day_item.text())
        #     self.ui.lw_appropriate_wp.addItems(appropriate_wp)
        else:
            pass

    # workplace has to students. if you use the set statement, list widget(remaining workplace) show only one student even if workplace has more than one student
    def remaining_wp_loader(self):
        self.ui.lw_remaining_wp.clear()
        # data = set(self.connection.selector(f"""SELECT workplaces.name FROM workplaces JOIN history ON history.workplaceID = workplaces.id WHERE leaving_date IS NULL"""))
        data = self.connection.selector(f"""SELECT workplaces.name FROM workplaces JOIN history ON history.workplaceID = workplaces.id 
                                            WHERE history.leaving_date IS NULL AND workplaces.staffID IS NULL AND workplaces.dayID IS NULL """)
        self.ui.lw_remaining_wp.addItems(get_list_general(data))

    # get simple
    @staticmethod
    def intersection_day(p_data, p_staff_day):
        data = p_data
        staff_day = p_staff_day

        worpla = set()
        worpla_dict = dict()
        for i in data:
            worpla.add(i[0])
        for i in worpla:
            worpla_dict[i] = {}
        for i in data:
            worpla_dict[i[0]][i[1]] = []
        for i in data:
            worpla_dict[i[0]][i[1]].append(i[2])
        day_dict = dict()
        for i, j in worpla_dict.items():
            day_dict[i] = []
            for k, m in j.items():
                day_dict[i].append(set(m))
        intersection_dict = dict()
        for i, j in day_dict.items():
            temp_list = j[0]
            for k in j:
                temp_list = k.intersection(temp_list)
            intersection_dict[i] = temp_list
        return_list = list()
        for i, j in intersection_dict.items():
            if staff_day in j:
                return_list.append(i)
        return return_list

    def closeEvent(self, event):
        self.connection.db_closer()


if __name__ == "__main__":
    app = QApplication([])
    window = AddWorkplaceToStaff()
    window.show()
    sys.exit(app.exec())
