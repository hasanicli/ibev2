from datetime import datetime
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QWidget, QAction
import sys
from screens.add_disconnection_python import Ui_Form
from connectionDB import DbManager
from control_page import *
from helper_function import *


class DisconnectionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Unvan Ekle")
        self.connection = DbManager()
        self.date_loader()
        self.student_loader()
        self.cause_loader()
        focus_item(self.ui.le_document_number)
        locale.setlocale(locale.LC_COLLATE, ('tr_TR', 'UTF8'))
        get_out = QAction("Quit", self)
        get_out.triggered.connect(self.closeEvent)
        self.ui.btn_save.clicked.connect(self.recorder)

    def recorder(self):
        item = self.ui.lw_students.currentItem()
        if item is not None and self.ui.le_document_number.text() != "" and self.ui.cmb_cause.currentText() != "":
            student_id = find_id_number(item.text())
            disconnection_date = datetime.date(datetime(*QDate.getDate(self.ui.date_disconnection.date())))
            document_number = self.ui.le_document_number.text()
            cause_id = self.connection.find(f"""SELECT id FROM causes WHERE name = "{self.ui.cmb_cause.currentText()}" """)
            record_date = self.connection.find(f"""SELECT record_date FROM students WHERE id_number = "{student_id}" """)

            is_going = self.connection.find(f"""SELECT is_going FROM students WHERE id_number = "{student_id}" """)

            if is_going == "E":
                old_wp_id = self.connection.find(f""" SELECT workplaceID FROM history WHERE studentID="{student_id}" AND leaving_date IS NULL""")
                self.connection.updater(f"""UPDATE history SET leaving_date="{disconnection_date}" WHERE studentID="{student_id}" AND leaving_date IS NULL """)
                number_of_student_in_old_wp = self.connection.selector(f""" SELECT COUNT(studentID) FROM history  WHERE workplaceID = {old_wp_id} AND leaving_date IS NULL """)[0][0]
                if number_of_student_in_old_wp == 0:
                    self.connection.updater(f"""UPDATE workplaces SET staffID=NULL, dayID=NULL WHERE id={old_wp_id} """)
                    message_box("buraya bir mesaj gelse iyi olur")
            else:
                self.connection.deleter(f"""DELETE FROM temp_workplace WHERE studentID="{student_id}" """)
            self.connection.recorder(f"""INSERT INTO archive (studentID, starting_date, disconnection_date, disconnection_causeID, document_number)
                                                        VALUES("{student_id}", "{record_date}", "{disconnection_date}", {cause_id}, "{document_number}") """)
            self.connection.updater(f"""UPDATE students SET is_active="H", classID = NULL WHERE id_number="{student_id}" """)
            self.student_loader()
            focus_item(self.ui.le_document_number)
        else:
            message_box("Önce seçim yapmalı ve doküman numarası girmelisiniz.")

    def date_loader(self):
        self.ui.date_disconnection.setDate(datetime.date(datetime.now()))

    def student_loader(self):
        self.ui.lw_students.clear()
        data = self.connection.selector(f""" SELECT name, surname, id_number FROM students WHERE is_active="E" """)
        self.ui.lw_students.addItems(get_list_personal(data))

    def cause_loader(self):
        self.ui.cmb_cause.clear()
        data = [i[0] for i in self.connection.selector("SELECT name FROM causes")]
        self.ui.cmb_cause.addItems(data)

    def closeEvent(self, event):
        self.connection.db_closer()


if __name__ == "__main__":
    app = QApplication([])
    window = DisconnectionWindow()
    window.show()
    sys.exit(app.exec())
