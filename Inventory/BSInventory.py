import sys, sqlite3

from PyQt4 import Qt
from PyQt4.uic import loadUi
from gui import Ui_MainWindow

conn = sqlite3.connect('inventory.db')
cur = conn.cursor()

class Main(Qt.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.actionLUH.triggered.connect(self.luh_action)
        self.actionApache.triggered.connect(self.apache_action)



    def luh_action(self):
        self.main_label.setText('LUH')


    def apache_action(self):
        self.main_label.setText('Apache')
        rows = cur.execute('select * from benchstock where acft="apache"').fetchall()
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(7)
        row_num = 0
        for row in rows:
            column = 0
            for cell in row:
                self.tableWidget.setItem(row_num, column, Qt.QTableWidgetItem(str(cell)))
                column += 1
            row_num += 1


def main():
    app = Qt.QApplication(sys.argv)
    main_view = Main()
    main_view.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()