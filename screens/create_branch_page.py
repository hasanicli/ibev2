from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QAction, QInputDialog, QLineEdit
import sys
from screens.add_branch_python import Ui_Form
from connectionDB import DbManager
from control_page import *
from helper_function import *


class BranchWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Dal Ekle")
        self.connection = DbManager()
        locale.setlocale(locale.LC_COLLATE, ('tr_TR', 'UTF8'))
        self.ui.lw_branch.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.lw_branch.customContextMenuRequested.connect(self.right_click)
        self.ui.le_branch.returnPressed.connect(self.recorder)
        get_out = QAction("Quit", self)
        get_out.triggered.connect(self.closeEvent)
        self.department_loader()
        self.branch_loader()
        self.ui.btn_save.clicked.connect(self.recorder)
        self.ui.btn_edit.clicked.connect(self.updater)
        self.ui.btn_delete.clicked.connect(self.deleter)
        self.ui.cmb_department.currentTextChanged.connect(self.branch_loader)

    def get_list_widgets_items(self):
        return [self.ui.lw_branch.item(index).text() for index in range(self.ui.lw_branch.count())]

    def recorder(self):
        lw_items = self.get_list_widgets_items()
        branch = tr_capitalize(stripper(self.ui.le_branch.text()))
        department = self.ui.cmb_department.currentText()
        if only_letter_control(branch, lw_items):
            department_id = self.connection.find(f"""SELECT id FROM departments WHERE name="{department}" """)
            self.connection.recorder(f"""INSERT INTO branches(name,departmentID) VALUES("{branch}", {department_id})""")
            self.branch_loader()
        focus_item(self.ui.le_branch)

    def updater(self,):
        obj = self.ui.lw_branch.currentItem()
        if obj is not None:
            lw_items = self.get_list_widgets_items()
            old_branch = obj.text()
            new_branch, ok_pressed = QInputDialog.getText(self, "Cevap ver", "Yeni Değer:", QLineEdit.Normal, old_branch)
            new_branch = tr_capitalize(stripper(new_branch))
            if ok_pressed and only_letter_control(new_branch, lw_items):
                self.connection.updater(f"""UPDATE branches SET name = "{new_branch}" WHERE name="{old_branch}" """)
                self.branch_loader()
        else:
            message_box("Önce seçim yapmalısınız!")
        focus_item(self.ui.le_branch)

    def deleter(self):
        obj = self.ui.lw_branch.currentItem()
        if obj is not None:
            self.connection.deleter(f"""DELETE FROM branches WHERE name = "{obj.text()}" """)
            self.branch_loader()
        else:
            message_box("Önce seçim yapmalısınız!")
        focus_item(self.ui.le_branch)

    def department_loader(self):
        self.ui.cmb_department.clear()
        data = self.connection.selector(f"""SELECT name FROM departments""")
        self.ui.cmb_department.addItems(get_list_general(data))

    def branch_loader(self):
        department_name = self.ui.cmb_department.currentText()
        if department_name != "":
            department_id = self.connection.find(f"""SELECT id FROM departments WHERE name="{department_name}" """)
            self.ui.lw_branch.clear()
            data = self.connection.selector(f"SELECT name FROM branches WHERE departmentID={department_id}")
            self.ui.lw_branch.addItems(get_list_general(data))

    def right_click(self, event):
        right_click_function(self, event, self.ui.lw_branch)

    def closeEvent(self, event):
        self.connection.db_closer()


if __name__ == "__main__":
    app = QApplication([])
    window = BranchWindow()
    window.show()
    sys.exit(app.exec())
