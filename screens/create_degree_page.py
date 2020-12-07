from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QAction, QInputDialog, QLineEdit
import sys
from screens.add_degree_python import Ui_Form
from connectionDB import DbManager
from control_page import *
from helper_function import *


class DegreeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Unvan Ekle")
        self.connection = DbManager()
        locale.setlocale(locale.LC_COLLATE, ('tr_TR', 'UTF8'))
        self.ui.lw_degree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.lw_degree.customContextMenuRequested.connect(self.right_click)
        self.ui.le_degree.returnPressed.connect(self.recorder)
        get_out = QAction("Quit", self)
        get_out.triggered.connect(self.closeEvent)
        self.degree_loader()
        self.ui.btn_save.clicked.connect(self.recorder)
        self.ui.btn_edit.clicked.connect(self.updater)
        self.ui.btn_delete.clicked.connect(self.deleter)

    def get_list_widgets_items(self):
        return [self.ui.lw_degree.item(index).text() for index in range(self.ui.lw_degree.count())]

    def recorder(self):
        lw_items = self.get_list_widgets_items()
        obj = tr_capitalize(stripper(self.ui.le_degree.text()))
        if general_name_control(obj, lw_items):
            self.connection.recorder(f"""INSERT INTO staff_degrees(name) VALUES("{obj}")""")
            self.degree_loader()
        focus_item(self.ui.le_degree)

    def updater(self):
        obj = self.ui.lw_degree.currentItem()
        if obj is not None:
            lw_items = self.get_list_widgets_items()
            old_degree = obj.text()
            new_degree, ok_pressed = QInputDialog.getText(self, "Cevap ver", "Yeni Değer:", QLineEdit.Normal, old_degree)
            new_degree = tr_capitalize(stripper(new_degree))
            if ok_pressed and general_name_control(new_degree, lw_items):
                self.connection.updater(f"""UPDATE  staff_degrees SET name = "{new_degree}" WHERE name="{old_degree}" """)
                self.degree_loader()
        else:
            message_box("Önce seçim yapmalısınız!")
        focus_item(self.ui.le_degree)

    def deleter(self):
        obj = self.ui.lw_degree.currentItem()
        if obj is not None:
            self.connection.deleter(f"""DELETE FROM staff_degrees WHERE name = "{obj.text()}" """)
            self.degree_loader()
        else:
            message_box("Önce seçim yapmalısınız!")
        focus_item(self.ui.le_degree)

    def degree_loader(self):
        self.ui.lw_degree.clear()
        data = self.connection.selector("SELECT name FROM staff_degrees")
        self.ui.lw_degree.addItems(get_list_general(data))

    def right_click(self, event):
        right_click_function(self, event, self.ui.lw_degree)

    def closeEvent(self, event):
        self.connection.db_closer()


if __name__ == "__main__":
    app = QApplication([])
    window = DegreeWindow()
    window.show()
    sys.exit(app.exec())
