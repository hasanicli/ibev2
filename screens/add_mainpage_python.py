# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Erhan/Desktop/Koordinator/ibeV1/screens/add_mainpage.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
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
"    background-color: #e4e4e4;\n"
"    color: #000;\n"
"    selection-background-color: #46a2da;\n"
"    selection-color: #fff;\n"
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
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
"    border: 1px solid #f1f1f1;\n"
"    color: #000;\n"
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
"    background-color: rgba(70,162,218,50%);\n"
"    border: 1px solid #46a2da;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:pressed \n"
"{\n"
"    background-color: #46a2da;\n"
"    border: 1px solid #46a2da;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenu-----*/\n"
"QMenu\n"
"{\n"
"    background-color: #d6d6d6;\n"
"    border: 1px solid #222;\n"
"    padding: 4px;\n"
"    color: #000;\n"
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
"       background-color: #46a2da;\n"
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
"    background-color: rgba(70,162,218,50%);\n"
"    border: 1px solid #46a2da;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolBar-----*/\n"
"QToolBar\n"
"{\n"
"    background-color: #d6d6d6;\n"
"    border-top: none;\n"
"    border-bottom: 1px solid #f1f1f1;\n"
"    border-left: 1px solid #f1f1f1;\n"
"    border-right: 1px solid #f1f1f1;\n"
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
"    padding: 3px;\n"
"    margin-left: 1px;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover\n"
"{\n"
"    background-color: rgba(70,162,218,50%);\n"
"    border: 1px solid #46a2da;\n"
"    color: #000;\n"
"    \n"
"}\n"
"\n"
"\n"
"QToolButton:pressed\n"
"{\n"
"    background-color: #727272;\n"
"    border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton:checked\n"
"{\n"
"    background-color: #727272;\n"
"    border: 1px solid #222;\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184, 184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"    color: #000;\n"
"    min-width: 80px;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
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
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"    background-color: #606060;\n"
"    color: #959595;\n"
"    border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    background-color: rgba(70,162,218,50%);\n"
"    border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(174, 174, 174, 255),stop:1 rgba(149, 149, 149, 255));\n"
"    border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::checked\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(174, 174, 174, 255),stop:1 rgba(149, 149, 149, 255));\n"
"    border: 1px solid #222;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"    background-color: #f6f6f6;\n"
"    color : #000;\n"
"    border: 1px solid #343434;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPlainTExtEdit-----*/\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #f6f6f6;\n"
"    color : #000;\n"
"    border: 1px solid #343434;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTabBar-----*/\n"
"QTabBar::tab\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
"    color: #000;\n"
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
"    background-color: #666666;\n"
"    margin-left: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    background-color: #666666;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    margin-top: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(127, 127, 127, 255),stop:1 rgba(87, 87, 87, 255));\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QComboBox-----*/\n"
"QComboBox\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184, 184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"    border: 1px solid #000;\n"
"    padding-left: 6px;\n"
"    color: #000;\n"
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
"    background-color: #46a2da;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #383838;\n"
"    color: #ffffff;\n"
"    border: 1px solid black;\n"
"    selection-background-color: #46a2da;\n"
"    outline: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(157, 157, 157, 255),stop:1 rgba(150, 150, 150, 255));\n"
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
"    background-color: #f6f6f6;\n"
"    color : #000;\n"
"    border: 1px solid #000;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button, \n"
"QDateTimeEdit::up-button\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184, 184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"    border-color: #000;\n"
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
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184, 184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"    width: 16px; \n"
"    border-width: 1px;\n"
"    border-color: #000;\n"
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
"    margin-top: 23px;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox::title  \n"
"{\n"
"    background-color: #a0a2a4;\n"
"    color: #000;\n"
"    subcontrol-position: top left;\n"
"    subcontrol-origin: margin;\n"
"    padding: 5px;\n"
"    border: 1px solid #000;\n"
"    border-bottom: none;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/*-----QHeaderView-----*/\n"
"QHeaderView::section\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
"    border: 1px solid #000;\n"
"    color: #000;\n"
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
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
"    color: #000;\n"
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
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
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
"    alternate-background-color: #c6c6c6;\n"
"    selection-color: #fff;\n"
"    background-color: #f6f6f6;\n"
"    border: 1px solid gray;\n"
"    padding-top : 5px;\n"
"    color: #000;\n"
"    font: 8pt;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:selected\n"
"{\n"
"    color:#fff;\n"
"    background-color: #46a2da;\n"
"    border-radius: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTreeView::item:!selected:hover\n"
"{\n"
"    background-color: #5e5e5e;\n"
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
"    background-color: #f6f6f6;\n"
"    border : none;\n"
"    color: #000;\n"
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
"    background-color: #f6f6f6;\n"
"    padding: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:alternate \n"
"{\n"
"    background-color: #c6c6c6;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:alternate:selected\n"
"{\n"
"    background-color: red;\n"
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
"    background-color: #46a2da;\n"
"    border: 1px solid #46a2da;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:active \n"
"{\n"
"    background-color: #46a2da;\n"
"    border: 1px solid #46a2da;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:hover {\n"
"    background-color: #5e5e5e;\n"
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
"    color: #000;\n"
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
"    background-color: #46a2da;\n"
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
"    color: #000;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked:hover \n"
"{\n"
"    background-color: darkgray;\n"
"    border: 2px solid #46a2da;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::checked \n"
"{\n"
"    border: 2px solid #52beff;\n"
"    border-radius: 6px;\n"
"    background-color: #0088da;  \n"
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
"    background-color: #46a2da;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal \n"
"{\n"
"    background-color: #5d5d5d;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal \n"
"{\n"
"    background-color: #46a2da;\n"
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
"    background-color: #0088da;\n"
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
"    background-color: #9d9d9d;\n"
"    height: 13px;\n"
"    margin: 0px 16px 0 16px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
"    border: 1px solid #2d2d2d;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
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
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
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
"    background-color: #9d9d9d;\n"
"    width: 13px;\n"
"    border: 1px solid #2d2d2d;\n"
"    margin: 16px 0px 16px 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
"    border: 1px solid #2d2d2d;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
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
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
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
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(227, 227, 227, 255),stop:1 rgba(187, 187, 187, 255));\n"
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
"    background-color: #46a2da;\n"
"    width: 5px;\n"
"    margin: 0.5px;\n"
"\n"
"}\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        self.menuEkle = QtWidgets.QMenu(self.menubar)
        self.menuEkle.setObjectName("menuEkle")
        self.menuE_itim_Y_l = QtWidgets.QMenu(self.menubar)
        self.menuE_itim_Y_l.setObjectName("menuE_itim_Y_l")
        self.menuGiri = QtWidgets.QMenu(self.menubar)
        self.menuGiri.setObjectName("menuGiri")
        self.menuKontrol = QtWidgets.QMenu(self.menubar)
        self.menuKontrol.setObjectName("menuKontrol")
        self.menuBarkod = QtWidgets.QMenu(self.menubar)
        self.menuBarkod.setObjectName("menuBarkod")
        self.menuVeri_Al = QtWidgets.QMenu(self.menubar)
        self.menuVeri_Al.setObjectName("menuVeri_Al")
        self.menuRaporlama = QtWidgets.QMenu(self.menubar)
        self.menuRaporlama.setObjectName("menuRaporlama")
        self.menuSGK = QtWidgets.QMenu(self.menubar)
        self.menuSGK.setObjectName("menuSGK")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.act_student = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.act_student.setFont(font)
        self.act_student.setObjectName("act_student")
        self.act_department = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.act_department.setFont(font)
        self.act_department.setObjectName("act_department")
        self.act_branch = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.act_branch.setFont(font)
        self.act_branch.setObjectName("act_branch")
        self.act_class = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.act_class.setFont(font)
        self.act_class.setObjectName("act_class")
        self.act_staff = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.act_staff.setFont(font)
        self.act_staff.setObjectName("act_staff")
        self.act_staff_branch = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.act_staff_branch.setFont(font)
        self.act_staff_branch.setObjectName("act_staff_branch")
        self.act_degree = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.act_degree.setFont(font)
        self.act_degree.setObjectName("act_degree")
        self.act_institutation_info = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.act_institutation_info.setFont(font)
        self.act_institutation_info.setObjectName("act_institutation_info")
        self.act_workplace = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.act_workplace.setFont(font)
        self.act_workplace.setObjectName("act_workplace")
        self.act_cause = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.act_cause.setFont(font)
        self.act_cause.setObjectName("act_cause")
        self.act_document = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.act_document.setFont(font)
        self.act_document.setObjectName("act_document")
        self.act_social_club = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.act_social_club.setFont(font)
        self.act_social_club.setObjectName("act_social_club")
        self.actionE_itim_Y_l_Ekle = QtWidgets.QAction(MainWindow)
        self.actionE_itim_Y_l_Ekle.setObjectName("actionE_itim_Y_l_Ekle")
        self.actionE_itim_Y_l_Se = QtWidgets.QAction(MainWindow)
        self.actionE_itim_Y_l_Se.setObjectName("actionE_itim_Y_l_Se")
        self.actionE_itim_Y_l_Kopyala = QtWidgets.QAction(MainWindow)
        self.actionE_itim_Y_l_Kopyala.setObjectName("actionE_itim_Y_l_Kopyala")
        self.actionYedek_Al = QtWidgets.QAction(MainWindow)
        self.actionYedek_Al.setObjectName("actionYedek_Al")
        self.actionYedekten_Getir = QtWidgets.QAction(MainWindow)
        self.actionYedekten_Getir.setObjectName("actionYedekten_Getir")
        self.actionKullan_c_Giri_i = QtWidgets.QAction(MainWindow)
        self.actionKullan_c_Giri_i.setObjectName("actionKullan_c_Giri_i")
        self.actionMisafir_Giri_i = QtWidgets.QAction(MainWindow)
        self.actionMisafir_Giri_i.setObjectName("actionMisafir_Giri_i")
        self.actionT_m_Bilgiler = QtWidgets.QAction(MainWindow)
        self.actionT_m_Bilgiler.setObjectName("actionT_m_Bilgiler")
        self.actionEksik_Bilgi_Doldur = QtWidgets.QAction(MainWindow)
        self.actionEksik_Bilgi_Doldur.setObjectName("actionEksik_Bilgi_Doldur")
        self.actionBarkod_Olu_tur = QtWidgets.QAction(MainWindow)
        self.actionBarkod_Olu_tur.setObjectName("actionBarkod_Olu_tur")
        self.actionBarkod_Oku = QtWidgets.QAction(MainWindow)
        self.actionBarkod_Oku.setObjectName("actionBarkod_Oku")
        self.actionVeri_Giri_i_Yap = QtWidgets.QAction(MainWindow)
        self.actionVeri_Giri_i_Yap.setObjectName("actionVeri_Giri_i_Yap")
        self.actionVeri_k_Yap = QtWidgets.QAction(MainWindow)
        self.actionVeri_k_Yap.setObjectName("actionVeri_k_Yap")
        self.actionSe_enekli_Rapor_Olu_tur = QtWidgets.QAction(MainWindow)
        self.actionSe_enekli_Rapor_Olu_tur.setObjectName("actionSe_enekli_Rapor_Olu_tur")
        self.actionHaftal_k_Form_retmen = QtWidgets.QAction(MainWindow)
        self.actionHaftal_k_Form_retmen.setObjectName("actionHaftal_k_Form_retmen")
        self.actionHaftal_k_Form_i_letme = QtWidgets.QAction(MainWindow)
        self.actionHaftal_k_Form_i_letme.setObjectName("actionHaftal_k_Form_i_letme")
        self.actionAyl_k_Form_retmen = QtWidgets.QAction(MainWindow)
        self.actionAyl_k_Form_retmen.setObjectName("actionAyl_k_Form_retmen")
        self.actionAyl_k_Form_i_letme = QtWidgets.QAction(MainWindow)
        self.actionAyl_k_Form_i_letme.setObjectName("actionAyl_k_Form_i_letme")
        self.action_retmen_G_rev_Formu = QtWidgets.QAction(MainWindow)
        self.action_retmen_G_rev_Formu.setObjectName("action_retmen_G_rev_Formu")
        self.actionD_nen_Evrak_Kontrol = QtWidgets.QAction(MainWindow)
        self.actionD_nen_Evrak_Kontrol.setObjectName("actionD_nen_Evrak_Kontrol")
        self.action_renci_Devams_zl_k_Ekle = QtWidgets.QAction(MainWindow)
        self.action_renci_Devams_zl_k_Ekle.setObjectName("action_renci_Devams_zl_k_Ekle")
        self.actionOkul_SGK_Bilgileri_Ekle = QtWidgets.QAction(MainWindow)
        self.actionOkul_SGK_Bilgileri_Ekle.setObjectName("actionOkul_SGK_Bilgileri_Ekle")
        self.actionSGK_Prim_Belgesi_7 = QtWidgets.QAction(MainWindow)
        self.actionSGK_Prim_Belgesi_7.setObjectName("actionSGK_Prim_Belgesi_7")
        self.actionSGK_Prim_Belgesi_42 = QtWidgets.QAction(MainWindow)
        self.actionSGK_Prim_Belgesi_42.setObjectName("actionSGK_Prim_Belgesi_42")
        self.actionSGK_Prim_Belgesi_49 = QtWidgets.QAction(MainWindow)
        self.actionSGK_Prim_Belgesi_49.setObjectName("actionSGK_Prim_Belgesi_49")
        self.actionSGK_Prim_Belgesi_50 = QtWidgets.QAction(MainWindow)
        self.actionSGK_Prim_Belgesi_50.setObjectName("actionSGK_Prim_Belgesi_50")
        self.actionVeri_Giri_i_Yap_2 = QtWidgets.QAction(MainWindow)
        self.actionVeri_Giri_i_Yap_2.setObjectName("actionVeri_Giri_i_Yap_2")
        self.act_neighborhood = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.act_neighborhood.setFont(font)
        self.act_neighborhood.setObjectName("act_neighborhood")
        self.act_parent_class = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.act_parent_class.setFont(font)
        self.act_parent_class.setObjectName("act_parent_class")
        self.act_day = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.act_day.setFont(font)
        self.act_day.setObjectName("act_day")
        self.act_add_class_to_parent = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.act_add_class_to_parent.setFont(font)
        self.act_add_class_to_parent.setObjectName("act_add_class_to_parent")
        self.act_staff_workplace = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.act_staff_workplace.setFont(font)
        self.act_staff_workplace.setObjectName("act_staff_workplace")
        self.act_staff_days = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.act_staff_days.setFont(font)
        self.act_staff_days.setObjectName("act_staff_days")
        self.act_class_days = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.act_class_days.setFont(font)
        self.act_class_days.setObjectName("act_class_days")
        self.act_change_workplace = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.act_change_workplace.setFont(font)
        self.act_change_workplace.setObjectName("act_change_workplace")
        self.act_disconnection = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.act_disconnection.setFont(font)
        self.act_disconnection.setObjectName("act_disconnection")
        self.menuEkle.addAction(self.act_student)
        self.menuEkle.addSeparator()
        self.menuEkle.addAction(self.act_department)
        self.menuEkle.addAction(self.act_branch)
        self.menuEkle.addAction(self.act_class)
        self.menuEkle.addAction(self.act_parent_class)
        self.menuEkle.addSeparator()
        self.menuEkle.addAction(self.act_staff)
        self.menuEkle.addAction(self.act_staff_branch)
        self.menuEkle.addAction(self.act_degree)
        self.menuEkle.addSeparator()
        self.menuEkle.addAction(self.act_institutation_info)
        self.menuEkle.addSeparator()
        self.menuEkle.addAction(self.act_workplace)
        self.menuEkle.addSeparator()
        self.menuEkle.addAction(self.act_cause)
        self.menuEkle.addAction(self.act_neighborhood)
        self.menuEkle.addAction(self.act_day)
        self.menuEkle.addAction(self.act_add_class_to_parent)
        self.menuEkle.addAction(self.act_staff_workplace)
        self.menuEkle.addAction(self.act_change_workplace)
        self.menuEkle.addAction(self.act_disconnection)
        self.menuE_itim_Y_l.addAction(self.actionE_itim_Y_l_Ekle)
        self.menuE_itim_Y_l.addAction(self.actionE_itim_Y_l_Se)
        self.menuE_itim_Y_l.addAction(self.actionE_itim_Y_l_Kopyala)
        self.menuE_itim_Y_l.addAction(self.actionYedek_Al)
        self.menuE_itim_Y_l.addAction(self.actionYedekten_Getir)
        self.menuGiri.addAction(self.actionKullan_c_Giri_i)
        self.menuGiri.addAction(self.actionMisafir_Giri_i)
        self.menuKontrol.addAction(self.actionT_m_Bilgiler)
        self.menuKontrol.addAction(self.actionEksik_Bilgi_Doldur)
        self.menuBarkod.addAction(self.actionBarkod_Olu_tur)
        self.menuBarkod.addAction(self.actionBarkod_Oku)
        self.menuVeri_Al.addAction(self.actionVeri_Giri_i_Yap)
        self.menuVeri_Al.addAction(self.actionVeri_k_Yap)
        self.menuVeri_Al.addAction(self.actionVeri_Giri_i_Yap_2)
        self.menuRaporlama.addAction(self.actionSe_enekli_Rapor_Olu_tur)
        self.menuRaporlama.addAction(self.actionHaftal_k_Form_retmen)
        self.menuRaporlama.addAction(self.actionHaftal_k_Form_i_letme)
        self.menuRaporlama.addAction(self.actionAyl_k_Form_retmen)
        self.menuRaporlama.addAction(self.actionAyl_k_Form_i_letme)
        self.menuRaporlama.addAction(self.action_retmen_G_rev_Formu)
        self.menuRaporlama.addAction(self.actionD_nen_Evrak_Kontrol)
        self.menuSGK.addAction(self.action_renci_Devams_zl_k_Ekle)
        self.menuSGK.addAction(self.actionOkul_SGK_Bilgileri_Ekle)
        self.menuSGK.addAction(self.actionSGK_Prim_Belgesi_7)
        self.menuSGK.addAction(self.actionSGK_Prim_Belgesi_42)
        self.menuSGK.addAction(self.actionSGK_Prim_Belgesi_49)
        self.menuSGK.addAction(self.actionSGK_Prim_Belgesi_50)
        self.menubar.addAction(self.menuGiri.menuAction())
        self.menubar.addAction(self.menuE_itim_Y_l.menuAction())
        self.menubar.addAction(self.menuEkle.menuAction())
        self.menubar.addAction(self.menuKontrol.menuAction())
        self.menubar.addAction(self.menuBarkod.menuAction())
        self.menubar.addAction(self.menuVeri_Al.menuAction())
        self.menubar.addAction(self.menuSGK.menuAction())
        self.menubar.addAction(self.menuRaporlama.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuEkle.setTitle(_translate("MainWindow", "Ekle"))
        self.menuE_itim_Y_l.setTitle(_translate("MainWindow", "Eğitim Yılı"))
        self.menuGiri.setTitle(_translate("MainWindow", "Giriş"))
        self.menuKontrol.setTitle(_translate("MainWindow", "Kontrol"))
        self.menuBarkod.setTitle(_translate("MainWindow", "Barkod"))
        self.menuVeri_Al.setTitle(_translate("MainWindow", "Veri Al"))
        self.menuRaporlama.setTitle(_translate("MainWindow", "Raporlama"))
        self.menuSGK.setTitle(_translate("MainWindow", "SGK"))
        self.act_student.setText(_translate("MainWindow", "Öğrenci"))
        self.act_department.setText(_translate("MainWindow", "Alan Ekle"))
        self.act_branch.setText(_translate("MainWindow", "Dal Ekle"))
        self.act_class.setText(_translate("MainWindow", "Sınıf Ekle"))
        self.act_staff.setText(_translate("MainWindow", "Personel Ekle"))
        self.act_staff_branch.setText(_translate("MainWindow", "Branş Ekle"))
        self.act_degree.setText(_translate("MainWindow", "Unvan Ekle"))
        self.act_institutation_info.setText(_translate("MainWindow", "Okul Bilgileri Ekle"))
        self.act_workplace.setText(_translate("MainWindow", "İşletme Ekle"))
        self.act_cause.setText(_translate("MainWindow", "Ayrılma Sebebi"))
        self.act_document.setText(_translate("MainWindow", "Belge Türü"))
        self.act_social_club.setText(_translate("MainWindow", "Sosyal Kulüp"))
        self.actionE_itim_Y_l_Ekle.setText(_translate("MainWindow", "Eğitim Yılı Ekle"))
        self.actionE_itim_Y_l_Se.setText(_translate("MainWindow", "Eğitim Yılı Seç"))
        self.actionE_itim_Y_l_Kopyala.setText(_translate("MainWindow", "Eğitim Yılı Kopyala"))
        self.actionYedek_Al.setText(_translate("MainWindow", "Yedek Al"))
        self.actionYedekten_Getir.setText(_translate("MainWindow", "Yedekten Getir"))
        self.actionKullan_c_Giri_i.setText(_translate("MainWindow", "Kullanıcı Girişi"))
        self.actionMisafir_Giri_i.setText(_translate("MainWindow", "Misafir Girişi"))
        self.actionT_m_Bilgiler.setText(_translate("MainWindow", "Tüm Bilgiler"))
        self.actionEksik_Bilgi_Doldur.setText(_translate("MainWindow", "Eksik Bilgi Doldur"))
        self.actionBarkod_Olu_tur.setText(_translate("MainWindow", "Barkod Oluştur"))
        self.actionBarkod_Oku.setText(_translate("MainWindow", "Barkod Oku"))
        self.actionVeri_Giri_i_Yap.setText(_translate("MainWindow", "Veri Girişi Yap (Excel)"))
        self.actionVeri_k_Yap.setText(_translate("MainWindow", "Veri Çıkışı Yap (Excel)"))
        self.actionSe_enekli_Rapor_Olu_tur.setText(_translate("MainWindow", "Seçenekli Rapor Oluştur"))
        self.actionHaftal_k_Form_retmen.setText(_translate("MainWindow", "Haftalık Form (Öğretmen)"))
        self.actionHaftal_k_Form_i_letme.setText(_translate("MainWindow", "Haftalık Form (işletme)"))
        self.actionAyl_k_Form_retmen.setText(_translate("MainWindow", "Aylık Form (Öğretmen)"))
        self.actionAyl_k_Form_i_letme.setText(_translate("MainWindow", "Aylık Form (işletme)"))
        self.action_retmen_G_rev_Formu.setText(_translate("MainWindow", "Öğretmen Görev Formu"))
        self.actionD_nen_Evrak_Kontrol.setText(_translate("MainWindow", "Dönen Evrak Kontrol"))
        self.action_renci_Devams_zl_k_Ekle.setText(_translate("MainWindow", "Öğrenci Devamsızlık Ekle"))
        self.actionOkul_SGK_Bilgileri_Ekle.setText(_translate("MainWindow", "Okul SGK Bilgileri Ekle"))
        self.actionSGK_Prim_Belgesi_7.setText(_translate("MainWindow", "SGK Prim Belgesi (7)"))
        self.actionSGK_Prim_Belgesi_42.setText(_translate("MainWindow", "SGK Prim Belgesi (42)"))
        self.actionSGK_Prim_Belgesi_49.setText(_translate("MainWindow", "SGK Prim Belgesi (49)"))
        self.actionSGK_Prim_Belgesi_50.setText(_translate("MainWindow", "SGK Prim Belgesi (50)"))
        self.actionVeri_Giri_i_Yap_2.setText(_translate("MainWindow", "Veri Girişi Yap"))
        self.act_neighborhood.setText(_translate("MainWindow", "Semt/Mahalle Ekle"))
        self.act_parent_class.setText(_translate("MainWindow", "Ortak Sınıf Ekle"))
        self.act_day.setText(_translate("MainWindow", "Günler"))
        self.act_add_class_to_parent.setText(_translate("MainWindow", "Ortak sınıfa alt sınıf ekle"))
        self.act_staff_workplace.setText(_translate("MainWindow", "Öğretmen-İşletme"))
        self.act_staff_days.setText(_translate("MainWindow", "Öğretmen İşletme Günleri Ekle"))
        self.act_class_days.setText(_translate("MainWindow", "Sınıf İşletme Günleri Ekle"))
        self.act_change_workplace.setText(_translate("MainWindow", "İşletme Değiştir"))
        self.act_disconnection.setText(_translate("MainWindow", "Ayrılış Yap"))

