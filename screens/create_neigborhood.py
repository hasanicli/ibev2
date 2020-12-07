from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QAction, QInputDialog, QLineEdit
import sys
from screens.add_neighborhood_python import Ui_Form
from connectionDB import DbManager
from control_page import *
from helper_function import *


class NeighborhoodWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Mahalle / Semt")
        self.connection = DbManager()
        locale.setlocale(locale.LC_COLLATE, ('tr_TR', 'UTF8'))
        self.ui.lw_neighborhood.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.lw_neighborhood.customContextMenuRequested.connect(self.right_click)
        self.ui.le_neighborhood.returnPressed.connect(self.recorder)
        get_out = QAction("Quit", self)
        get_out.triggered.connect(self.closeEvent)
        self.neighborhood_loader()
        self.ui.btn_save.clicked.connect(self.recorder)
        self.ui.btn_edit.clicked.connect(self.updater)
        self.ui.btn_delete.clicked.connect(self.deleter)

    def get_list_widgets_items(self):
        return [self.ui.lw_neighborhood.item(index).text() for index in range(self.ui.lw_neighborhood.count())]

    def recorder(self):
        lw_items = self.get_list_widgets_items()
        neighborhood = tr_capitalize(stripper(self.ui.le_neighborhood.text()))
        if general_name_control(neighborhood, lw_items):
            self.connection.recorder(f"""INSERT INTO neighborhoods(name) VALUES("{neighborhood}")""")
            self.neighborhood_loader()
        focus_item(self.ui.le_neighborhood)

    def updater(self):
        item = self.ui.lw_neighborhood.currentItem()
        if item is not None:
            lw_items = self.get_list_widgets_items()
            old_neighborhood = item.text()
            new_neighborhood, ok_pressed = QInputDialog.getText(self, "Cevap ver", "Yeni Değer:", QLineEdit.Normal, old_neighborhood)
            new_neighborhood = tr_capitalize(stripper(new_neighborhood))
            if ok_pressed and general_name_control(new_neighborhood, lw_items):
                self.connection.updater(f"""UPDATE neighborhoods SET name = "{new_neighborhood}" WHERE name="{old_neighborhood}" """)
                self.neighborhood_loader()
        else:
            message_box("Önce seçim yapmalısınız!")
        focus_item(self.ui.le_neighborhood)

    def deleter(self):
        item = self.ui.lw_neighborhood.currentItem()
        if item is not None:
            self.connection.deleter(f"""DELETE FROM neighborhoods WHERE name = "{item.text()}" """)
            self.neighborhood_loader()
        else:
            message_box("Önce seçim yapmalısınız!")
        focus_item(self.ui.le_neighborhood)

    def neighborhood_loader(self):
        self.ui.lw_neighborhood.clear()
        data = self.connection.selector("SELECT name FROM neighborhoods")
        self.ui.lw_neighborhood.addItems(get_list_general(data))

    def right_click(self, event):
        right_click_function(self, event, self.ui.lw_neighborhood)

    def closeEvent(self, event):
        self.connection.db_closer()
        print(self.connection.connection_state())


if __name__ == "__main__":
    app = QApplication([])
    window = NeighborhoodWindow()
    window.show()
    sys.exit(app.exec())
