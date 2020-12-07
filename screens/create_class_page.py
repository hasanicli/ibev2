from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QAction,  QInputDialog, QLineEdit,  QCheckBox
import sys
from screens.add_class_python import Ui_Form
from connectionDB import DbManager
from control_page import *
from helper_function import *


class ClassWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Sınıf Ekle")

        self.connection = DbManager()

        self.first_state_of_days = set()

        locale.setlocale(locale.LC_COLLATE, ('tr_TR', 'UTF8'))

        self.ui.lw_class.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.lw_class.customContextMenuRequested.connect(self.right_click)

        self.ui.le_class.returnPressed.connect(self.recorder)

        get_out = QAction("Quit", self)
        get_out.triggered.connect(self.closeEvent)

        self.department_loader()
        self.class_loader()

        self.ui.btn_save.clicked.connect(self.recorder)
        self.ui.btn_edit.clicked.connect(self.updater)
        self.ui.btn_update.clicked.connect(self.updater_days)
        self.ui.btn_delete.clicked.connect(self.deleter)
        self.ui.cmb_department.currentTextChanged.connect(self.class_loader)
        self.ui.lw_class.currentRowChanged.connect(self.day_loader)
        self.ui.le_class.textChanged.connect(lambda: self.ui.lw_class.setCurrentItem(None))

    def get_list_widgets_items(self):
        return [self.ui.lw_class.item(index).text() for index in range(self.ui.lw_class.count())]

    def recorder(self):
        lw_items = self.get_list_widgets_items()
        class_name = tr_upper(stripper(self.ui.le_class.text()))
        if general_name_control(class_name, lw_items):
            department_id = self.connection.find(f"""SELECT id FROM departments WHERE name = "{self.ui.cmb_department.currentText()}" """)
            self.connection.recorder(f"""INSERT INTO classes(name, departmentID) VALUES("{class_name}", {department_id})""")
            class_id = self.connection.find(f"""SELECT id FROM classes WHERE name = "{class_name}" """)
            day_id_list = [self.connection.find(f""" SELECT id FROM days WHERE name="{i}" """) for i in [i.text() for i in self.ui.groupBox.findChildren(QCheckBox) if i.isChecked()]]
            for day_id in day_id_list:
                self.connection.recorder(f"""INSERT INTO classes_days(classID,dayID) VALUES({class_id}, {day_id})""")
            self.class_loader()
            focus_item(self.ui.le_class)

    def updater(self):
        item = self.ui.lw_class.currentItem()
        if item is not None:
            lw_items = self.get_list_widgets_items()
            old_class = item.text()
            new_class, ok_pressed = QInputDialog.getText(self, "Cevap ver", "Yeni Değer:", QLineEdit.Normal, old_class)
            new_class = tr_upper(stripper(new_class))
            if ok_pressed and general_name_control(new_class, lw_items):
                self.connection.updater(f"""UPDATE classes SET name = "{new_class}" WHERE name="{old_class}" """)
                self.class_loader()
        else:
            message_box("Önce seçim yapmalısınız!")
        focus_item(self.ui.le_class)

    def updater_days(self):
        item = self.ui.lw_class.currentItem()
        if item is not None:
            class_id = self.connection.find(f"""SELECT id FROM classes WHERE name = "{item.text()}" """)
            last_state_of_days = set([self.connection.find(f""" SELECT id FROM days WHERE name="{i}" """) for i in [i.text() for i in self.ui.groupBox.findChildren(QCheckBox) if i.isChecked()]])
            add_days = list(last_state_of_days.difference(self.first_state_of_days))
            sub_days = list(self.first_state_of_days.difference(last_state_of_days))
            if len(add_days) > 0:
                for day_id in add_days:
                    self.connection.recorder(f"""INSERT INTO classes_days(classID, dayID) VALUES({class_id}, {day_id})""")
            if len(sub_days) > 0:
                for day_id in sub_days:
                    self.connection.deleter(f"""DELETE FROM classes_days WHERE dayID = {day_id} AND classID = {class_id}""")
                self.settle_workplace(class_id, sub_days)
            self.class_loader()
            focus_item(self.ui.le_class)
        else:
            message_box("Önce seçim yapmalısınız!")

    def settle_workplace(self, p_class_id, p_day_list):
        wp_id_list = set(self.connection.selector(
            f"""SELECT workplaceID FROM history JOIN students ON students.id_number = history.studentID WHERE students.classID = {p_class_id} AND history.leaving_date IS NULL"""))
        message_box_list = ""
        for deleted_day_id in p_day_list:
            for wp_id in wp_id_list:
                wp_name = self.connection.find(f"""SELECT name FROM workplaces WHERE id ={wp_id[0]} """)
                staff_id = self.connection.find(f"""SELECT staffID FROM workplaces WHERE id ={wp_id[0]} """)
                day_id = self.connection.find(f"""SELECT dayID FROM workplaces WHERE id ={wp_id[0]} """)
                if staff_id is not None and day_id is not None:
                    staff_name = " ".join(self.connection.selector(f""" SELECT name, surname FROM staffs WHERE id_number = "{staff_id}" """)[0])
                    day_name = self.connection.find(f""" SELECT name FROM days WHERE id={day_id} """)
                    if deleted_day_id == day_id:
                        self.connection.updater(f"""UPDATE workplaces SET staffID = NULL, dayID = NULL WHERE id={wp_id[0]} and dayID = {deleted_day_id} """)
                        message_box_list += f"""{staff_name}'in {day_name} günü {wp_name} işletmesindeki görevi sıfırlanmıştır.\n"""
        if message_box_list != "":
            message_box(message_box_list)
        else:
            message_box("Bu degişiklikten kimse etkilenmedi")

    def deleter(self):
        item = self.ui.lw_class.currentItem()
        if item is not None:
            self.connection.deleter(f"""DELETE FROM classes WHERE name = "{item.text()}" """)
            self.class_loader()
        else:
            message_box("Önce seçim yapmalısınız!")
        focus_item(self.ui.le_class)

    def unset_checkbox(self):
        for day in self.ui.groupBox.findChildren(QCheckBox):
            day.setChecked(False)

    def day_loader(self):
        item = self.ui.lw_class.currentItem()
        if item is not None:
            self.first_state_of_days.clear()
            self.ui.le_class.setText(None)
            self.unset_checkbox()
            class_id = self.connection.find(f"""SELECT id FROM classes WHERE name = "{item.text()}" """)
            days_id_list = [i[0] for i in self.connection.selector(f""" SELECT dayID FROM classes_days WHERE classID={class_id}""")]
            days_name_list = [self.connection.find(f"""SELECT name FROM days WHERE id = {j} """) for j in days_id_list]
            day_item_list = self.ui.groupBox.findChildren(QCheckBox)
            for i in day_item_list:
                if i.text() in days_name_list:
                    i.setChecked(True)
            self.first_state_of_days = set(days_id_list)
        else:
            self.unset_checkbox()

    def department_loader(self):
        self.ui.cmb_department.clear()
        data = self.connection.selector("SELECT name FROM departments")
        self.ui.cmb_department.addItems(get_list_general(data))

    def class_loader(self):
        self.ui.lw_class.clear()
        self.unset_checkbox()
        if self.ui.cmb_department is not None:
            department_id = self.connection.find(f"""SELECT id FROM departments WHERE name = "{self.ui.cmb_department.currentText()}" """)
            data = self.connection.selector(f"""SELECT name FROM classes WHERE departmentID={department_id}""")
            self.ui.lw_class.addItems(get_list_general(data))

    def right_click(self, event):
        right_click_function(self, event, self.ui.lw_class)

    def closeEvent(self, event):
        self.connection.db_closer()


if __name__ == "__main__":
    app = QApplication([])
    window = ClassWindow()
    window.show()
    sys.exit(app.exec())
