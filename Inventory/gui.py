# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.main_label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.main_label.setFont(font)
        self.main_label.setObjectName(_fromUtf8("main_label"))
        self.horizontalLayout_3.addWidget(self.main_label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.nsn_search_edit = QtGui.QLineEdit(self.centralwidget)
        self.nsn_search_edit.setObjectName(_fromUtf8("nsn_search_edit"))
        self.verticalLayout_2.addWidget(self.nsn_search_edit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.pn_search_edit = QtGui.QLineEdit(self.centralwidget)
        self.pn_search_edit.setObjectName(_fromUtf8("pn_search_edit"))
        self.verticalLayout_3.addWidget(self.pn_search_edit)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_4.addWidget(self.label_4)
        self.desc_search_edit = QtGui.QLineEdit(self.centralwidget)
        self.desc_search_edit.setObjectName(_fromUtf8("desc_search_edit"))
        self.verticalLayout_4.addWidget(self.desc_search_edit)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_5.addWidget(self.label_5)
        self.loc_search_edit = QtGui.QLineEdit(self.centralwidget)
        self.loc_search_edit.setObjectName(_fromUtf8("loc_search_edit"))
        self.verticalLayout_5.addWidget(self.loc_search_edit)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_6.addWidget(self.label_6)
        self.niin_search_edit = QtGui.QLineEdit(self.centralwidget)
        self.niin_search_edit.setObjectName(_fromUtf8("niin_search_edit"))
        self.verticalLayout_6.addWidget(self.niin_search_edit)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_7.addWidget(self.label_7)
        self.remarks_search_edit = QtGui.QLineEdit(self.centralwidget)
        self.remarks_search_edit.setObjectName(_fromUtf8("remarks_search_edit"))
        self.verticalLayout_7.addWidget(self.remarks_search_edit)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.search_button = QtGui.QPushButton(self.centralwidget)
        self.search_button.setObjectName(_fromUtf8("search_button"))
        self.horizontalLayout.addWidget(self.search_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_8.addWidget(self.label_8)
        self.nsn_edit = QtGui.QLineEdit(self.centralwidget)
        self.nsn_edit.setObjectName(_fromUtf8("nsn_edit"))
        self.verticalLayout_8.addWidget(self.nsn_edit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_9.addWidget(self.label_9)
        self.pn_edit = QtGui.QLineEdit(self.centralwidget)
        self.pn_edit.setObjectName(_fromUtf8("pn_edit"))
        self.verticalLayout_9.addWidget(self.pn_edit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_10.addWidget(self.label_10)
        self.desc_edit = QtGui.QLineEdit(self.centralwidget)
        self.desc_edit.setObjectName(_fromUtf8("desc_edit"))
        self.verticalLayout_10.addWidget(self.desc_edit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_11.addWidget(self.label_11)
        self.loc_edit = QtGui.QLineEdit(self.centralwidget)
        self.loc_edit.setObjectName(_fromUtf8("loc_edit"))
        self.verticalLayout_11.addWidget(self.loc_edit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_12.addWidget(self.label_12)
        self.niin_edit = QtGui.QLineEdit(self.centralwidget)
        self.niin_edit.setObjectName(_fromUtf8("niin_edit"))
        self.verticalLayout_12.addWidget(self.niin_edit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_13.addWidget(self.label_13)
        self.remarks_edit = QtGui.QLineEdit(self.centralwidget)
        self.remarks_edit.setObjectName(_fromUtf8("remarks_edit"))
        self.verticalLayout_13.addWidget(self.remarks_edit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.update_button = QtGui.QPushButton(self.centralwidget)
        self.update_button.setObjectName(_fromUtf8("update_button"))
        self.verticalLayout_14.addWidget(self.update_button)
        self.add_button = QtGui.QPushButton(self.centralwidget)
        self.add_button.setObjectName(_fromUtf8("add_button"))
        self.verticalLayout_14.addWidget(self.add_button)
        self.horizontalLayout_2.addLayout(self.verticalLayout_14)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.select_row_button = QtGui.QPushButton(self.centralwidget)
        self.select_row_button.setObjectName(_fromUtf8("select_row_button"))
        self.verticalLayout.addWidget(self.select_row_button)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMain = QtGui.QMenu(self.menubar)
        self.menuMain.setObjectName(_fromUtf8("menuMain"))
        MainWindow.setMenuBar(self.menubar)
        self.actionLUH = QtGui.QAction(MainWindow)
        self.actionLUH.setObjectName(_fromUtf8("actionLUH"))
        self.actionApache = QtGui.QAction(MainWindow)
        self.actionApache.setObjectName(_fromUtf8("actionApache"))
        self.menuMain.addAction(self.actionLUH)
        self.menuMain.addAction(self.actionApache)
        self.menubar.addAction(self.menuMain.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Benchstock", None))
        self.main_label.setText(_translate("MainWindow", "Apache", None))
        self.label_2.setText(_translate("MainWindow", "NSN", None))
        self.label_3.setText(_translate("MainWindow", "PN", None))
        self.label_4.setText(_translate("MainWindow", "Description", None))
        self.label_5.setText(_translate("MainWindow", "Location", None))
        self.label_6.setText(_translate("MainWindow", "NIIN", None))
        self.label_7.setText(_translate("MainWindow", "Remarks", None))
        self.search_button.setText(_translate("MainWindow", "Search", None))
        self.label_8.setText(_translate("MainWindow", "NSN", None))
        self.label_9.setText(_translate("MainWindow", "PN", None))
        self.label_10.setText(_translate("MainWindow", "Description", None))
        self.label_11.setText(_translate("MainWindow", "Location", None))
        self.label_12.setText(_translate("MainWindow", "NIIN", None))
        self.label_13.setText(_translate("MainWindow", "Remarks", None))
        self.update_button.setText(_translate("MainWindow", "Update", None))
        self.add_button.setText(_translate("MainWindow", "Add", None))
        self.select_row_button.setText(_translate("MainWindow", "Select Item", None))
        self.menuMain.setTitle(_translate("MainWindow", "Main", None))
        self.actionLUH.setText(_translate("MainWindow", "LUH", None))
        self.actionApache.setText(_translate("MainWindow", "Apache", None))

