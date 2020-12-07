from PyQt5.QtWidgets import QApplication, QWidget, QAction
import sys
from screens.add_class_to_parent_python import Ui_Form
from connectionDB import DbManager
from control_page import *


# Üst sınıfa aynı günlerdeki sınıflar katılabilir
class AddClassWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Üst sınıfa alt sınıf ekle")
        self.connection = DbManager()
        get_out = QAction("Quit", self)
        get_out.triggered.connect(self.closeEvent)
        self.parent_class_loader()
        self.free_classes_loader()
        self.assigned_classes_loader()
        self.ui.btn_add.clicked.connect(self.adding)
        self.ui.btn_sub.clicked.connect(self.subbing)
        self.ui.cmb_parent_class.currentTextChanged.connect(self.assigned_classes_loader)
        self.ui.cmb_parent_class.currentTextChanged.connect(self.free_classes_loader)
        self.ui.lw_all_class.doubleClicked.connect(self.adding)
        self.ui.lw_assigned_class.doubleClicked.connect(self.subbing)

    def adding(self):
        item = self.ui.lw_all_class.currentItem()
        if item is not None:
            parent_name = self.ui.cmb_parent_class.currentText()
            parent_id = self.connection.find(f"""SELECT id FROM parent_classes WHERE name = "{parent_name}" """)
            self.connection.recorder(f"""UPDATE classes SET parentID = {parent_id} WHERE name = "{item.text()}" """)
            self.free_classes_loader()
            self.assigned_classes_loader()
        else:
            message_box("Önce seçim yapmalısınız!")

    def subbing(self):
        item = self.ui.lw_assigned_class.currentItem()
        if item is not None:
            self.connection.recorder(f"""UPDATE classes SET parentID = NULL WHERE name = "{item.text()}" """)
            self.free_classes_loader()
            self.assigned_classes_loader()
        else:
            message_box("Önce seçim yapmalısınız!")

    def parent_class_loader(self):
        self.ui.cmb_parent_class.clear()
        data = [i[0] for i in self.connection.selector("SELECT name FROM parent_classes")]
        self.ui.cmb_parent_class.addItems(data)

    # Burada bir süzme işlemi yapılabilir.
    def free_classes_loader(self):
        self.ui.lw_all_class.clear()
        parent_name = self.ui.cmb_parent_class.currentText()
        if parent_name != "":
            data = [i[0] for i in self.connection.selector(f""" SELECT name FROM classes WHERE parentID IS NULL""")]
            self.ui.lw_all_class.addItems(data)

    def assigned_classes_loader(self):
        self.ui.lw_assigned_class.clear()
        parent_name = self.ui.cmb_parent_class.currentText()
        if parent_name != "":
            parent_id = self.connection.find(f"""SELECT id FROM parent_classes WHERE name = "{parent_name}" """)
            data = [i[0] for i in self.connection.selector(f""" SELECT name FROM classes WHERE parentID={parent_id}""")]
            self.ui.lw_assigned_class.addItems(data)

    def closeEvent(self, event):
        self.connection.db_closer()


if __name__ == "__main__":
    app = QApplication([])
    window = AddClassWindow()
    window.show()
    sys.exit(app.exec())
