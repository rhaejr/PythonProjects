import sys, sqlite3, os
from mytools import calculate_checksum, label_maker
from PyQt4 import Qt
from gui import Ui_MainWindow
from ipc import Ui_Dialog

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

        self.model = Qt.QStringListModel()
        self.word_list = set()
        self.auto_completer()
        self.completer = Qt.QCompleter()
        self.completer.setCaseSensitivity(False)
        self.completer.setModel(self.model)
        self.ui.search_edit.setCompleter(self.completer)

        self.ui.search_edit.returnPressed.connect(self.search)
        self.ui.actionLUH.triggered.connect(self.luh_action)
        self.ui.actionApache.triggered.connect(self.apache_action)
        self.ui.add_button.clicked.connect(self.add_item)
        self.ui.search_button.clicked.connect(self.search)
        self.ui.reset_table_button.clicked.connect(self.reset_table)
        self.ui.update_button.clicked.connect(self.update_db)
        self.ui.tableWidget.doubleClicked.connect(self.load_from_table)
        self.ui.print_label_btn.clicked.connect(self.print_labels)
        self.ui.add_label_btn.clicked.connect(self.add_label)
        self.ui.reset_labels_btn.clicked.connect(self.reset_labels)
        self.ui.ipc_button.clicked.connect(self.open_ipc)

        self.ui.tableWidget.setEditTriggers(Qt.QAbstractItemView.NoEditTriggers)
        self.header = self.ui.tableWidget.horizontalHeader()
        self.header.setStretchLastSection(True)

    def auto_completer(self):
        cur.execute('select nsn, pn, desc, remarks, location, niin, barcode from benchstock where acft="{}"'.format(self.acft))
        for i in cur.fetchall():
            for j in i:
                self.word_list.add(j)

        self.model.setStringList(list(self.word_list))



    def reset_table(self):
        if self.acft == 'luh':
            self.luh_action()
        if self.acft == 'apache':
            self.apache_action()

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
        # ac = {'luh': '720', 'apache': '640'}
        # code = '{}{}'.format(ac[self.acft], fields[0][-9:])
        # barcode = '{}{}'.format(str(code), str(calculate_checksum(code)))
        check = [fields[0], fields[1], fields[5]]
        matches = False
        for f in check:
            if f[0] != '':
                # not checking for location for now
                cur.execute('select * from benchstock where {} = "{}"'.format(f[1], f[0]))
                if len(cur.fetchall()) > 0:
                    print(f[1])
                    matches = True
        if matches == False:

            cur.execute('insert into benchstock values(?,?,?,?,?,?,?,?,?)', (fields[0][0], fields[1][0], fields[2][0],
                                                                                 fields[3][0], fields[4][0], fields[5][0],
                                                                                  self.acft,'', 'false'))
            conn.commit()
            if self.acft == 'apache':
                self.apache_action()
                self.search()
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

    def print_labels(self):
        label_maker(self.acft)

    def add_label(self):
        rowID = self.ui.tableWidget.currentRow()
        nsn = self.ui.tableWidget.item(rowID, 0).text()
        cur.execute('update benchstock set label="true" where nsn="{}"'.format(nsn))
        conn.commit()

    def reset_labels(self):
        cur.execute('update benchstock set label="false" where acft="{}"'.format(self.acft))
        conn.commit()

    def search(self):
        self.ui.tableWidget.clear()
        fields = ['nsn', 'pn', 'desc', 'remarks', 'location', 'niin', 'barcode']
        rows = set()
        for i in fields:
            if i[0] != '':
                select = cur.execute(
                    'select nsn, pn, niin, location, desc, remarks from benchstock where acft="{}" and {} like "%{}%"'.format(self.acft, i, self.ui.search_edit.text())).fetchall()
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
        self.ui.label_7.setText('Search: {}'.format(self.ui.search_edit.text()))
        self.ui.search_edit.setText('')

    def open_ipc(self):
        ipc = IPC()
        res = ipc.exec()
        if res:
            print('test')



class IPC(Qt.QDialog):
    def __init__(self, parent=None):
        Qt.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setGeometry(50,50,1750,800)
        self.ui.label.setPixmap(Qt.QPixmap('apache tm/blade-1.jpg'))
        self.pages_dic = {}
        self.pages = self.make_page_dic(os.listdir('apache tm'))
        print(self.pages_dic)

        self.ui.pages_combo.addItems(self.pages)
        self.ui.pages_combo.activated[str].connect(self.change_page)


    def make_page_dic(self, pages):
        temp_list = []
        for p in pages:
            fig = p[-10:-7]
            items = p[-6:-4]
            ext = p[-4:]

            self.pages_dic[p[:-4]] = (fig, items,ext)
            temp_list.append(p[:-4])

        return temp_list



    def change_page(self,page):

        self.ui.label.setPixmap(Qt.QPixmap('apache tm/{}'.format(page)))
        # self.search_button = QtGui.QPushButton(self.tab_2)
        # self.search_button.setObjectName(_fromUtf8("search_button"))
        # self.horizontalLayout.addWidget(self.search_button)


def main():
    app = Qt.QApplication(sys.argv)
    main_view = Main()
    main_view.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


