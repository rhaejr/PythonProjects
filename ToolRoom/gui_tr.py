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
        MainWindow.resize(801, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_4.addWidget(self.label_2)
        self.desc_edit = QtGui.QLineEdit(self.tab)
        self.desc_edit.setObjectName(_fromUtf8("desc_edit"))
        self.verticalLayout_4.addWidget(self.desc_edit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_5.addWidget(self.label_3)
        self.id_edit = QtGui.QLineEdit(self.tab)
        self.id_edit.setObjectName(_fromUtf8("id_edit"))
        self.verticalLayout_5.addWidget(self.id_edit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_6.addWidget(self.label_4)
        self.loc_edit = QtGui.QLineEdit(self.tab)
        self.loc_edit.setObjectName(_fromUtf8("loc_edit"))
        self.verticalLayout_6.addWidget(self.loc_edit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_8.addWidget(self.label_6)
        self.remarks_edit = QtGui.QLineEdit(self.tab)
        self.remarks_edit.setObjectName(_fromUtf8("remarks_edit"))
        self.verticalLayout_8.addWidget(self.remarks_edit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_10.addWidget(self.label_8)
        self.acft_list = QtGui.QComboBox(self.tab)
        self.acft_list.setObjectName(_fromUtf8("acft_list"))
        self.verticalLayout_10.addWidget(self.acft_list)
        self.horizontalLayout_2.addLayout(self.verticalLayout_10)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_9.addWidget(self.label_7)
        self.user_list = QtGui.QComboBox(self.tab)
        self.user_list.setObjectName(_fromUtf8("user_list"))
        self.verticalLayout_9.addWidget(self.user_list)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.add = QtGui.QPushButton(self.tab)
        self.add.setObjectName(_fromUtf8("add"))
        self.horizontalLayout.addWidget(self.add)
        self.return_btn = QtGui.QPushButton(self.tab)
        self.return_btn.setObjectName(_fromUtf8("return_btn"))
        self.horizontalLayout.addWidget(self.return_btn)
        self.issue_btn = QtGui.QPushButton(self.tab)
        self.issue_btn.setObjectName(_fromUtf8("issue_btn"))
        self.horizontalLayout.addWidget(self.issue_btn)
        self.update = QtGui.QPushButton(self.tab)
        self.update.setObjectName(_fromUtf8("update"))
        self.horizontalLayout.addWidget(self.update)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_11.addLayout(self.verticalLayout_3)
        self.tableWidget = QtGui.QTableWidget(self.tab)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_11.addWidget(self.tableWidget)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.first_edit = QtGui.QLineEdit(self.tab)
        self.first_edit.setObjectName(_fromUtf8("first_edit"))
        self.verticalLayout.addWidget(self.first_edit)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_7.addWidget(self.label_5)
        self.last_edit = QtGui.QLineEdit(self.tab)
        self.last_edit.setObjectName(_fromUtf8("last_edit"))
        self.verticalLayout_7.addWidget(self.last_edit)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.add_user_btn = QtGui.QPushButton(self.tab)
        self.add_user_btn.setObjectName(_fromUtf8("add_user_btn"))
        self.horizontalLayout_3.addWidget(self.add_user_btn)
        self.verticalLayout_11.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.ID_label = QtGui.QLabel(self.tab_2)
        self.ID_label.setObjectName(_fromUtf8("ID_label"))
        self.horizontalLayout_4.addWidget(self.ID_label)
        self.nomenclature_label = QtGui.QLabel(self.tab_2)
        self.nomenclature_label.setObjectName(_fromUtf8("nomenclature_label"))
        self.horizontalLayout_4.addWidget(self.nomenclature_label)
        self.verticalLayout_12.addLayout(self.horizontalLayout_4)
        self.history_table = QtGui.QTableWidget(self.tab_2)
        self.history_table.setObjectName(_fromUtf8("history_table"))
        self.history_table.setColumnCount(0)
        self.history_table.setRowCount(0)
        self.verticalLayout_12.addWidget(self.history_table)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_2.setText(_translate("MainWindow", "Nomenclature", None))
        self.label_3.setText(_translate("MainWindow", "ID", None))
        self.label_4.setText(_translate("MainWindow", "Location", None))
        self.label_6.setText(_translate("MainWindow", "Remarks", None))
        self.label_8.setText(_translate("MainWindow", "ACFT:", None))
        self.label_7.setText(_translate("MainWindow", "Issue To:", None))
        self.add.setText(_translate("MainWindow", "ADD", None))
        self.return_btn.setText(_translate("MainWindow", "Return", None))
        self.issue_btn.setText(_translate("MainWindow", "Issue", None))
        self.update.setText(_translate("MainWindow", "UPDATE", None))
        self.label.setText(_translate("MainWindow", "First Name:", None))
        self.label_5.setText(_translate("MainWindow", "Last Name", None))
        self.add_user_btn.setText(_translate("MainWindow", "Add User", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.ID_label.setText(_translate("MainWindow", "TextLabel", None))
        self.nomenclature_label.setText(_translate("MainWindow", "TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))

