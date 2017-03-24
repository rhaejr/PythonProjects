import sys, sqlite3
from collections import OrderedDict
import datetime as dt


from PyQt4 import Qt
from PyQt4.uic import loadUi
from gui_tr import Ui_MainWindow
dt_format = "%H%M %d%b%y"
conn = sqlite3.connect('toolroom.db')
cur = conn.cursor()

# nsn, pn, desc, remarks, location, niin, acft


class Main(Qt.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.issue_to = ''
        self.acft = ''

        self.ui.setupUi(self)
        self.tool_list()
        self.fill_drop_down()
        self.fill_acft_dropdown()

        # self.ui.id_edit.returnPressed.connect(self.load_from_table)
        self.ui.return_btn.clicked.connect(self.return_tool)
        self.ui.acft_list.activated[str].connect(self.acft_select)
        self.ui.user_list.activated[str].connect(self.user_select)
        self.ui.issue_btn.clicked.connect(self.issue_tool)
        self.ui.add_user_btn.clicked.connect(self.add_user)
        self.ui.add.clicked.connect(self.add_item)
        self.ui.update.clicked.connect(self.update_db)
        self.ui.tableWidget.doubleClicked.connect(self.load_from_table)


        self.ui.tableWidget.setEditTriggers(Qt.QAbstractItemView.NoEditTriggers)
        self.header = self.ui.tableWidget.horizontalHeader()
        self.header.setStretchLastSection(True)

    def tool_list(self):
        self.ui.tableWidget.clear()
        rows = cur.execute(
            'select id, desc, location, issue, remarks from tools').fetchall()
        self.ui.tableWidget.setRowCount(len(rows))
        self.ui.tableWidget.setColumnCount(5)
        row_num = 0
        for row in rows:
            column = 0
            for cell in row:
                self.ui.tableWidget.setItem(row_num, column, Qt.QTableWidgetItem(str(cell)))
                column += 1
            row_num += 1

        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'NOMENCLATURE', 'LOCATION', 'ISSUE', 'REMARKS'])
        self.ui.tableWidget.resizeColumnsToContents()

    def add_item(self):
        fields = [[self.ui.id_edit.text().upper(), 'id'],
                  [self.ui.desc_edit.text().upper(), 'desc'],
                  [self.ui.loc_edit.text().upper().upper(), 'location'],
                  [self.ui.remarks_edit.text().upper(), 'remarks']]
        matches = False

        cur.execute('select * from tools where {} = "{}"'.format(fields[0][1], fields[0][0]))
        if len(cur.fetchall()) > 0:
            matches = True
        if matches == False:

            cur.execute('insert into tools values(?,?,?,?,"")',(fields[0][0], fields[1][0], fields[3][0], fields[2][0]))
            conn.commit()
        self.tool_list()

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
        self.ui.id_edit.setText(items[0])
        self.ui.loc_edit.setText(items[2])
        self.ui.desc_edit.setText(items[1])
        self.ui.remarks_edit.setText(items[4])

    def update_db(self):
        fields = [[self.ui.id_edit.text().upper(), 'id'],
                  [self.ui.desc_edit.text().upper(), 'desc'],
                  [self.ui.loc_edit.text().upper().upper(), 'location'],
                  [self.ui.remarks_edit.text().upper(), 'remarks']]
        cur.execute('update tools set desc="{}", location="{}", remarks="{}" where id="{}"'.format(
            fields[1][0], fields[2][0], fields[3][0], fields[0][0]).upper())

        conn.commit()
        self.tool_list()

    def fill_drop_down(self):
        cur.execute('''SELECT * FROM users''')
        rows = cur.fetchall()
        self.ui.user_list.addItem("Select user...")
        for row in rows:
            self.ui.user_list.addItem(row[0])

    def fill_acft_dropdown(self):
        acft_list = ['72030','72137','72138','72140','72040','72041','72238','72','087','227','215','161','111']
        self.ui.acft_list.addItem('')
        self.ui.acft_list.addItems(acft_list)

    def acft_select(self, text):
        self.acft = text

    def user_select(self, text):
        self.issue_to = text
        # cur.execute(
        #     "SELECT from_date, to_date,from_time,to_time,leave_type,remarks,signed,hours  FROM leave_forms WHERE ID=" + self.leave_form.ssn)
        # rows = cur.fetchall()
        # self.form_table.setRowCount(len(rows))
        # try:
        #     self.form_table.setColumnCount(len(rows[0]))
        # except IndexError:
        #     self.form_table.setColumnCount(11)
        # row_num = 0
        # for row in rows:
        #     column = 0
        #     for cell in row:
        #         self.form_table.setItem(row_num, column, Qt.QTableWidgetItem(str(cell)))
        #         column += 1
        #     row_num += 1
        # self.form_table.setHorizontalHeaderLabels(
        #     ['from date', 'to date', 'from time', 'to time', 'leave type', 'remarks', 'signed', 'hours'])

    def issue_tool(self):
        # self.ui.remarks_edit.setText(self.issue_to)
        check_out = dt.datetime.now().strftime(dt_format)
        print(self.issue_to)
        fields = [[self.ui.id_edit.text().upper(), 'id'],
                  [self.ui.desc_edit.text().upper(), 'desc'],
                  [self.ui.loc_edit.text().upper().upper(), 'location'],
                  [self.ui.remarks_edit.text().upper(), 'remarks']]
        cur.execute('select check_out, check_in from issues where id="{}"'.format(fields[0][0]))
        select = cur.fetchall()
        checked_in = True
        print(len(select))
        if len(select) != 0:
            print(1)
            for i in select:
                if i[0] != '':
                    print(2)
                    if i[1] == '':
                        checked_in = False
                        print(False)

        if checked_in:


            cur.execute('update tools set issue="{}", desc="{}", location="{}", remarks="{}" where id="{}"'.format(
                self.issue_to,fields[1][0], fields[2][0], fields[3][0], fields[0][0]).upper())
            cur.execute('insert into issues values(?,?,?,?,?,?)', (fields[0][0], '', check_out,  self.issue_to, self.acft, fields[3][0]))

        conn.commit()
        self.tool_list()

    def return_tool(self):
        check_in = dt.datetime.now().strftime(dt_format)
        acft = 'test'
        print(self.issue_to)
        fields = [[self.ui.id_edit.text().upper(), 'id'],
                  [self.ui.desc_edit.text().upper(), 'desc'],
                  [self.ui.loc_edit.text().upper().upper(), 'location'],
                  [self.ui.remarks_edit.text().upper(), 'remarks']]


        cur.execute('update issues set check_in="{}", remarks="{}" where id="{}" and check_in=""'.format(check_in, fields[3][0], fields[0][0]))
        cur.execute('update tools set issue="IN", remarks="{}" where id="{}"'.format(fields[3][0], fields[0][0]))

        conn.commit()
        self.tool_list()


    def add_user(self):

        first = self.ui.first_edit.text().capitalize()
        last = self.ui.last_edit.text().capitalize()


        try:
            cur.execute("INSERT INTO users VALUES('{}, {}')".format(last, first))
            conn.commit()
            self.ui.user_list.clear()
            self.fill_drop_down()
        except sqlite3.IntegrityError:
            self.update_user()

    def update_user(self):
        msg = Qt.QMessageBox()
        msg = Qt.QMessageBox.question(msg, "User already enrolled!",
                                         Qt.QMessageBox.Ok)


class Tool:
    def __init__(self, id_num, location, nomenclature, remarks='', issue=''):
        self.id = id_num
        self.location = location
        self.remarks = remarks
        self.issue = issue
        self.nomenclature = nomenclature




def main():
    app = Qt.QApplication(sys.argv)
    main_view = Main()
    main_view.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
