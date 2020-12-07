from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMessageBox, QMenu


def message_box(p_text):
    QMessageBox.warning(None, "UYARI !!!", p_text)


def right_click_function(self, event, p_object):
    self.contextMenu = QMenu(self)
    delete_act = self.contextMenu.addAction("Sil")
    edit_act = self.contextMenu.addAction("Düzenle")
    quit_act = self.contextMenu.addAction("Çıkış")
    index = p_object.indexAt(event)
    if not index.isValid():
        return
    self.contextMenu.popup(QCursor.pos())
    action = self.contextMenu.exec()
    if action == delete_act:
        self.deleter()
    if action == edit_act:
        self.updater()
    if action == quit_act:
        self.close()


def is_name(p_text):
    letters = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p",
               "r", "s", "ş", "t", "u", "ü", "v", "y", "z", " ", "A", "B", "C", "Ç", "D", "E", "F", "G", "Ğ", "H",
               "I", "İ", "J", "K", "L", "M", "N", "O", "Ö", "P", "R", "S", "Ş", "T", "U, ""Ü", "V", "Y", "Z", "."]
    for letter in p_text:
        if letter not in letters:
            return False
    return True


def is_surname(p_text):
    letters = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p",
               "r", "s", "ş", "t", "u", "ü", "v", "y", "z", "A", "B", "C", "Ç", "D", "E", "F", "G", "Ğ", "H",
               "I", "İ", "J", "K", "L", "M", "N", "O", "Ö", "P", "R", "S", "Ş", "T", "U, ""Ü", "V", "Y", "Z"]
    for letter in p_text:
        if letter not in letters:
            return False
    return True


def is_number(p_text):
    letters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for letter in p_text:
        if letter not in letters:
            return False
    return True


def is_only_letter(p_text):
    letters = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p",
               "r", "s", "ş", "t", "u", "ü", "v", "y", "z", " ", "A", "B", "C", "Ç", "D", "E", "F", "G", "Ğ", "H",
               "I", "İ", "J", "K", "L", "M", "N", "O", "Ö", "P", "R", "S", "Ş", "T", "U", "Ü", "V", "Y", "Z"]
    for letter in p_text:
        if letter not in letters:
            return False
    return True


def name_control(p_text):
    if p_text == "":
        message_box("İsim alanı boş geçilemez!")
        return False
    elif not is_name(p_text):
        message_box("İsim alanı içerisinde sadece harf ve boşluk olabilir!")
        return False
    return True


def surname_control(p_text):
    if p_text == "":
        message_box("Soyadı alanı boş geçilemez!")
        return False
    elif not is_surname(p_text):
        message_box("Soyadı alanı içerisinde sadece harf olabilir!")
        return False
    return True


def identity_number_control(p_text, p_list):
    if not is_number(p_text):
        message_box("TC Kimlik no alanına sadece rakam girebilirsiniz!")
        return False
    elif len(p_text) != 11:
        message_box("11 Karakterden oluşan TC Kimlik no girmelisiniz!")
        return False
    elif p_text in p_list:
        message_box("Girdiğiniz veri daha önce kaydedilmiş!")
        return False
    return True


def archive_identity_number_control(p_text, p_list):
    if p_text in p_list:
        message_box("Bu kayıt arşivde var.\nBu TC Kimlik no ile kayıt yapamazsınız.\nSadece güncelleme ile arşivden çağırabilirsiz.")
        return False
    return True


def number_control(p_text):
    if len(p_text) < 1:
        message_box("Okul no alanı boş geçilemez!")
        return False
    elif not is_number(p_text):
        message_box("Okul no alanına sadece rakam girilebilir!")
        return False
    return True


def only_letter_control(p_text, p_list):
    if p_text == "":
        message_box("Sadece boşluktan oluşan bir giriş yapamazsınız!")
        return False
    elif not is_only_letter(p_text):
        message_box("Girdiğiniz veri içerisinde sadece harf olabilir!")
        return False
    elif p_text in p_list:
        message_box("Girdiğiniz veri daha önce kaydedilmiş!")
        return False
    return True


def general_name_control(p_text, p_list):
    if p_text == "":
        message_box("İsim alanı boşluktan oluşamaz!")
        return False
    elif p_text in p_list:
        message_box("Girdiğiniz isim daha önce kaydedilmiş!")
        return False
    return True
