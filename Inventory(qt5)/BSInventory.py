import sqlite3

from PyQt5 import Qt
from gui import Ui_MainWindow

conn = sqlite3.connect('inventory.db')
cur = conn.cursor()

# nsn, pn, desc, remarks, location, niin, acft


class Main(Qt.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.apache_action()
        self.acft = 'apache'
        self.ui.actionLUH.triggered.connect(self.luh_action)
        self.ui.actionApache.triggered.connect(self.apache_action)
        self.ui.add_button.clicked.connect(self.add_item)
        self.ui.search_button.clicked.connect(self.search)
        self.ui.select_row_button.clicked.connect(self.load_from_table)
        self.ui.update_button.clicked.connect(self.update_db)
        self.ui.tableWidget.doubleClicked.connect(self.load_from_table)
        self.ui.tableWidget.setEditTriggers(Qt.QAbstractItemView.NoEditTriggers)
        self.header = self.ui.tableWidget.horizontalHeader()
        self.header.setStretchLastSection(True)



    def luh_action(self):
        self.ui.main_label.setText('LUH')
        self.acft = 'luh'
        self.ui.tableWidget.clear()
        rows = cur.execute(
            'select pn, location, desc, remarks from benchstock where acft="luh"').fetchall()
        self.ui.tableWidget.setRowCount(len(rows))
        self.ui.tableWidget.setColumnCount(4)
        row_num = 0
        for row in rows:
            column = 0
            for cell in row:
                self.ui.tableWidget.setItem(row_num, column, Qt.QTableWidgetItem(str(cell)))
                column += 1
            row_num += 1

        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['PN', 'LOCATION', 'DESCRIPTION', 'REMARKS'])
        self.ui.tableWidget.resizeColumnsToContents()


    def apache_action(self):
        self.ui.main_label.setText('Apache')
        self.acft = 'apache'
        self.ui.tableWidget.clear()
        rows = cur.execute('select nsn, pn, niin, location, desc, remarks from benchstock where acft="apache"').fetchall()
        self.ui.tableWidget.setRowCount(len(rows))
        self.ui.tableWidget.setColumnCount(6)
        row_num = 0
        for row in rows:
            column = 0
            for cell in row:
                self.ui.tableWidget.setItem(row_num, column, Qt.QTableWidgetItem(str(cell)))
                column += 1
            row_num += 1

        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['NSN', 'PN', 'NIIN', 'LOCATION', 'DESCRIPTION', 'REMARKS'])
        self.ui.tableWidget.resizeColumnsToContents()





    # nsn, pn, desc, remarks, location, niin, acft
    def add_item(self):
        fields = [[self.ui.nsn_edit.text().upper(), 'nsn'],
                  [self.ui.pn_edit.text().upper(), 'pn'],
                  [self.ui.desc_edit.text().upper(), 'desc'],
                  [self.ui.remarks_edit.text().upper(), 'remarks'],
                  [self.ui.loc_edit.text().upper().upper(), 'location'],
                  [self.ui.niin_edit.text().upper(), 'niin']]
        matches = False
        for f in fields:
            if f[0] != '':
                cur.execute('select * from benchstock where {} = "{}"'.format(f[1], f[0]))
                if len(cur.fetchall()) > 0:
                    matches = True
        if matches == False:

            cur.execute('insert into benchstock values(?,?,?,?,?,?,?)', (fields[0][0], fields[1][0], fields[2][0],
                                                                                 fields[3][0], fields[4][0], fields[5][0],
                                                                                 self.acft))
            conn.commit()
            if self.acft == 'apache':
                self.apache_action()
            else:
                self.luh_action()

    def load_from_table(self):
        rowID = self.ui.tableWidget.currentRow()
        items = []

        if len(self.ui.tableWidget.selectedItems()) == self.ui.tableWidget.columnCount():

            items = self.ui.tableWidget.selectedItems()
            for n in range(len(items)):
                items[n] = items[n].text()
        else:
            for i in range(self.ui.tableWidget.columnCount()):
                items.append(self.ui.tableWidget.item(rowID, i).text())
        self.ui.nsn_edit.setText(items[0])
        self.ui.pn_edit.setText(items[1])
        self.ui.niin_edit.setText(items[2])
        self.ui.loc_edit.setText(items[3])
        self.ui.desc_edit.setText(items[4])
        self.ui.remarks_edit.setText(items[5])

    def update_db(self):
        fields = [[self.ui.nsn_edit.text(), 'nsn'],
                  [self.ui.niin_edit.text(), 'niin'],
                  [self.ui.pn_edit.text(), 'pn'],
                  [self.ui.desc_edit.text(), 'desc'],
                  [self.ui.loc_edit.text(), 'location'],
                  [self.ui.remarks_edit.text(), 'remarks']]
        cur.execute('update benchstock set nsn="{}", niin="{}", pn="{}", desc="{}", location="{}", remarks="{}" where nsn="{}"'.format(
            fields[0][0], fields[1][0], fields[2][0], fields[3][0], fields[4][0], fields[5][0], fields[0][0]).upper())

        conn.commit()
        if self.acft == 'apache':
            self.apache_action()
        else:
            self.luh_action()




    def search(self):
        self.ui.tableWidget.clear()
        fields = [[self.ui.nsn_search_edit.text(), 'nsn'],
                  [self.ui.niin_search_edit.text(), 'niin'],
                  [self.ui.pn_search_edit.text(), 'pn'],
                  [self.ui.desc_search_edit.text(), 'desc'],
                  [self.ui.loc_search_edit.text(), 'location'],
                  [self.ui.remarks_search_edit.text(), 'remarks']]
        rows = set()
        for i in fields:
            if i[0] != '':
                select = cur.execute(
                    'select nsn, pn, niin, location, desc, remarks from benchstock where acft="{}" and {} like "%{}%"'.format(self.acft, i[1], i[0])).fetchall()
                if len(select) != 0:
                    rows.update(select)
        self.ui.tableWidget.setRowCount(len(rows))
        self.ui.tableWidget.setColumnCount(6)
        row_num = 0
        for row in rows:
            column = 0
            for cell in row:
                self.ui.tableWidget.setItem(row_num, column, Qt.QTableWidgetItem(str(cell)))
                column += 1
            row_num += 1

        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['nsn', 'pn', 'niin', 'location', 'description', 'remarks'])



def main():
    app = Qt.QApplication([])
    main_view = Main()
    main_view.show()

    app.exec_()


if __name__ == "__main__":
    main()


