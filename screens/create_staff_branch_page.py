from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QAction, QInputDialog, QLineEdit
import sys
from screens.add_staff_branch_python import Ui_Form
from connectionDB import DbManager
from control_page import *
from helper_function import *


class StaffBranchWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Öğretmen Branş Ekle")
        self.connection = DbManager()
        locale.setlocale(locale.LC_COLLATE, ('tr_TR', 'UTF8'))
        self.ui.lw_staff_branch.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.lw_staff_branch.customContextMenuRequested.connect(self.right_click)
        self.ui.le_staff_branch.returnPressed.connect(self.recorder)
        get_out = QAction("Quit", self)
        get_out.triggered.connect(self.closeEvent)
        self.staff_branch_loader()
        self.ui.btn_save.clicked.connect(self.recorder)
        self.ui.btn_edit.clicked.connect(self.updater)
        self.ui.btn_delete.clicked.connect(self.deleter)

    def get_list_widgets_items(self):
        return [self.ui.lw_staff_branch.item(index).text() for index in range(self.ui.lw_staff_branch.count())]

    def recorder(self):
        lw_items = self.get_list_widgets_items()
        staff_branch = tr_capitalize(stripper(self.ui.le_staff_branch.text()))
        if only_letter_control(staff_branch, lw_items):
            self.connection.recorder(f"""INSERT INTO staff_branches(name) VALUES("{staff_branch}")""")
            self.staff_branch_loader()
        focus_item(self.ui.le_staff_branch)

    def updater(self):
        item = self.ui.lw_staff_branch.currentItem()
        if item is not None:
            lw_items = self.get_list_widgets_items()
            old_staff_branches = item.text()
            new_staff_branches, ok_pressed = QInputDialog.getText(self, "Cevap ver", "Yeni Değer:", QLineEdit.Normal, old_staff_branches)
            new_staff_branches = tr_capitalize(stripper(new_staff_branches))
            if ok_pressed and only_letter_control(new_staff_branches, lw_items):
                self.connection.updater(f"""UPDATE  staff_branches SET name = "{new_staff_branches}" WHERE name="{old_staff_branches}" """)
                self.staff_branch_loader()
        else:
            message_box("Önce seçim yapmalısınız!")
        focus_item(self.ui.le_staff_branch)

    def deleter(self):
        item = self.ui.lw_staff_branch.currentItem()
        if item is not None:
            delete_item = item.text()
            self.connection.deleter(f"""DELETE FROM staff_branches WHERE name = "{delete_item}" """)
            self.staff_branch_loader()
        else:
            message_box("Önce seçim yapmalısınız!")
        focus_item(self.ui.le_staff_branch)

    def staff_branch_loader(self):
        self.ui.lw_staff_branch.clear()
        data = self.connection.selector("SELECT name FROM staff_branches")
        self.ui.lw_staff_branch.addItems(get_list_general(data))

    def right_click(self, event):
        right_click_function(self, event, self.ui.lw_staff_branch)

    def closeEvent(self, event):
        self.connection.db_closer()
        print(self.connection.connection_state())


if __name__ == "__main__":
    app = QApplication([])
    window = StaffBranchWindow()
    window.show()
    sys.exit(app.exec())
