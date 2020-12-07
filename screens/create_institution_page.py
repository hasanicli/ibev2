from PyQt5.QtWidgets import QApplication, QWidget, QAction
import sys
from screens.add_institution_info_python import Ui_Form
from connectionDB import DbManager
from helper_function import *


class InstitutionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Kurum Bilgileri Ekle")
        self.connection = DbManager()
        self.staff_loader()
        self.data_loader()
        get_out = QAction("Quit", self)
        get_out.triggered.connect(self.closeEvent)
        self.ui.btn_save.clicked.connect(self.recorder)

    def recorder(self):
        li = [self.ui.le_city.text(), self.ui.le_county.text(), self.ui.le_school_name.text(), find_id_number(self.ui.cmb_school_manager.currentText()),
              find_id_number(self.ui.cmb_manager_asistant.currentText()), self.ui.le_phone1.text(), self.ui.le_phone2.text(), self.ui.le_email.text()]
        self.connection.deleter(f"""DELETE FROM school_info WHERE id = 1 """)
        self.connection.recorder(f"""INSERT INTO school_info VALUES(1, "{li[0]}", "{li[1]}", "{li[2]}", "{li[3]}", "{li[4]}", "{li[5]}", "{li[6]}", "{li[7]}")""")

    def staff_loader(self):
        self.ui.cmb_manager_asistant.clear()
        self.ui.cmb_school_manager.clear()
        data = self.connection.selector(f""" SELECT name, surname, id_number FROM staffs """)
        self.ui.cmb_school_manager.addItems(get_list_personal(data))
        self.ui.cmb_manager_asistant.addItems(get_list_personal(data))

    def data_loader(self):
        info_list = list(self.connection.selector(f""" SELECT city, county, name, managerID, coordinator_managerID, phone_number1,phone_number2, email FROM school_info WHERE id=1 """)[0])
        obj_list = [self.ui.le_city, self.ui.le_county, self.ui.le_school_name, self.ui.cmb_school_manager, self.ui.cmb_manager_asistant, self.ui.le_phone1, self.ui.le_phone2, self.ui.le_email]
        for number, obj in enumerate(obj_list):
            if obj.objectName().startswith("le"):
                obj.setText(info_list[number])
            elif obj.objectName().startswith("cmb"):
                person_name = ""
                for key, val in person_dict.items():
                    if info_list[number] == val[2]:
                        person_name = str(val[0]) + " " + str(val[1]) + " " + str(key)
                obj.setCurrentText(person_name)

    def closeEvent(self, event):
        self.connection.db_closer()


if __name__ == "__main__":
    app = QApplication([])
    window = InstitutionWindow()
    window.show()
    sys.exit(app.exec())
