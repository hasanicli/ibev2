from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QAction, QInputDialog, QLineEdit
import sys
from screens.add_cause_python import Ui_Form
from connectionDB import DbManager
from control_page import *
from helper_function import *


class CauseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Ayrılma Sebebi Ekle")
        self.connection = DbManager()
        locale.setlocale(locale.LC_COLLATE, ('tr_TR', 'UTF8'))
        self.ui.lw_cause.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.lw_cause.customContextMenuRequested.connect(self.right_click)
        self.ui.le_cause.returnPressed.connect(self.recorder)
        get_out = QAction("Quit", self)
        get_out.triggered.connect(self.closeEvent)
        self.cause_loader()
        self.ui.btn_save.clicked.connect(self.recorder)
        self.ui.btn_edit.clicked.connect(self.updater)
        self.ui.btn_delete.clicked.connect(self.deleter)

    def get_list_widgets_items(self):
        return [self.ui.lw_cause.item(index).text() for index in range(self.ui.lw_cause.count())]

    def recorder(self):
        lw_items = self.get_list_widgets_items()
        cause_name = tr_capitalize(stripper(self.ui.le_cause.text()))
        if only_letter_control(cause_name, lw_items):
            self.connection.recorder(f"""INSERT INTO causes(name) VALUES("{cause_name}") """)
            self.cause_loader()
        focus_item(self.ui.le_cause)

    def updater(self):
        item = self.ui.lw_cause.currentItem()
        if item is not None:
            lw_items = self.get_list_widgets_items()
            old_cause = item.text()
            new_cause, ok_pressed = QInputDialog.getText(self, "Cevap ver", "Yeni Değer:", QLineEdit.Normal, old_cause)
            new_cause = tr_capitalize(stripper(new_cause))
            if ok_pressed and only_letter_control(new_cause, lw_items):
                self.connection.updater(f"""UPDATE causes SET name = "{new_cause}" WHERE name="{old_cause}" """)
                self.cause_loader()
        else:
            message_box("Önce seçim yapmalısınız!")
        focus_item(self.ui.le_cause)

    def deleter(self):
        item = self.ui.lw_cause.currentItem()
        if item is not None:
            self.connection.deleter(f"""DELETE FROM causes WHERE name = "{item.text()}" """)
            self.cause_loader()
        else:
            message_box("Önce seçim yapmalısınız!")
        focus_item(self.ui.le_cause)

    def cause_loader(self):
        self.ui.lw_cause.clear()
        data = self.connection.selector(f"""SELECT name FROM causes""")
        self.ui.lw_cause.addItems(get_list_general(data))

    def right_click(self, event):
        right_click_function(self, event, self.ui.lw_cause)

    def closeEvent(self, event):
        self.connection.db_closer()


if __name__ == "__main__":
    app = QApplication([])
    window = CauseWindow()
    window.show()
    sys.exit(app.exec())
