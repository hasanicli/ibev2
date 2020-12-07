from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QAction, QInputDialog, QLineEdit
import sys
from screens.add_parent_class_python import Ui_Form
from connectionDB import DbManager
from control_page import *
from helper_function import *


class ParentClassWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Ortak Sınıf")
        self.connection = DbManager()
        locale.setlocale(locale.LC_COLLATE, ('tr_TR', 'UTF8'))
        self.ui.lw_parent_class.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.lw_parent_class.customContextMenuRequested.connect(self.right_click)
        self.ui.le_parent_class.returnPressed.connect(self.recorder)
        get_out = QAction("Quit", self)
        get_out.triggered.connect(self.closeEvent)
        self.parent_class_loader()
        self.ui.btn_save.clicked.connect(self.recorder)
        self.ui.btn_edit.clicked.connect(self.updater)
        self.ui.btn_delete.clicked.connect(self.deleter)

    def get_list_widgets_items(self):
        return [self.ui.lw_parent_class.item(index).text() for index in range(self.ui.lw_parent_class.count())]

    def recorder(self):
        lw_items = self.get_list_widgets_items()
        classroom = tr_upper(stripper(self.ui.le_parent_class.text()))
        if general_name_control(classroom, lw_items):
            self.connection.recorder(f"""INSERT INTO parent_classes(name) VALUES("{classroom}") """)
            self.parent_class_loader()
        focus_item(self.ui.le_parent_class)

    def updater(self):
        item = self.ui.lw_parent_class.currentItem()
        if item is not None:
            lw_items = self.get_list_widgets_items()
            old_parent = item.text()
            new_parent, ok_pressed = QInputDialog.getText(self, "Cevap ver", "Yeni Değer:", QLineEdit.Normal, old_parent)
            new_parent = tr_upper(stripper(new_parent))
            if ok_pressed and general_name_control(new_parent, lw_items):
                self.connection.updater(f"""UPDATE  parent_classes SET name = "{new_parent}" WHERE name="{old_parent}" """)
                self.parent_class_loader()
        else:
            message_box("Önce seçim yapmalısınız!")
        focus_item(self.ui.le_parent_class)

    def deleter(self):
        item = self.ui.lw_parent_class.currentItem()
        if item is not None:
            self.connection.deleter(f"""DELETE FROM parent_classes WHERE name = "{item.text()}" """)
            self.parent_class_loader()
        else:
            message_box("Önce seçim yapmalısınız!")
        focus_item(self.ui.le_parent_class)

    def parent_class_loader(self):
        self.ui.lw_parent_class.clear()
        data = self.connection.selector("SELECT name FROM parent_classes")
        self.ui.lw_parent_class.addItems(get_list_general(data))

    def right_click(self, event):
        right_click_function(self, event, self.ui.lw_parent_class)

    def closeEvent(self, event):
        self.connection.db_closer()


if __name__ == "__main__":
    app = QApplication([])
    window = ParentClassWindow()
    window.show()
    sys.exit(app.exec())
