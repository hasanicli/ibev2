from PyQt5.QtWidgets import QMessageBox
from mysql import connector
from mysql.connector import Error


class DbManager:
    def __init__(self):
        self.my_connection = connector.connect(host="localhost", user="root", password="Musa2015", database="ime")
        self.wizard = self.my_connection.cursor()

    @staticmethod
    def message_box(p_text):
        QMessageBox.warning(None, "Uyarı", "Bir hataya raslanıldı.\nProgram kapanacak.\n" + p_text)

    def recorder(self, p_text):
        try:
            self.wizard.execute(p_text)
            self.my_connection.commit()
        except Error as err:
            self.message_box(str(err.errno))

    def updater(self, p_text):
        try:
            self.wizard.execute(p_text)
            self.my_connection.commit()
        except Error as err:
            self.message_box(str(err))

    def deleter(self, p_text):
        try:
            self.wizard.execute(p_text)
            self.my_connection.commit()
        except Error as err:
            if err.errno == 1451:
                QMessageBox.warning(None, "UYARI !!!", "Bu kayıtla ilişkili kayıtlar var.\nKaydı silemezsiniz.\nSadece güncelleme yapabilirsiniz.")
            else:
                self.message_box(str(err.errno))

    def selector(self, p_text):
        try:
            self.wizard.execute(p_text)
            return self.wizard.fetchall()
        except Error as err:
            self.message_box(str(err))

    def find(self, p_text):
        try:
            self.wizard.execute(p_text)
            return self.wizard.fetchone()[0]
        except Error as err:
            self.message_box(str(err))

    def db_closer(self):
        self.my_connection.close()

    def connection_state(self):
        return self.my_connection.is_connected()
