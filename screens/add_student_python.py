# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Erhan/Desktop/Koordinator/ibeV2/screens/add_student.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(755, 527)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("/*Copyright (c) DevSec Studio. All rights reserved.\n"
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
"    background-color: #3a3a3a;\n"
"    color: #fff;\n"
"    selection-background-color: #b78620;\n"
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
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #000;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item \n"
"{\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:selected \n"
"{\n"
"    background-color: rgba(183, 134, 32, 20%);\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:pressed \n"
"{\n"
"    background-color: rgb(183, 134, 32);\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenu-----*/\n"
"QMenu\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #222;\n"
"    padding: 4px;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item\n"
"{\n"
"    background-color: transparent;\n"
"    padding: 2px 20px 2px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"       background-color: rgb(183, 134, 32);\n"
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
"    background-color: rgba(183, 134, 32, 20%);\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolBar-----*/\n"
"QToolBar\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(69, 69, 69, 255),stop:1 rgba(58, 58, 58, 255));\n"
"    border-top: none;\n"
"    border-bottom: 1px solid #4f4f4f;\n"
"    border-left: 1px solid #4f4f4f;\n"
"    border-right: 1px solid #4f4f4f;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolBar::separator\n"
"{\n"
"    background-color: #2e2e2e;\n"
"    width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton \n"
"{\n"
"    background-color: transparent;\n"
"    color: #fff;\n"
"    padding: 5px;\n"
"    padding-left: 8px;\n"
"    padding-right: 8px;\n"
"    margin-left: 1px;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover\n"
"{\n"
"    background-color: rgba(183, 134, 32, 20%);\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"    \n"
"}\n"
"\n"
"\n"
"QToolButton:pressed\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton:checked\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #222;\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));\n"
"    color: #ffffff;\n"
"    min-width: 80px;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 3px;\n"
"    border-color: #051a39;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::flat\n"
"{\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"    background-color: #404040;\n"
"    color: #656565;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    background-color: rgba(183, 134, 32, 20%);\n"
"    border: 1px solid #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));\n"
"    border: 1px solid #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::checked\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));\n"
"    border: 1px solid #222;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"    background-color: #131313;\n"
"    color : #eee;\n"
"    border: 1px solid #343434;\n"
"    border-radius: 2px;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPlainTExtEdit-----*/\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #131313;\n"
"    color : #eee;\n"
"    border: 1px solid #343434;\n"
"    border-radius: 2px;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTabBar-----*/\n"
"QTabBar::tab\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));\n"
"    color: #ffffff;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: #666;\n"
"    border-bottom: none;\n"
"    padding: 5px;\n"
"    padding-left: 15px;\n"
"    padding-right: 15px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane \n"
"{\n"
"    background-color: red;\n"
"    border: 1px solid #666;\n"
"    top: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; \n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
"    background-color: #0c0c0d;\n"
"    margin-left: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    background-color: #0c0c0d;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    margin-bottom: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    border-top-color: #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QComboBox-----*/\n"
"QComboBox\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));\n"
"    border: 1px solid #000;\n"
"    padding-left: 6px;\n"
"    color: #ffffff;\n"
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
"    background-color: #b78620;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #383838;\n"
"    color: #ffffff;\n"
"    border: 1px solid black;\n"
"    selection-background-color: #b78620;\n"
"    outline: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: black;\n"
"    border-left-style: solid; \n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"\n"
"/*-----QSpinBox & QDateTimeEdit-----*/\n"
"QSpinBox,\n"
"QDateTimeEdit \n"
"{\n"
"    background-color: #131313;\n"
"    color : #eee;\n"
"    border: 1px solid #343434;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    border-radius : 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button, \n"
"QDateTimeEdit::up-button\n"
"{\n"
"    border-top-right-radius:2px;\n"
"    background-color: #777777;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:hover, \n"
"QDateTimeEdit::up-button:hover\n"
"{\n"
"    background-color: #585858;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:pressed, \n"
"QDateTimeEdit::up-button:pressed\n"
"{\n"
"    background-color: #252525;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-arrow,\n"
"QDateTimeEdit::up-arrow\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 7px;\n"
"    height: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button, \n"
"QDateTimeEdit::down-button\n"
"{\n"
"    border-bottom-right-radius:2px;\n"
"    background-color: #777777;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button:hover, \n"
"QDateTimeEdit::down-button:hover\n"
"{\n"
"    background-color: #585858;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button:pressed, \n"
"QDateTimeEdit::down-button:pressed\n"
"{\n"
"    background-color: #252525;\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-arrow,\n"
"QDateTimeEdit::down-arrow\n"
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
"    border: 1px solid;\n"
"    border-color: #666666;\n"
"    border-radius: 5px;\n"
"    margin-top: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox::title  \n"
"{\n"
"    background-color: transparent;\n"
"    color: #eee;\n"
"    subcontrol-origin: margin;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QHeaderView-----*/\n"
"QHeaderView::section\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(60, 60, 60, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #000;\n"
"    color: #fff;\n"
"    text-align: left;\n"
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
"QHeaderView::section:checked\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(60, 60, 60, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(60, 60, 60, 255),stop:1 rgba(50, 50, 50, 255));\n"
"    border: 1px solid #000;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTreeWidget-----*/\n"
"QTreeView\n"
"{\n"
"    show-decoration-selected: 1;\n"
"    alternate-background-color: #3a3a3a;\n"
"    selection-color: #fff;\n"
"    background-color: #2d2d2d;\n"
"    border: 1px solid gray;\n"
"    padding-top : 5px;\n"
"    color: #fff;\n"
"    font: 8pt;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected\n"
"{\n"
"    color:#fff;\n"
"    background-color: #b78620;\n"
"    border-radius: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:!selected:hover\n"
"{\n"
"    background-color: #262626;\n"
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
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(83, 83, 83, 255),stop:0.293269 rgba(81, 81, 81, 255),stop:0.634615 rgba(79, 79, 79, 255),stop:1 rgba(83, 83, 83, 255));\n"
"    border : none;\n"
"    color: white;\n"
"    show-decoration-selected: 1; \n"
"    outline: 0;\n"
"    border: 1px solid gray;\n"
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
"    background-color: #2d2d2d;\n"
"    padding: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:alternate \n"
"{\n"
"    background-color: #3a3a3a;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected \n"
"{\n"
"    background-color: #b78620;\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:!active \n"
"{\n"
"    background-color: #b78620;\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:active \n"
"{\n"
"    background-color: #b78620;\n"
"    border: 1px solid #b78620;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:hover {\n"
"    background-color: #262626;\n"
"    border: none;\n"
"    color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox\n"
"{\n"
"    background-color: transparent;\n"
"    color: lightgray;\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator\n"
"{\n"
"    background-color: #323232;\n"
"    border: 1px solid darkgray;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(\"./ressources/check.png\");\n"
"    background-color: #b78620;\n"
"    border: 1px solid #3a546e;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 1px solid #b78620; \n"
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
"    color: lightgray;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked:hover \n"
"{\n"
"    background-color: lightgray;\n"
"    border: 2px solid #b78620;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::checked \n"
"{\n"
"    border: 2px solid #b78620;\n"
"    border-radius: 6px;\n"
"    background-color: rgba(183,134,32,20%);  \n"
"    width: 9px; \n"
"    height: 9px; \n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QSlider-----*/\n"
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
"    background-color: #b78620;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal \n"
"{\n"
"    background-color: #131313;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal \n"
"{\n"
"    background-color: #b78620;\n"
"    width: 14px;\n"
"    margin-top: -6px;\n"
"    margin-bottom: -6px;\n"
"    border-radius: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal:hover \n"
"{\n"
"    background-color: #d89e25;\n"
"    border-radius: 6px;\n"
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
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal\n"
"{\n"
"    border: 1px solid #222222;\n"
"    background-color: #3d3d3d;\n"
"    height: 15px;\n"
"    margin: 0px 16px 0 16px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"    border: 1px solid #2d2d2d;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"    border: 1px solid #2d2d2d;\n"
"    width: 15px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"    border: 1px solid #2d2d2d;\n"
"    width: 15px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-right.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::left-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-left.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #3d3d3d;\n"
"    width: 16px;\n"
"    border: 1px solid #2d2d2d;\n"
"    margin: 16px 0px 16px 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"    border: 1px solid #2d2d2d;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"    border: 1px solid #2d2d2d;\n"
"    height: 15px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(97, 97, 97, 255),stop:1 rgba(90, 90, 90, 255));\n"
"    border: 1px solid #2d2d2d;\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QProgressBar-----*/\n"
"QProgressBar\n"
"{\n"
"    border: 1px solid #666666;\n"
"    text-align: center;\n"
"    color: #000;\n"
"    font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #b78620;\n"
"    width: 30px;\n"
"    margin: 0.5px;\n"
"\n"
"}\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.horizontalLayout_2.addWidget(self.line_9)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(13, 5, 13, 5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_3.addWidget(self.line_8)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.lbl_photo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_photo.setMinimumSize(QtCore.QSize(96, 128))
        self.lbl_photo.setMaximumSize(QtCore.QSize(96, 128))
        self.lbl_photo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lbl_photo.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lbl_photo.setText("")
        self.lbl_photo.setPixmap(QtGui.QPixmap("../../Pictures/resimler/0000.png"))
        self.lbl_photo.setScaledContents(True)
        self.lbl_photo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_photo.setWordWrap(False)
        self.lbl_photo.setObjectName("lbl_photo")
        self.verticalLayout_3.addWidget(self.lbl_photo)
        self.btn_take_photo = QtWidgets.QPushButton(self.centralwidget)
        self.btn_take_photo.setMinimumSize(QtCore.QSize(92, 0))
        self.btn_take_photo.setMaximumSize(QtCore.QSize(96, 16777215))
        self.btn_take_photo.setObjectName("btn_take_photo")
        self.verticalLayout_3.addWidget(self.btn_take_photo)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_3.addWidget(self.line_7)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_2.addWidget(self.line_5)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_2.addWidget(self.line_6)
        self.verticalGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.verticalGroupBox.setFont(font)
        self.verticalGroupBox.setStyleSheet("#verticalGroupBox{\n"
"    \n"
"}")
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout.setContentsMargins(10, 10, 8, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_save = QtWidgets.QPushButton(self.verticalGroupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_save.setFont(font)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        self.btn_change_id = QtWidgets.QPushButton(self.verticalGroupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_change_id.setFont(font)
        self.btn_change_id.setObjectName("btn_change_id")
        self.horizontalLayout.addWidget(self.btn_change_id)
        self.btn_edit = QtWidgets.QPushButton(self.verticalGroupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_edit.setFont(font)
        self.btn_edit.setObjectName("btn_edit")
        self.horizontalLayout.addWidget(self.btn_edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.line_4 = QtWidgets.QFrame(self.verticalGroupBox)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.btn_clear_all = QtWidgets.QPushButton(self.verticalGroupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_clear_all.setFont(font)
        self.btn_clear_all.setObjectName("btn_clear_all")
        self.verticalLayout.addWidget(self.btn_clear_all)
        self.line_3 = QtWidgets.QFrame(self.verticalGroupBox)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_2.addWidget(self.verticalGroupBox)
        self.horizontalLayout_2.setStretch(1, 20)
        self.horizontalLayout_2.setStretch(5, 80)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(460, 300))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("#tab_student{\n"
"border-image: url(:/flat/blue_background_abstract-wide.jpg);}\n"
"#tab_personal{\n"
"border-image: url(:/flat/blue_background_abstract-wide.jpg);}\n"
"#tab_communication{\n"
"border-image: url(:/flat/blue_background_abstract-wide.jpg);}\n"
"#tab_workplace{\n"
"border-image: url(:/flat/blue_background_abstract-wide.jpg);}\n"
"#tab_leaving{\n"
"border-image: url(:/flat/blue_background_abstract-wide.jpg);}\n"
"    ")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_student = QtWidgets.QWidget()
        self.tab_student.setObjectName("tab_student")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab_student)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 441, 256))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_19 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.le_id_number = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.le_id_number.setFont(font)
        self.le_id_number.setObjectName("le_id_number")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_id_number)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label)
        self.le_number = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.le_number.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.le_number.setFont(font)
        self.le_number.setInputMask("")
        self.le_number.setPlaceholderText("")
        self.le_number.setObjectName("le_number")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.le_number)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.date_record = QtWidgets.QDateEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.date_record.setFont(font)
        self.date_record.setProperty("showGroupSeparator", False)
        self.date_record.setCalendarPopup(True)
        self.date_record.setObjectName("date_record")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.date_record)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.le_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.le_name.setFont(font)
        self.le_name.setObjectName("le_name")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.le_name)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.le_surname = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.le_surname.setFont(font)
        self.le_surname.setObjectName("le_surname")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.le_surname)
        self.cmb_department = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cmb_department.setFont(font)
        self.cmb_department.setObjectName("cmb_department")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.cmb_department)
        self.cmb_branch = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cmb_branch.setFont(font)
        self.cmb_branch.setObjectName("cmb_branch")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.cmb_branch)
        self.cmb_class = QtWidgets.QComboBox(self.formLayoutWidget)
        self.cmb_class.setMaximumSize(QtCore.QSize(10000, 10000))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cmb_class.setFont(font)
        self.cmb_class.setAutoFillBackground(False)
        self.cmb_class.setObjectName("cmb_class")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.cmb_class)
        self.tabWidget.addTab(self.tab_student, "")
        self.tab_personal = QtWidgets.QWidget()
        self.tab_personal.setObjectName("tab_personal")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.tab_personal)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 441, 201))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.le_father_name = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.le_father_name.setFont(font)
        self.le_father_name.setObjectName("le_father_name")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_father_name)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.le_mother_name = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.le_mother_name.setFont(font)
        self.le_mother_name.setObjectName("le_mother_name")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_mother_name)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.date_of_birth = QtWidgets.QDateEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.date_of_birth.setFont(font)
        self.date_of_birth.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.date_of_birth.setCalendarPopup(True)
        self.date_of_birth.setObjectName("date_of_birth")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.date_of_birth)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.le_birth_place = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.le_birth_place.setFont(font)
        self.le_birth_place.setObjectName("le_birth_place")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.le_birth_place)
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.rb_male = QtWidgets.QRadioButton(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.rb_male.setFont(font)
        self.rb_male.setChecked(True)
        self.rb_male.setObjectName("rb_male")
        self.verticalLayout_4.addWidget(self.rb_male)
        self.rb_female = QtWidgets.QRadioButton(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.rb_female.setFont(font)
        self.rb_female.setObjectName("rb_female")
        self.verticalLayout_4.addWidget(self.rb_female)
        self.formLayout_2.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(4, QtWidgets.QFormLayout.LabelRole, spacerItem4)
        self.tabWidget.addTab(self.tab_personal, "")
        self.tab_workplace = QtWidgets.QWidget()
        self.tab_workplace.setObjectName("tab_workplace")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.tab_workplace)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 441, 101))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.cmb_workplace = QtWidgets.QComboBox(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cmb_workplace.setFont(font)
        self.cmb_workplace.setObjectName("cmb_workplace")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cmb_workplace)
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.le_coordinator = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.le_coordinator.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.le_coordinator.setFont(font)
        self.le_coordinator.setObjectName("le_coordinator")
        self.horizontalLayout_4.addWidget(self.le_coordinator)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget_3)
        self.pushButton.setMinimumSize(QtCore.QSize(92, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.horizontalLayout_4.setStretch(0, 150)
        self.formLayout_3.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.date_starting_work = QtWidgets.QDateEdit(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.date_starting_work.setFont(font)
        self.date_starting_work.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.date_starting_work.setCalendarPopup(True)
        self.date_starting_work.setObjectName("date_starting_work")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.date_starting_work)
        self.tabWidget.addTab(self.tab_workplace, "")
        self.tab_communication = QtWidgets.QWidget()
        self.tab_communication.setObjectName("tab_communication")
        self.formLayoutWidget_5 = QtWidgets.QWidget(self.tab_communication)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(10, 10, 441, 135))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.formLayout_5.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.label_20 = QtWidgets.QLabel(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.le_father_phone = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.le_father_phone.setFont(font)
        self.le_father_phone.setObjectName("le_father_phone")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_father_phone)
        self.label_21 = QtWidgets.QLabel(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.le_mother_phone = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.le_mother_phone.setFont(font)
        self.le_mother_phone.setObjectName("le_mother_phone")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.le_mother_phone)
        self.label_22 = QtWidgets.QLabel(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.le_email = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.le_email.setFont(font)
        self.le_email.setObjectName("le_email")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.le_email)
        self.le_self_phone = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.le_self_phone.setFont(font)
        self.le_self_phone.setInputMask("")
        self.le_self_phone.setText("")
        self.le_self_phone.setObjectName("le_self_phone")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_self_phone)
        self.tabWidget.addTab(self.tab_communication, "")
        self.horizontalLayout_3.addWidget(self.tabWidget)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        spacerItem5 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formFrame_6 = QtWidgets.QFrame(self.centralwidget)
        self.formFrame_6.setObjectName("formFrame_6")
        self.formLayout_6 = QtWidgets.QFormLayout(self.formFrame_6)
        self.formLayout_6.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_25 = QtWidgets.QLabel(self.formFrame_6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.le_search = QtWidgets.QLineEdit(self.formFrame_6)
        self.le_search.setObjectName("le_search")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_search)
        self.verticalLayout_2.addWidget(self.formFrame_6)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.lw_students = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lw_students.setFont(font)
        self.lw_students.setObjectName("lw_students")
        self.verticalLayout_2.addWidget(self.lw_students)
        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 84)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.setStretch(2, 2)
        self.horizontalLayout_3.setStretch(4, 48)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_take_photo.setText(_translate("MainWindow", "Foto Yükle"))
        self.btn_save.setText(_translate("MainWindow", "Kaydet"))
        self.btn_change_id.setText(_translate("MainWindow", "TC Değiştir"))
        self.btn_edit.setText(_translate("MainWindow", "Güncelle"))
        self.btn_clear_all.setText(_translate("MainWindow", "Yeni Kayıt İçin Temizle"))
        self.label_19.setText(_translate("MainWindow", "TC Kimlik No : "))
        self.label.setText(_translate("MainWindow", "Numara : "))
        self.label_2.setText(_translate("MainWindow", "Alan : "))
        self.label_3.setText(_translate("MainWindow", "Dal : "))
        self.label_4.setText(_translate("MainWindow", "Sınıf : "))
        self.label_6.setText(_translate("MainWindow", "Kayıt Tarihi : "))
        self.date_record.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy"))
        self.label_5.setText(_translate("MainWindow", "Adı : "))
        self.label_7.setText(_translate("MainWindow", "Soyadı : "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_student), _translate("MainWindow", "Okul"))
        self.label_8.setText(_translate("MainWindow", "Baba Adı : "))
        self.label_9.setText(_translate("MainWindow", "Ana Adı : "))
        self.label_10.setText(_translate("MainWindow", "Doğum Tarihi : "))
        self.date_of_birth.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy"))
        self.label_11.setText(_translate("MainWindow", "Doğum Yeri : "))
        self.label_15.setText(_translate("MainWindow", "Cinsiyet : "))
        self.rb_male.setText(_translate("MainWindow", "Erkek"))
        self.rb_female.setText(_translate("MainWindow", "Kız"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_personal), _translate("MainWindow", "Kişisel"))
        self.label_12.setText(_translate("MainWindow", "İşletme Adı : "))
        self.label_13.setText(_translate("MainWindow", "Koordinatör Öğretmen : "))
        self.pushButton.setText(_translate("MainWindow", "Seç"))
        self.label_14.setText(_translate("MainWindow", "İşe Giriş Tarihi : "))
        self.date_starting_work.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_workplace), _translate("MainWindow", "İşletme"))
        self.label_17.setText(_translate("MainWindow", "Kendi Telefonu :"))
        self.label_20.setText(_translate("MainWindow", "Veli Telefonu1 :"))
        self.label_21.setText(_translate("MainWindow", "Veli Telefonu2 :"))
        self.label_22.setText(_translate("MainWindow", "E-Posta :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_communication), _translate("MainWindow", "İletişim"))
        self.label_25.setText(_translate("MainWindow", "Ara : "))

