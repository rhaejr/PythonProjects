import sqlite3
from PyQt4 import Qt
from gui_track import Ui_MainWindow

conn = sqlite3.connect('track.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS track(
activity TEXT,
blue_pc    TEXT ,
red_pc    TEXT ,
yellow_pc    TEXT ,
green_pc    TEXT ,
blue_weight    TEXT ,
red_weight    TEXT ,
yellow_weight    TEXT ,
green_weight    TEXT ,
blue_tab    TEXT ,
red_tab    TEXT ,
yellow_tab    TEXT ,
green_tab    TEXT ,
date TEXT,
run TEXT
);''')

cur.execute('''create table if not exists activities(
activity text,
acft text
)''')

class Main(Qt.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # initialized variables
        self.activated = ''
        self.acft_activated = ''
        self.acft_list = ['111', '161', '087', '215', '227', '030', '040', '041', '137', '138', '139', '140', '238']


        self.defaults()




        # Connections
        self.ui.add_changes_btn.clicked.connect(self.add_changes)
        self.ui.add_activity_btn.clicked.connect(self.add_activity)
        self.ui.activity_comboBox.activated[str].connect(self.activated_activity)
        self.ui.acft_comboBox.activated[str].connect(self.activated_acft)

    def defaults(self):
        self.ui.dateEdit.setDate(Qt.QDate.currentDate())
        self.fill_activity()
        self.fill_acft()
        self.fill_tree()

    def activated_activity(self, activated):
        self.activated = activated
        print(self.activated)

    def activated_acft(self, acft_activated):
        self.acft_activated = acft_activated

    def current_text(self):
        current = (self.activated,
                   self.ui.blue_pc_edit.text(),
                   self.ui.red_pc_edit.text(),
                   self.ui.yellow_pc_edit.text(),
                   self.ui.green_pc_edit.text(),
                   self.ui.blue_weight_edit.text(),
                   self.ui.red_weight_edit.text(),
                   self.ui.yellow_weight_edit.text(),
                   self.ui.green_weight_edit.text(),
                   self.ui.blue_tab_edit.text(),
                   self.ui.red_tab_edit.text(),
                   self.ui.yellow_tab_edit.text(),
                   self.ui.green_tab_edit.text(),
                   self.ui.dateEdit.date().toPyDate().strftime("%d-%b-%Y"),
                   self.ui.run_counter.text()
                   )

        return current
    def add_changes(self):

        cur.execute('insert into track values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', self.current_text())
        print(self.current_text())

    def add_activity(self):

        activity = self.ui.activity_edit.text()

        if self.acft_activated != '':
            cur.execute("INSERT INTO activities VALUES('{}', '{}')".format(activity,self.acft_activated))
            conn.commit()
            self.ui.activity_comboBox.clear()
            self.fill_activity()

    def fill_activity(self):
        self.ui.activity_comboBox.clear()
        activities = []
        cur.execute('''SELECT activity FROM activities''')
        rows = cur.fetchall()
        for row in rows:
            activities.append(row[0])
        self.ui.activity_comboBox.addItem('...')
        self.ui.activity_comboBox.addItems(activities)

    def fill_acft(self):
        self.ui.acft_comboBox.clear()
        self.ui.acft_comboBox.addItem('...')
        self.ui.acft_comboBox.addItems(self.acft_list)

    def fill_tree(self):
        tree_dict = {}
        for i in self.acft_list:
            rows = cur.execute('select activity from activities where acft="{}"'.format(i)).fetchall()
            tree_dict[i] = rows
        # for key in tree_dict.keys():
        #     tree_item = Qt.QTreeWidgetItem()
        #
        #     for item in tree_dict[key]:

        print(tree_dict)




def main():
    app = Qt.QApplication([])
    main_view = Main()
    main_view.show()

    app.exec_()


if __name__ == "__main__":
    main()
    conn.close()