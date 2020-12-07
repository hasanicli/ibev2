from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QAction, QInputDialog, QLineEdit
import sys
from screens.add_department_python import Ui_Form
from connectionDB import DbManager
from control_page import *
from helper_function import *


class DepartmentWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Alan Ekle")
        self.connection = DbManager()
        locale.setlocale(locale.LC_COLLATE, ('tr_TR', 'UTF8'))
        self.ui.lw_department.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.lw_department.customContextMenuRequested.connect(self.right_click)
        self.ui.le_department.returnPressed.connect(self.recorder)
        get_out = QAction("Quit", self)
        get_out.triggered.connect(self.closeEvent)
        self.department_loader()
        self.ui.btn_save.clicked.connect(self.recorder)
        self.ui.btn_edit.clicked.connect(self.updater)
        self.ui.btn_delete.clicked.connect(self.deleter)

    def get_list_widgets_items(self):
        return [self.ui.lw_department.item(index).text() for index in range(self.ui.lw_department.count())]

    def recorder(self):
        lw_items = self.get_list_widgets_items()
        department = tr_capitalize(stripper(self.ui.le_department.text()))
        if only_letter_control(department, lw_items):
            self.connection.recorder(f"""INSERT INTO departments(name) VALUES("{department}")""")
            self.department_loader()
        focus_item(self.ui.le_department)

    def updater(self):
        obj = self.ui.lw_department.currentItem()
        if obj is not None:
            lw_items = self.get_list_widgets_items()
            old_department = obj.text()
            new_department, ok_pressed = QInputDialog.getText(self, "Cevap ver", "Yeni Değer:", QLineEdit.Normal, old_department)
            new_department = tr_capitalize(stripper(new_department))
            if ok_pressed and only_letter_control(new_department, lw_items):
                self.connection.updater(f"""UPDATE departments SET name = "{new_department}" WHERE name="{old_department}" """)
                self.department_loader()
        else:
            message_box("Önce seçim yapmalısınız!")
        focus_item(self.ui.le_department)

    def deleter(self):
        obj = self.ui.lw_department.currentItem()
        if obj is not None:
            self.connection.deleter(f"""DELETE FROM departments WHERE name = "{obj.text()}" """)
            self.department_loader()
        else:
            message_box("Önce seçim yapmalısınız!")
        focus_item(self.ui.le_department)

    def department_loader(self):
        self.ui.lw_department.clear()
        data = self.connection.selector("SELECT name FROM departments")
        self.ui.lw_department.addItems(get_list_general(data))

    def right_click(self, event):
        right_click_function(self, event, self.ui.lw_department)

    def closeEvent(self, event):
        self.connection.db_closer()
        print(self.connection.connection_state())


if __name__ == "__main__":
    app = QApplication([])
    window = DepartmentWindow()
    window.show()
    sys.exit(app.exec())
