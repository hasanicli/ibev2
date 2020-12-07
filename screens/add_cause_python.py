# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Erhan/Desktop/Koordinator/ibeV1/screens/add_cause.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(540, 211)
        font = QtGui.QFont()
        font.setPointSize(11)
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
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(24, 25, 29, 255),stop:1 rgba(42, 44, 51, 255));\n"
"    color: #eee;\n"
"    border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #ffffff;\n"
"\n"
"}\n"
"\n"
"\n"
"QLabel::disabled\n"
"{\n"
"    background-color: transparent;\n"
"    color: gray;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenuBar-----*/\n"
"QMenuBar\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 51, 255), stop:1 rgba(24, 25, 29, 255));\n"
"    color: #eee;\n"
"    border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"    \n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 51, 255), stop:1 rgba(24, 25, 29, 255));\n"
"    color: #eee;\n"
"    border-color: #000000;\n"
"    \n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:disabled\n"
"{\n"
"    background-color: transparent;\n"
"    color: gray;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(171, 129, 102, 255),stop:1 rgba(140, 107, 85, 255));\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(121, 79, 52, 255),stop:1 rgba(90, 57, 35, 255));\n"
"    border: 1px solid #794f34;\n"
"    margin-bottom: -1px;\n"
"    padding-bottom: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenu-----*/\n"
"QMenu\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(24, 25, 29, 255),stop:1 rgba(42, 44, 51, 255));\n"
"    border: 1px solid;\n"
"    color: #eee;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 1px;\n"
"    background-color: #000;\n"
"    color: #ffffff;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item\n"
"{\n"
"    min-width : 150px;\n"
"    padding: 3px 20px 3px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(121, 79, 52, 255),stop:1 rgba(90, 57, 35, 255));\n"
"    color: #ffffff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:disabled\n"
"{\n"
"    color: #262626;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(151, 109, 82, 255),stop:1 rgba(120, 87, 65, 255));\n"
"    color: #000000;\n"
"    border-color: #000000;\n"
"    border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(171, 129, 102, 255),stop:1 rgba(140, 107, 85, 255));\n"
"    color: #000000;\n"
"    border-color: #000000;\n"
"    border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(121, 79, 52, 255),stop:1 rgba(90, 57, 35, 255));\n"
"    color: #000000;\n"
"    border-color: #000000;\n"
"    border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::checked\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(121, 79, 52, 255),stop:1 rgba(90, 57, 35, 255));\n"
"    color: #000000;\n"
"    border-color: #000000;\n"
"    border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QSlider-----*/\n"
"QSlider{\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::groove:horizontal \n"
"{\n"
"    background-color: transparent;\n"
"    height: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal \n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(121, 79, 52, 255),stop:1 rgba(90, 57, 35, 255));\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal \n"
"{\n"
"    background-color: #666765;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal \n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(151, 109, 82, 255),stop:1 rgba(120, 87, 65, 255));\n"
"    width: 14px;\n"
"    margin: -5px;\n"
"    border-radius: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal:hover \n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(121, 79, 52, 255),stop:1 rgba(90, 57, 35, 255));\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal:disabled \n"
"{\n"
"    background-color: #bbb;\n"
"    border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal:disabled \n"
"{\n"
"    background-color: #eee;\n"
"    border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal:disabled \n"
"{\n"
"    background-color: #eee;\n"
"    border: 1px solid #aaa;\n"
"    border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QStatusBar-----*/\n"
"QStatusBar\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 51, 255), stop:1 rgba(24, 25, 29, 255));\n"
"    color: #eee;\n"
"    border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.le_cause = QtWidgets.QLineEdit(Form)
        self.le_cause.setObjectName("le_cause")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_cause)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_save = QtWidgets.QPushButton(Form)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        self.btn_delete = QtWidgets.QPushButton(Form)
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout.addWidget(self.btn_delete)
        self.btn_edit = QtWidgets.QPushButton(Form)
        self.btn_edit.setObjectName("btn_edit")
        self.horizontalLayout.addWidget(self.btn_edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.lw_cause = QtWidgets.QListWidget(Form)
        self.lw_cause.setObjectName("lw_cause")
        self.verticalLayout_2.addWidget(self.lw_cause)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.setStretch(0, 60)
        self.horizontalLayout_2.setStretch(2, 40)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Ayrılma Sebebi : "))
        self.btn_save.setText(_translate("Form", "Kaydet"))
        self.btn_delete.setText(_translate("Form", "Sil"))
        self.btn_edit.setText(_translate("Form", "Düzenle"))
        self.label_5.setText(_translate("Form", "Sebepler"))

