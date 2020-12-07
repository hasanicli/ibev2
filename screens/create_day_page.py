from PyQt5.QtWidgets import QApplication, QWidget, QAction
import sys
from screens.add_day_python import Ui_Form
from connectionDB import DbManager


class DayWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Günler")

        self.connection = DbManager()
        print(self.connection.connection_state())

        get_out = QAction("Quit", self)
        get_out.triggered.connect(self.closeEvent)
        self.day_loader()

    def day_loader(self):
        self.ui.lw_day.clear()
        recorded_item = [item[0] for item in self.connection.selector("SELECT (name) FROM days ORDER BY id")]
        self.ui.lw_day.addItems(recorded_item)

    def closeEvent(self, event):
        self.connection.db_closer()
        print(self.connection.connection_state())


if __name__ == "__main__":
    app = QApplication([])
    window = DayWindow()
    window.show()
    sys.exit(app.exec())
