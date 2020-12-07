from PyQt5.QtWidgets import QApplication, QWidget, QAction
import sys
from screens.add_workplace_python import Ui_Form
from connectionDB import DbManager
from control_page import *
from helper_function import *


class WorkplaceWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("İşletme Bilgileri Ekle")
        self.connection = DbManager()
        locale.setlocale(locale.LC_COLLATE, ('tr_TR', 'UTF8'))
        get_out = QAction("Quit", self)
        get_out.triggered.connect(self.closeEvent)

        # self.old_wp_id = None
        self.old_wp_name = ""
        self.workplace_loader()
        self.department_loader()
        self.neighborhood_loader()

        self.ui.btn_save.clicked.connect(lambda: self.obj_control(self.recorder, self.ui.lw_workplace))
        self.ui.btn_edit.clicked.connect(lambda: self.obj_control(self.updater, self.ui.lw_workplace))
        self.ui.btn_delete.clicked.connect(lambda: self.obj_control(self.deleter, self.ui.lw_workplace))
        self.ui.lw_workplace.currentRowChanged.connect(lambda: self.obj_control(self.data_loader, self.ui.lw_workplace))
        self.ui.le_workplace_name.textChanged.connect(self.text_change_control)

    def text_change_control(self):
        if self.ui.le_workplace_name.text() == "":
            self.cleaner()

    def obj_control(self, func, obj):
        if func.__name__ == "recorder":
            self.ui.lw_workplace.setCurrentItem(None)
            self.generate_value(func)
        elif func.__name__ != "data_loader" and obj.currentItem() is None:
            message_box("Önce seçim yapmalısınız!")
        elif func.__name__ == "data_loader" and obj.currentItem() is not None:
            func(obj.currentItem())
        elif func.__name__ == "updater" and obj.currentItem() is not None:
            self.generate_value(func)
        elif func.__name__ == "deleter" and obj.currentItem() is not None:
            func(obj.currentItem())

    def generate_value(self, func):
        gc = "E"
        if not self.ui.cb_request.isChecked():
            gc = "H"
        li_kw = {"wp_name": tr_capitalize(stripper(self.ui.le_workplace_name.text())), "boss": tr_capitalize(stripper(self.ui.le_boss.text())),
                 "department_id": self.connection.find(f"""SELECT id FROM departments WHERE name = "{self.ui.cmb_department.currentText()}" """),
                 "wp_mi": tr_capitalize(stripper(self.ui.le_master_instructive.text())),
                 "neigh_id": self.connection.find(f"""SELECT id FROM neighborhoods WHERE name = "{self.ui.cmb_neighborhood.currentText()}" """),
                 "street": tr_capitalize(stripper(self.ui.le_street.text())), "address_number": self.ui.le_number.text(), "phone1": self.ui.le_phone1.text(), "phone2": self.ui.le_phone2.text(),
                 "email": self.ui.le_email.text(), "gc": gc}
        func(**li_kw)

    def cleaner(self):
        self.ui.lw_workplace.setCurrentItem(None)
        self.ui.cmb_department.setCurrentIndex(0)
        # self.ui.le_workplace_name.clear()
        self.ui.le_boss.clear()
        self.ui.le_master_instructive.clear()
        self.ui.le_coordinator.clear()
        self.ui.cmb_neighborhood.setCurrentIndex(0)
        self.ui.le_street.clear()
        self.ui.le_number.clear()
        self.ui.le_phone1.clear()
        self.ui.le_phone2.clear()
        self.ui.le_email.clear()
        self.ui.cb_request.setChecked(True)

    def get_list_widgets_items(self):
        return [self.ui.lw_workplace.item(index).text() for index in range(self.ui.lw_workplace.count())]

    def recorder(self, **p_dict):
        lw_items = self.get_list_widgets_items()
        control_list = [general_name_control(p_dict["wp_name"], lw_items), name_control(p_dict["boss"]), name_control(p_dict["wp_mi"])]
        if False not in control_list:
            self.connection.recorder(
                f"""INSERT INTO workplaces(name, boss, departmentID, master_instructive, neighborhoodID, street, address_number, phone_number1,phone_number2, email, government_contribution)
                    VALUES("{p_dict["wp_name"]}", "{p_dict["boss"]}", {p_dict["department_id"]}, "{p_dict["wp_mi"]}", {p_dict["neigh_id"]}, "{p_dict["street"]}", "{p_dict["address_number"]}", 
                            "{p_dict["phone1"]}", "{p_dict["phone2"]}", "{p_dict["email"]}" , "{p_dict["gc"]}" ) """)
        self.workplace_loader()
        focus_item(self.ui.le_workplace_name)
        # self.cleaner()
        self.ui.le_workplace_name.clear()

    def deleter(self, p_item):
        item_id = self.connection.find(f"""SELECT id FROM workplaces WHERE name="{p_item.text()}" """)
        self.connection.deleter(f"""DELETE FROM workplaces WHERE id = {item_id} """)
        self.workplace_loader()
        self.ui.le_workplace_name.clear()
        # self.cleaner()

    def updater(self, **p_dict):
        lw_items = self.get_list_widgets_items()
        if p_dict["wp_name"] == self.old_wp_name:
            control_list = [name_control(p_dict["boss"]), name_control(p_dict["wp_mi"])]
        else:
            control_list = [general_name_control(p_dict["wp_name"], lw_items), name_control(p_dict["boss"]), name_control(p_dict["wp_mi"])]
        if False not in control_list:
            self.connection.updater(f"""UPDATE workplaces SET name="{p_dict["wp_name"]}", departmentID={p_dict["department_id"]}, boss="{p_dict["boss"]}", master_instructive="{p_dict["wp_mi"]}",
                                    neighborhoodID={p_dict["neigh_id"]}, street="{p_dict["street"]}", address_number="{p_dict["address_number"]}", phone_number1="{p_dict["phone1"]}",
                                    phone_number2="{p_dict["phone2"]}", email="{p_dict["email"]}", government_contribution="{p_dict["gc"]}" WHERE name="{self.old_wp_name}" """)
        self.ui.le_workplace_name.clear()
        self.workplace_loader()
        focus_item(self.ui.le_workplace_name)

    def workplace_loader(self):
        self.ui.lw_workplace.clear()
        data = self.connection.selector(f"""SELECT name FROM workplaces """)
        self.ui.lw_workplace.addItems(get_list_general(data))

    def department_loader(self):
        self.ui.cmb_department.clear()
        data = self.connection.selector(f"""SELECT name FROM departments """)
        self.ui.cmb_department.addItems(get_list_general(data))

    def neighborhood_loader(self):
        self.ui.cmb_neighborhood.clear()
        data = self.connection.selector(f"""SELECT name FROM neighborhoods """)
        self.ui.cmb_neighborhood.addItems(get_list_general(data))

    def data_loader(self, p_item):
        info = list(self.connection.selector(f"""SELECT * FROM workplaces WHERE name="{p_item.text()}" """)[0])
        department_name = self.connection.find(f"""SELECT name FROM departments WHERE id = {info[3]} """)
        neigh_name = self.connection.find(f"""SELECT name FROM neighborhoods WHERE id = {info[5]} """)
        staff_name = ""
        if info[13] is not None:
            staff_name = " ".join(self.connection.selector(f"""SELECT name, surname FROM staffs WHERE id_number="{info[13]}" """)[0])
        self.ui.le_workplace_name.setText(info[1])
        self.ui.le_boss.setText(info[2])
        self.ui.cmb_department.setCurrentText(department_name)
        self.ui.le_master_instructive.setText(info[4])
        self.ui.le_coordinator.setText(staff_name)
        self.ui.cmb_neighborhood.setCurrentText(neigh_name)
        self.ui.le_street.setText(info[6])
        self.ui.le_number.setText(info[7])
        self.ui.le_phone1.setText(info[8])
        self.ui.le_phone2.setText(info[9])
        self.ui.le_email.setText(info[10])
        if info[11] == "E":
            self.ui.cb_request.setChecked(True)
        else:
            self.ui.cb_request.setChecked(False)

        self.old_wp_name = info[1]

    def closeEvent(self, event):
        self.connection.db_closer()


if __name__ == "__main__":
    app = QApplication([])
    window = WorkplaceWindow()
    window.show()
    sys.exit(app.exec())
