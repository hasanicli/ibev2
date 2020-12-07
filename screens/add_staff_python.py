# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Erhan/Desktop/Koordinator/ibeV1/screens/add_staff.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(621, 231)
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
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0.00480769 rgba(3, 50, 76, 255),stop:0.293269 rgba(6, 82, 125, 255),stop:0.514423 rgba(8, 117, 178, 255),stop:0.745192 rgba(7, 108, 164, 255),stop:1 rgba(3, 51, 77, 255));\n"
"    color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(42, 95, 113, 255),stop:1 rgba(12, 53, 97, 255));\n"
"    color: #fff;\n"
"    border: 0px;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(167, 214, 50, 255),stop:1 rgba(98, 169, 67, 255));\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(147, 194, 30, 255),stop:1 rgba(78, 149, 47, 255));\n"
"    color: #fff;\n"
"    border: 0px;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"    background-color: #bfbfbf;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-color: #141414;\n"
"    border-radius: 5px;\n"
"    padding-left: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QListView-----*/\n"
"QListView{\n"
"    background-color: transparent;\n"
"    font-size: 12pt;\n"
"    border: none;\n"
"    color: #fff;\n"
"    show-decoration-selected: 0;\n"
"    padding-left: px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected{\n"
"    color: #fff;\n"
"    font-weight: bold;\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(147, 194, 30, 255),stop:1 rgba(78, 149, 47, 255));\n"
"       border: none;\n"
"       border-radius: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:!selected{\n"
"    color: #fff;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:!selected:hover{\n"
"    color: #fff;\n"
"    background-color: #0c3561;\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"    \n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:vertical \n"
"{\n"
"    border: none;\n"
"    width: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical \n"
"{\n"
"    border: none;\n"
"    border-radius : 0px;\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(167, 214, 50, 255),stop:1 rgba(98, 169, 67, 255));\n"
"    min-height: 50px;\n"
"    width : 16px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical:pressed\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(147, 194, 30, 255),stop:1 rgba(78, 149, 47, 255)); \n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    border: none;\n"
"    background: transparent;\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover \n"
"{\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:pressed \n"
"{\n"
"    background-color: #3f3f3f;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    border: none;\n"
"    background: transparent;\n"
"    height: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical:hover \n"
"{\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical:pressed \n"
"{\n"
"    background-color: #3f3f3f;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    background: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical \n"
"{\n"
"       width: 0px;\n"
"       height: 0px;\n"
"       background: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"       background-color: #0c2669;\n"
"    width: 11px;;\n"
"    \n"
"}\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.le_identity_number = QtWidgets.QLineEdit(Form)
        self.le_identity_number.setObjectName("le_identity_number")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_identity_number)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.le_name = QtWidgets.QLineEdit(Form)
        self.le_name.setObjectName("le_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_name)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.le_surname = QtWidgets.QLineEdit(Form)
        self.le_surname.setObjectName("le_surname")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.le_surname)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.cmb_staff_branch = QtWidgets.QComboBox(Form)
        self.cmb_staff_branch.setObjectName("cmb_staff_branch")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cmb_staff_branch)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.cmb_staff_degree = QtWidgets.QComboBox(Form)
        self.cmb_staff_degree.setObjectName("cmb_staff_degree")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cmb_staff_degree)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.le_phone_number = QtWidgets.QLineEdit(Form)
        self.le_phone_number.setObjectName("le_phone_number")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.le_phone_number)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.le_mail = QtWidgets.QLineEdit(Form)
        self.le_mail.setObjectName("le_mail")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.le_mail)
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
        self.btn_delete = QtWidgets.QPushButton(Form)
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout.addWidget(self.btn_delete)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.btn_edit = QtWidgets.QPushButton(Form)
        self.btn_edit.setObjectName("btn_edit")
        self.horizontalLayout.addWidget(self.btn_edit)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 73, 157))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setEnabled(True)
        self.checkBox.setCheckable(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_3.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_2.setEnabled(True)
        self.checkBox_2.setCheckable(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_3.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_3.setEnabled(True)
        self.checkBox_3.setCheckable(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_3.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_4.setEnabled(True)
        self.checkBox_4.setCheckable(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_3.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_5.setEnabled(True)
        self.checkBox_5.setCheckable(True)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_3.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_6.setEnabled(True)
        self.checkBox_6.setCheckable(True)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_3.addWidget(self.checkBox_6)
        self.checkBox_7 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_7.setEnabled(True)
        self.checkBox_7.setCheckable(True)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout_3.addWidget(self.checkBox_7)
        self.horizontalLayout_2.addWidget(self.groupBox)
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        spacerItem7 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem7)
        self.lw_staff = QtWidgets.QListWidget(Form)
        self.lw_staff.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lw_staff.setObjectName("lw_staff")
        self.verticalLayout.addWidget(self.lw_staff)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(0, 55)
        self.horizontalLayout_2.setStretch(4, 5)
        self.horizontalLayout_2.setStretch(6, 40)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "TC Kimlik No : "))
        self.label.setText(_translate("Form", "Adı : "))
        self.label_7.setText(_translate("Form", "Soyadı : "))
        self.label_2.setText(_translate("Form", "Branş : "))
        self.label_3.setText(_translate("Form", "Ünvan : "))
        self.label_6.setText(_translate("Form", "Telefon : "))
        self.label_8.setText(_translate("Form", "E-posta : "))
        self.btn_save.setText(_translate("Form", "Kaydet"))
        self.btn_delete.setText(_translate("Form", "Sil"))
        self.btn_edit.setText(_translate("Form", "Düzelt"))
        self.groupBox.setTitle(_translate("Form", "İşletme Günleri"))
        self.checkBox.setText(_translate("Form", "Pazartesi"))
        self.checkBox_2.setText(_translate("Form", "Salı"))
        self.checkBox_3.setText(_translate("Form", "Çarşamba"))
        self.checkBox_4.setText(_translate("Form", "Perşembe"))
        self.checkBox_5.setText(_translate("Form", "Cuma"))
        self.checkBox_6.setText(_translate("Form", "Cumartesi"))
        self.checkBox_7.setText(_translate("Form", "Pazar"))
        self.label_4.setText(_translate("Form", "Varolan Öğretmenler"))

