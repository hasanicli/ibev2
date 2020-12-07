# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Erhan/Desktop/Koordinator/ibeV1/screens/add_class.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(547, 263)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        Form.setStyleSheet("/*\n"
"* QSS Qt Stylesheets Collection.\n"
"* Created in 2013 by Khromathyon Software.\n"
"* QSS Theme: Visual Studio(R) 2012 Dark Theme.\n"
"* License: WTFPL\n"
"*/\n"
"QMainWindow {\n"
"  background-color:#2d2d30;\n"
"  color:#f1f1f1;\n"
"}\n"
"\n"
"\n"
"QMenuBar {\n"
"\n"
"  background-color:#2d2d30;\n"
"  text-transform: uppercase;\n"
"  color:#f1f1f1;\n"
"}\n"
"\n"
"QMenuBar::item:selected{\n"
"  background-color:#3e3e40;\n"
"}\n"
"\n"
"QMenu {\n"
"  border:0.5px solid #333337;\n"
"  color:#f1f1f1;\n"
"}\n"
"QMenu::item:selected {\n"
"  background-color:#2d2d30;\n"
"  border-color:#333337;\n"
"\n"
"}\n"
"\n"
"QMenu::item {\n"
"  background-color:#1b1b1c;\n"
"  border-color:#333337;\n"
"       padding: 2px 25px 2px 20px;\n"
"\n"
"}\n"
"\n"
"QMenu::separator{\n"
"  background-color:#333337;\n"
"  spacing:2px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"  background-color:#2d2d30;\n"
"  border: 1px solid transparent;\n"
"  color:#f1f1f1;\n"
"  padding:5px;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:hover{\n"
"  background-color:#1c97ea;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"  background-color:#007acc;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"  border-top: 2px solid #007acc;\n"
"  background-color:#2d2d30;\n"
"}\n"
"\n"
"QDockWidget {\n"
"    background: #2d2d30;\n"
"    color:#f1f1f1;\n"
"}\n"
"\n"
"QDockWidget::active {\n"
"  border: 1px solid #007acc;\n"
"}\n"
"\n"
"QDockWidget::title {\n"
"  color:#f1f1f1;\n"
"  background:#007acc;\n"
"}\n"
"\n"
"QComboBox {\n"
"  border-style:none;\n"
"  background-color:#333337;\n"
"  color:#b2b2b2;\n"
"  border-style:none;\n"
"}\n"
"\n"
"QComboBox:on {\n"
"  background-color:#3f3f46;\n"
"}\n"
"\n"
"QComboBox:down-arrow {\n"
"  border-style:none;\n"
"  border-left: 1px solid #007acc;\n"
"}\n"
"\n"
"QComboBox:drop-down {\n"
"  border-style:none;\n"
"}\n"
"\n"
"/*Needs fix*/\n"
"QScrollBar{\n"
"  background:#3e3e42;\n"
"  border-style:none;\n"
"}\n"
"\n"
"QScrollbar::horizontal{\n"
"     height: 15px;\n"
"     margin: 0px 20px 0 20px;\n"
"}\n"
"\n"
"QScrollBar:handle {\n"
"  border-style:none;\n"
"  background:#9d9d9d;\n"
"  margin: inherited;\n"
"\n"
"}\n"
"QPushButton {\n"
"  border-style:none;\n"
"  border-bottom:1px solid #007acc;\n"
"  color:#f1f1f1;\n"
"  background:#3e3e42;\n"
"  padding:5px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"  border: 1px solid #007acc;\n"
"  background:#3e3e42;\n"
"\n"
"}\n"
"\n"
"QToolButton {\n"
"  border-style:none;\n"
"  background:#2d2d30;\n"
"  color:#f1f1f1;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"  border: 1px solid #007acc;\n"
"  background:#3e3e42;\n"
"}\n"
"\n"
"QLabel {\n"
"  color:#f1f1f1;\n"
"}\n"
"\n"
"QLineEdit {\n"
"  border: 1px solid #3e3e42;\n"
"  background-color:#3f3f46;\n"
"  color:#b2b2b2;\n"
"  selection-background-color:#1c97ea;\n"
"\n"
"}\n"
"QLineEdit:selected {\n"
"  border-color:#007acc;\n"
"}\n"
"\n"
"\n"
"QToolBar {\n"
"  background:#2d2d30;\n"
"  border-style:none;\n"
"}\n"
"\n"
"QToolBox{\n"
"  background:#2d2d30;\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"  background:#2d2d30;\n"
"  color:#f1f1f1;\n"
"  border-style:none;\n"
"  border-bottom-style: solid;\n"
"  border-bottom: 2px solid #007acc;\n"
"}\n"
"\n"
"QToolBox::tab:selected {\n"
"  border:1px solid #007acc;\n"
"}\n"
"\n"
"QWidget{\n"
"  background:#2d2d30;\n"
"  color:#f1f1f1;\n"
"}\n"
"\n"
"QTreeView {\n"
"  background-color:#2d2d30;\n"
"  border-style:none;\n"
"}\n"
"\n"
"QTreeView::item:selected\n"
"{\n"
"  background:#007acc;\n"
"}\n"
"\n"
"QTreeView::item:selected!active {\n"
"  background: #3f3f46;\n"
"}\n"
"\n"
"QTreeView::item:selected {\n"
"  background: #3f3f46;\n"
"}\n"
"QListView {\n"
"  background-color:#252526;\n"
"  border-style:none;\n"
"\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.cmb_department = QtWidgets.QComboBox(Form)
        self.cmb_department.setMinimumSize(QtCore.QSize(200, 0))
        self.cmb_department.setObjectName("cmb_department")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cmb_department)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.le_class = QtWidgets.QLineEdit(Form)
        self.le_class.setObjectName("le_class")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_class)
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
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(10, 18, 71, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setEnabled(True)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 41, 71, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setEnabled(True)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 64, 71, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setEnabled(True)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 87, 71, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_5.setEnabled(True)
        self.checkBox_5.setGeometry(QtCore.QRect(10, 110, 71, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_6.setEnabled(True)
        self.checkBox_6.setGeometry(QtCore.QRect(10, 133, 71, 17))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_7.setEnabled(True)
        self.checkBox_7.setGeometry(QtCore.QRect(10, 156, 71, 17))
        self.checkBox_7.setObjectName("checkBox_7")
        self.btn_update = QtWidgets.QPushButton(self.groupBox)
        self.btn_update.setGeometry(QtCore.QRect(10, 210, 75, 23))
        self.btn_update.setObjectName("btn_update")
        self.horizontalLayout_2.addWidget(self.groupBox)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_2.addWidget(self.line_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.lw_class = QtWidgets.QListWidget(Form)
        self.lw_class.setObjectName("lw_class")
        self.verticalLayout_2.addWidget(self.lw_class)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.horizontalLayout_2.setStretch(0, 50)
        self.horizontalLayout_2.setStretch(3, 10)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Alan : "))
        self.label.setText(_translate("Form", "Sınıf : "))
        self.btn_save.setText(_translate("Form", "Kaydet"))
        self.btn_delete.setText(_translate("Form", "Sil"))
        self.btn_edit.setText(_translate("Form", "Düzenle"))
        self.groupBox.setTitle(_translate("Form", "İşletme Günleri"))
        self.checkBox.setText(_translate("Form", "Pazartesi"))
        self.checkBox_2.setText(_translate("Form", "Salı"))
        self.checkBox_3.setText(_translate("Form", "Çarşamba"))
        self.checkBox_4.setText(_translate("Form", "Perşembe"))
        self.checkBox_5.setText(_translate("Form", "Cuma"))
        self.checkBox_6.setText(_translate("Form", "Cumartesi"))
        self.checkBox_7.setText(_translate("Form", "Pazar"))
        self.btn_update.setText(_translate("Form", "Güncelle"))
        self.label_5.setText(_translate("Form", "Oluşturulmuş Sınıflar"))

