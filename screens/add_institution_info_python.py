# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Erhan/Desktop/Koordinator/ibeV1/screens/add_institution_info.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(472, 289)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        Form.setStyleSheet("/*Copyright (c) DevSec Studio. All rights reserved.\n"
"\n"
"MIT License\n"
"\n"
"Permission is hereby granted, free of charge, to any person obtaining a copy\n"
"of this software and associated documentation files (the \"Software\"), to deal\n"
"in the Software without restriction, including without limitation the rights\n"
"to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
"copies of the Software, and to permit persons to whom the Software is\n"
"furnished to do so, subject to the following conditions:\n"
"\n"
"The above copyright notice and this permission notice shall be included in all\n"
"copies or substantial portions of the Software.\n"
"\n"
"THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
"IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
"FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
"AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
"LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
"OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n"
"*/\n"
"\n"
"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"    background-color: #232430;\n"
"    color: #000000;\n"
"    border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: #232430;\n"
"    color: #c1c1c1;\n"
"    border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"    background-color: #ff9c2b;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    border-style: solid;\n"
"    border-color: #000000;\n"
"    padding: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    background-color: #ffaf5d;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: #dd872f;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton\n"
"{\n"
"    background-color: #ff9c2b;\n"
"    color: #000000;\n"
"    font-weight: bold;\n"
"    border-style: solid;\n"
"    border-color: #000000;\n"
"    padding: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::hover\n"
"{\n"
"    background-color: #ffaf5d;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::pressed\n"
"{\n"
"    background-color: #dd872f;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"    background-color: #38394e;\n"
"    color: #c1c1c1;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: #4a4c68;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTableView-----*/\n"
"QTableView, \n"
"QHeaderView, \n"
"QTableView::item \n"
"{\n"
"    background-color: #232430;\n"
"    color: #c1c1c1;\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected \n"
"{ \n"
"    background-color: #41424e;\n"
"    color: #c1c1c1;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:horizontal \n"
"{\n"
"    background-color: #232430;\n"
"    border: 1px solid #37384d;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::indicator{\n"
"    background-color: #1d1d28;\n"
"    border: 1px solid #37384d;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::indicator:checked{\n"
"    image:url(\"./ressources/check.png\"); /*To replace*/\n"
"    background-color: #1d1d28;\n"
"\n"
"}\n"
"\n"
"/*-----QTabWidget-----*/\n"
"QTabWidget::pane \n"
"{ \n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabWidget::tab-bar \n"
"{\n"
"    left: 5px; \n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab \n"
"{\n"
"    color: #c1c1c1;\n"
"    min-width: 1px;\n"
"    padding-left: 25px;\n"
"    margin-left:-22px;\n"
"    height: 28px;\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected \n"
"{\n"
"    color: #c1c1c1;\n"
"    font-weight: bold;\n"
"    height: 28px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!first \n"
"{\n"
"    margin-left: -20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:hover \n"
"{\n"
"    color: #DDD;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal \n"
"{\n"
"    background-color: transparent;\n"
"    height: 8px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal \n"
"{\n"
"    border: none;\n"
"    min-width: 100px;\n"
"    background-color: #56576c;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal, \n"
"QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-page:horizontal, \n"
"QScrollBar::sub-page:horizontal \n"
"{\n"
"    width: 0px;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical \n"
"{\n"
"    background-color: transparent;\n"
"    width: 8px;\n"
"    margin: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical \n"
"{\n"
"    border: none;\n"
"    min-height: 100px;\n"
"    background-color: #56576c;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical, \n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-page:vertical, \n"
"QScrollBar::sub-page:vertical \n"
"{\n"
"    height: 0px;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.le_city = QtWidgets.QLineEdit(Form)
        self.le_city.setObjectName("le_city")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_city)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.le_county = QtWidgets.QLineEdit(Form)
        self.le_county.setObjectName("le_county")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_county)
        self.le_school_name = QtWidgets.QLineEdit(Form)
        self.le_school_name.setObjectName("le_school_name")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.le_school_name)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.cmb_school_manager = QtWidgets.QComboBox(Form)
        self.cmb_school_manager.setObjectName("cmb_school_manager")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cmb_school_manager)
        self.cmb_manager_asistant = QtWidgets.QComboBox(Form)
        self.cmb_manager_asistant.setObjectName("cmb_manager_asistant")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cmb_manager_asistant)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.le_phone1 = QtWidgets.QLineEdit(Form)
        self.le_phone1.setObjectName("le_phone1")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.le_phone1)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.le_phone2 = QtWidgets.QLineEdit(Form)
        self.le_phone2.setObjectName("le_phone2")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.le_phone2)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.le_email = QtWidgets.QLineEdit(Form)
        self.le_email.setObjectName("le_email")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.le_email)
        self.verticalLayout_2.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_save = QtWidgets.QPushButton(Form)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.horizontalLayout.setStretch(0, 10)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "İl :"))
        self.label_2.setText(_translate("Form", "İlçe : "))
        self.label_3.setText(_translate("Form", "Okul Adı : "))
        self.label_5.setText(_translate("Form", "Okul Müdürü : "))
        self.label_6.setText(_translate("Form", "Koodinatör Md. Yrd. : "))
        self.label_4.setText(_translate("Form", "Telefon1 : "))
        self.label_7.setText(_translate("Form", "Telefon2 : "))
        self.label_8.setText(_translate("Form", "E-Posta : "))
        self.btn_save.setText(_translate("Form", "Kaydet"))

