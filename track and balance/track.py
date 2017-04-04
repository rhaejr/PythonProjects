import sqlite3
from PyQt5 import Qt
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
        self.defaults()
        self.fill_activity()
        self.ui.add_changes_btn.clicked.connect(self.add_changes)
        self.ui.add_activity_btn.clicked.connect(self.add_activity)



    def defaults(self):
        self.ui.dateEdit.setDate(Qt.QDate.currentDate())
    def current_text(self):
        current = (self.ui.activity_edit.text(),
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

        try:
            cur.execute("INSERT INTO activities VALUES(?, '')", activity)
            conn.commit()
            self.ui.activity_comboBox.clear()
            self.fill_activity()
        except sqlite3.IntegrityError:
            print('fail')

    def fill_activity(self):
        activities = []
        cur.execute('''SELECT activity FROM activities''')
        rows = cur.fetchall()
        for row in rows:
            activities.append(row[0])
        self.ui.activity_comboBox.addItem('...')
        self.ui.activity_comboBox.addItems(activities)



def main():
    app = Qt.QApplication([])
    main_view = Main()
    main_view.show()

    app.exec_()


if __name__ == "__main__":
    main()