# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.main_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.main_label.setFont(font)
        self.main_label.setObjectName("main_label")
        self.horizontalLayout_3.addWidget(self.main_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.nsn_search_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.nsn_search_edit.setObjectName("nsn_search_edit")
        self.verticalLayout_2.addWidget(self.nsn_search_edit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.pn_search_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.pn_search_edit.setObjectName("pn_search_edit")
        self.verticalLayout_3.addWidget(self.pn_search_edit)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.desc_search_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.desc_search_edit.setObjectName("desc_search_edit")
        self.verticalLayout_4.addWidget(self.desc_search_edit)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.loc_search_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.loc_search_edit.setObjectName("loc_search_edit")
        self.verticalLayout_5.addWidget(self.loc_search_edit)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.niin_search_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.niin_search_edit.setObjectName("niin_search_edit")
        self.verticalLayout_6.addWidget(self.niin_search_edit)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.remarks_search_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.remarks_search_edit.setObjectName("remarks_search_edit")
        self.verticalLayout_7.addWidget(self.remarks_search_edit)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setObjectName("search_button")
        self.horizontalLayout.addWidget(self.search_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.nsn_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.nsn_edit.setObjectName("nsn_edit")
        self.verticalLayout_8.addWidget(self.nsn_edit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_9.addWidget(self.label_9)
        self.pn_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.pn_edit.setObjectName("pn_edit")
        self.verticalLayout_9.addWidget(self.pn_edit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_10.addWidget(self.label_10)
        self.desc_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.desc_edit.setObjectName("desc_edit")
        self.verticalLayout_10.addWidget(self.desc_edit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_11.addWidget(self.label_11)
        self.loc_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.loc_edit.setObjectName("loc_edit")
        self.verticalLayout_11.addWidget(self.loc_edit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_12.addWidget(self.label_12)
        self.niin_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.niin_edit.setObjectName("niin_edit")
        self.verticalLayout_12.addWidget(self.niin_edit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_13.addWidget(self.label_13)
        self.remarks_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.remarks_edit.setObjectName("remarks_edit")
        self.verticalLayout_13.addWidget(self.remarks_edit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.update_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_button.setObjectName("update_button")
        self.verticalLayout_14.addWidget(self.update_button)
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setObjectName("add_button")
        self.verticalLayout_14.addWidget(self.add_button)
        self.horizontalLayout_2.addLayout(self.verticalLayout_14)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.select_row_button = QtWidgets.QPushButton(self.centralwidget)
        self.select_row_button.setObjectName("select_row_button")
        self.verticalLayout.addWidget(self.select_row_button)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        MainWindow.setMenuBar(self.menubar)
        self.actionLUH = QtWidgets.QAction(MainWindow)
        self.actionLUH.setObjectName("actionLUH")
        self.actionApache = QtWidgets.QAction(MainWindow)
        self.actionApache.setObjectName("actionApache")
        self.menuMain.addAction(self.actionLUH)
        self.menuMain.addAction(self.actionApache)
        self.menubar.addAction(self.menuMain.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Benchstock"))
        self.main_label.setText(_translate("MainWindow", "Apache"))
        self.label_2.setText(_translate("MainWindow", "NSN"))
        self.label_3.setText(_translate("MainWindow", "PN"))
        self.label_4.setText(_translate("MainWindow", "Description"))
        self.label_5.setText(_translate("MainWindow", "Location"))
        self.label_6.setText(_translate("MainWindow", "NIIN"))
        self.label_7.setText(_translate("MainWindow", "Remarks"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.label_8.setText(_translate("MainWindow", "NSN"))
        self.label_9.setText(_translate("MainWindow", "PN"))
        self.label_10.setText(_translate("MainWindow", "Description"))
        self.label_11.setText(_translate("MainWindow", "Location"))
        self.label_12.setText(_translate("MainWindow", "NIIN"))
        self.label_13.setText(_translate("MainWindow", "Remarks"))
        self.update_button.setText(_translate("MainWindow", "Update"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.select_row_button.setText(_translate("MainWindow", "Select Item"))
        self.menuMain.setTitle(_translate("MainWindow", "Main"))
        self.actionLUH.setText(_translate("MainWindow", "LUH"))
        self.actionApache.setText(_translate("MainWindow", "Apache"))

