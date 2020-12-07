# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Erhan/Desktop/Koordinator/ibeV1/screens/add_workplace_to_staff.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1162, 658)
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
"    background-color: #8f1e28;\n"
"    color: #fff;\n"
"    selection-background-color: #aa7e82;\n"
"    selection-color: #000;\n"
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
"/*-----QMenuBar-----*/\n"
"QMenuBar \n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(70, 70, 70, 255),stop:1 rgba(3, 2, 5, 255));\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item \n"
"{\n"
"    background-color: transparent;\n"
"    border-left: 1px solid gray;\n"
"    padding: 5px;\n"
"    padding-left: 15px;\n"
"    padding-right: 15px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:selected \n"
"{\n"
"    background-color: #af272e;\n"
"    border: 1px solid #8f1e28;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:pressed \n"
"{\n"
"    background-color: #6e181c;\n"
"    border: 1px solid #6e181c;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenu-----*/\n"
"QMenu\n"
"{\n"
"    background-color: #e8d9d7;\n"
"    border: 1px solid #4a5157;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item\n"
"{\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"    min-width: 100px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"       background-color: #6e181c;\n"
"    height: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:disabled\n"
"{\n"
"    color: #555;\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    background-color: #ab7f83;\n"
"    border: 1px solid #ab7f83;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"    background-color: #6384ff;\n"
"    color: #fff;\n"
"    border: none;\n"
"    min-width: 80px;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::flat\n"
"{\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"    background-color: #606060;\n"
"    color: #959595;\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    background-color: #718fff;\n"
"    border: 1px solid #718fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: #446cff;\n"
"    border: 1px solid #446cff;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::checked\n"
"{\n"
"    background-color: #3761ff;\n"
"    border: 1px solid #3761ff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"    background-color: #e8d9d7;\n"
"    color : #000;\n"
"    border: 1px solid #1d1d1d;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPlainTExtEdit-----*/\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #e8d9d7;\n"
"    color : #000;\n"
"    border: 1px solid #1d1d1d;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolBox-----*/\n"
"QToolBox\n"
"{\n"
"    background-color: transparent;\n"
"    border: 1px solid #410d12;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolBox::tab\n"
"{\n"
"    background-color: #640000;\n"
"    border: 1px solid #640000;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolBox::tab:hover\n"
"{\n"
"    background-color: #640000;\n"
"    border: 1px solid #1d1d1d;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QComboBox-----*/\n"
"QComboBox\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(70, 70, 70, 255),stop:1 rgba(3, 2, 5, 255));\n"
"    padding-left: 6px;\n"
"    border: 1px solid #1d1d1d;\n"
"    color: #fff;\n"
"    height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #4a5157;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #e8d9d7;\n"
"    color: #000;\n"
"    selection-background-color: #aa7e82;\n"
"    selection-color: #fff;\n"
"    outline: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    background-color: #4a5157;\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QDoubleSpinBox & QCalendarWidget-----*/\n"
"QDoubleSpinBox,\n"
"QCalendarWidget QSpinBox \n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(70, 70, 70, 255),stop:1 rgba(3, 2, 5, 255));\n"
"    color : #fff;\n"
"    border: 1px solid #1d1d1d;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::up-button, \n"
"QCalendarWidget QSpinBox::up-button\n"
"{\n"
"    background-color: #4a5157;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"    border-color: #1d1d1d;\n"
"\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::up-button:hover, \n"
"QCalendarWidget QSpinBox::up-button:hover\n"
"{\n"
"    background-color: #585858;\n"
"\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::up-button:pressed, \n"
"QCalendarWidget QSpinBox::up-button:pressed\n"
"{\n"
"    background-color: #252525;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::up-arrow,\n"
"QCalendarWidget QSpinBox::up-arrow\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 7px;\n"
"    height: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::down-button, \n"
"QCalendarWidget QSpinBox::down-button\n"
"{\n"
"    background-color: #4a5157;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"    border-color: #1d1d1d;\n"
"\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::down-button:hover, \n"
"QCalendarWidget QSpinBox::down-button:hover\n"
"{\n"
"    background-color: #585858;\n"
"\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::down-button:pressed, \n"
"QCalendarWidget QSpinBox::down-button:pressed\n"
"{\n"
"    background-color: #252525;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QDoubleSpinBox::down-arrow,\n"
"QCalendarWidget QSpinBox::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 7px;\n"
"    height: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QGroupBox-----*/\n"
"QGroupBox \n"
"{\n"
"    background-color: #640000;\n"
"    border: 1px solid;\n"
"    border-color: #410d12;\n"
"    margin-top: 23px;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox::title  \n"
"{\n"
"    background-color: #640000;\n"
"    color: #fff;\n"
"    subcontrol-position: top left;\n"
"    subcontrol-origin: margin;\n"
"    padding: 5px;\n"
"    min-width: 100px;\n"
"    border: 1px solid #410d12;\n"
"    border-bottom: none;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QHeaderView-----*/\n"
"QHeaderView::section\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(70, 70, 70, 255),stop:1 rgba(3, 2, 5, 255));\n"
"    border-top: 0px solid gray;\n"
"    border-bottom: 0px solid gray;\n"
"    border-right: 1px solid gray;\n"
"    border-left: 0px solid gray;\n"
"    color: #fff;\n"
"    padding: 4px;\n"
"    \n"
"}\n"
"\n"
"\n"
"QHeaderView::section:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-left: 1px solid #003333;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-left: 1px solid #003333;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #003333;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: 1px solid #003333;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCalendarWidget-----*/\n"
"QCalendarWidget QMenu \n"
"{\n"
"    width: 100px;\n"
"    left: 20px;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QCalendarWidget QWidget \n"
"{ \n"
"    alternate-background-color: #1d1d1d; \n"
"    border: 1px solid #410d12;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled \n"
"{\n"
"    color: #fff;  \n"
"    background-color: #1d1d1d;\n"
"    selection-background-color: #8f1e28; \n"
"    selection-color: #fff; \n"
"\n"
"}\n"
"\n"
"\n"
"QCalendarWidget QAbstractItemView:disabled \n"
"{ \n"
"    color: #404040; \n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTreeWidget-----*/\n"
"QTreeView\n"
"{\n"
"    show-decoration-selected: 0;\n"
"    alternate-background-color: transparent;\n"
"    background-color: #e8d9d7;\n"
"       border: 1px solid #410d12;\n"
"    color: #000;\n"
"    font: 8pt;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected\n"
"{\n"
"    color:#fff;\n"
"    background-color: #af272e;\n"
"    border-radius: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:!selected:hover\n"
"{\n"
"    background-color: #ab7f83;\n"
"    border: none;\n"
"    color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings \n"
"{\n"
"    image: url(://tree-closed.png);\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  \n"
"{\n"
"    image: url(://tree-open.png);\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QListView-----*/\n"
"QListView \n"
"{\n"
"    background-color: #e8d9d7;\n"
"    alternate-background-color: transparent;\n"
"    border : none;\n"
"    color: #000;\n"
"    show-decoration-selected: 1; \n"
"    outline: 0;\n"
"       border: 1px solid #410d12;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::disabled \n"
"{\n"
"    background-color: #656565;\n"
"    color: #1b1b1b;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item \n"
"{\n"
"    background-color: transparent;\n"
"    padding: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected \n"
"{\n"
"    background-color: #af272e;\n"
"    border: 1px solid #af272e;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:!active \n"
"{\n"
"    background-color: #af272e;\n"
"    border: 1px solid #af272e;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:active \n"
"{\n"
"    background-color: #af272e;\n"
"    border: 1px solid #af272e;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:hover {\n"
"    background-color: #ab7f83;\n"
"    border: none;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox\n"
"{\n"
"    background-color: transparent;\n"
"    color: #fff;\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator\n"
"{\n"
"    background-color: lightgray;\n"
"    border: 1px solid #000;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(\"./ressources/check.png\");\n"
"    background-color: #cd70ff;\n"
"    border: 1px solid #3a546e;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 1px solid #46a2da; \n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"    background-color: #656565;\n"
"    color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QRadioButton-----*/\n"
"QRadioButton \n"
"{\n"
"    color: #fff;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked:hover \n"
"{\n"
"    background-color: #d3d3d3;\n"
"    border: 2px solid #462657;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::checked \n"
"{\n"
"    border: 2px solid #462657;\n"
"    border-radius: 6px;\n"
"    background-color: #cd70ff;  \n"
"    width: 9px; \n"
"    height: 9px; \n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:vertical \n"
"{\n"
"   border: none;\n"
"   width: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical \n"
"{\n"
"   border: none;\n"
"   background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(70, 70, 70, 255),stop:1 rgba(3, 2, 5, 255));\n"
"   min-height: 80px;\n"
"   width : 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical:pressed\n"
"{\n"
"   background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(102, 40, 40, 255),stop:0.480769 rgba(64, 19, 19, 255),stop:1 rgba(58, 0, 0, 255));\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"   border: none;\n"
"   background: transparent;\n"
"   height: 0px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover \n"
"{\n"
"   background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:pressed \n"
"{\n"
"   background-color: #3f3f3f;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"   border: none;\n"
"   background: transparent;\n"
"   height: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical:hover \n"
"{\n"
"   background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical:pressed \n"
"{\n"
"   background-color: #3f3f3f;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"   width: 0px;\n"
"   height: 0px;\n"
"   background: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical \n"
"{\n"
"   width: 0px;\n"
"   height: 0px;\n"
"   background: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"   background-color: #e8d9d7;\n"
"    \n"
"}\n"
"\n"
"\n"
"QScrollBar:horizontal \n"
"{\n"
"   border: none;\n"
"   height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal \n"
"{\n"
"   border: none;\n"
"   border-radius : 0px;\n"
"   background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(70, 70, 70, 255),stop:1 rgba(3, 2, 5, 255));\n"
"   min-height: 80px;\n"
"   height : 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal:pressed\n"
"{\n"
"   background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(102, 40, 40, 255),stop:0.480769 rgba(64, 19, 19, 255),stop:1 rgba(58, 0, 0, 255)); \n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"   border: none;\n"
"   background: transparent;\n"
"   height: 0px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal:hover \n"
"{\n"
"   background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal:pressed \n"
"{\n"
"   background-color: #3f3f3f;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"   border: none;\n"
"   background: transparent;\n"
"   height: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover \n"
"{\n"
"   background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed \n"
"{\n"
"   background-color: #3f3f3f;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:horizontal\n"
"{\n"
"   width: 0px;\n"
"   height: 0px;\n"
"   background: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:horizontal \n"
"{\n"
"   width: 0px;\n"
"   height: 0px;\n"
"   background: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"   background-color: #e8d9d7;\n"
"    \n"
"}\n"
"\n"
"\n"
"/*-----QProgressBar-----*/\n"
"QProgressBar\n"
"{\n"
"    border: 1px solid #410d12;\n"
"    text-align: center;\n"
"    color: #000;\n"
"    font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #cd70ff;\n"
"    margin: 0.5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QStatusBar-----*/\n"
"QStatusBar\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(70, 70, 70, 255),stop:1 rgba(3, 2, 5, 255));\n"
"    color: #ffffff;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QSizeGrip-----*/\n"
"QSizeGrip \n"
"{\n"
"    background-color: image(\"./ressources/sizegrip.png\"); /*To replace*/\n"
"    border: none;\n"
"\n"
"}\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.lw_remaining_wp = QtWidgets.QListWidget(Form)
        self.lw_remaining_wp.setObjectName("lw_remaining_wp")
        self.verticalLayout_6.addWidget(self.lw_remaining_wp)
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_6.addWidget(self.label_11)
        self.verticalLayout_6.setStretch(2, 20)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.cmb_staff_branch = QtWidgets.QComboBox(Form)
        self.cmb_staff_branch.setObjectName("cmb_staff_branch")
        self.verticalLayout_3.addWidget(self.cmb_staff_branch)
        self.btn_staff_wp_num = QtWidgets.QPushButton(Form)
        self.btn_staff_wp_num.setObjectName("btn_staff_wp_num")
        self.verticalLayout_3.addWidget(self.btn_staff_wp_num)
        spacerItem2 = QtWidgets.QSpacerItem(20, 23, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.lw_staff = QtWidgets.QListWidget(Form)
        self.lw_staff.setObjectName("lw_staff")
        self.verticalLayout_3.addWidget(self.lw_staff)
        self.lw_staff_day = QtWidgets.QListWidget(Form)
        self.lw_staff_day.setMaximumSize(QtCore.QSize(16777215, 100))
        self.lw_staff_day.setObjectName("lw_staff_day")
        self.verticalLayout_3.addWidget(self.lw_staff_day)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.verticalLayout_3.setStretch(4, 18)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.cmb_department = QtWidgets.QComboBox(Form)
        self.cmb_department.setObjectName("cmb_department")
        self.verticalLayout_5.addWidget(self.cmb_department)
        self.cmb_neighborhood = QtWidgets.QComboBox(Form)
        self.cmb_neighborhood.setObjectName("cmb_neighborhood")
        self.verticalLayout_5.addWidget(self.cmb_neighborhood)
        self.btn_neigh_staff = QtWidgets.QPushButton(Form)
        self.btn_neigh_staff.setObjectName("btn_neigh_staff")
        self.verticalLayout_5.addWidget(self.btn_neigh_staff)
        self.lw_appropriate_wp = QtWidgets.QListWidget(Form)
        self.lw_appropriate_wp.setObjectName("lw_appropriate_wp")
        self.verticalLayout_5.addWidget(self.lw_appropriate_wp)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.btn_add = QtWidgets.QPushButton(Form)
        self.btn_add.setObjectName("btn_add")
        self.verticalLayout.addWidget(self.btn_add)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.btn_sub = QtWidgets.QPushButton(Form)
        self.btn_sub.setObjectName("btn_sub")
        self.verticalLayout.addWidget(self.btn_sub)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.lw_assigned_wp = QtWidgets.QListWidget(Form)
        self.lw_assigned_wp.setObjectName("lw_assigned_wp")
        self.verticalLayout_2.addWidget(self.lw_assigned_wp)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_9.setText(_translate("Form", "Ataması yapılmamış işletmeler"))
        self.label_11.setText(_translate("Form", "Gün işletme sayısı"))
        self.label_2.setText(_translate("Form", "Öğretmenler"))
        self.btn_staff_wp_num.setText(_translate("Form", "Öğretmen İşletme Sayıları"))
        self.label_4.setText(_translate("Form", "Öğretmen öğrenci sayısı"))
        self.label_8.setText(_translate("Form", "Müsait İşletmeler"))
        self.btn_neigh_staff.setText(_translate("Form", "Mahalle Öğretmenleri"))
        self.label_10.setText(_translate("Form", "İşletme Öğrenci Sayısı"))
        self.btn_add.setText(_translate("Form", "Ekle>>>"))
        self.btn_sub.setText(_translate("Form", "<<<Çıkar"))
        self.label_3.setText(_translate("Form", "Atanmış işletmeler"))
        self.label_5.setText(_translate("Form", "Toplam öğrenci sayısı : "))

