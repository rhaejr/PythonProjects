# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'history_gui.ui'
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
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ID_label = QtGui.QLabel(self.centralwidget)
        self.ID_label.setObjectName(_fromUtf8("ID_label"))
        self.horizontalLayout.addWidget(self.ID_label)
        self.nomenclature_label = QtGui.QLabel(self.centralwidget)
        self.nomenclature_label.setObjectName(_fromUtf8("nomenclature_label"))
        self.horizontalLayout.addWidget(self.nomenclature_label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.history_table = QtGui.QTableWidget(self.centralwidget)
        self.history_table.setObjectName(_fromUtf8("history_table"))
        self.history_table.setColumnCount(0)
        self.history_table.setRowCount(0)
        self.verticalLayout.addWidget(self.history_table)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.ID_label.setText(_translate("MainWindow", "TextLabel", None))
        self.nomenclature_label.setText(_translate("MainWindow", "TextLabel", None))

