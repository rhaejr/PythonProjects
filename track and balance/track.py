import sqlite3
from PyQt4 import Qt
from gui_track import Ui_MainWindow

conn = sqlite3.connect('track.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS track(
activity        TEXT,
acft            TEXT,
blue_pc         TEXT ,
red_pc          TEXT ,
yellow_pc       TEXT ,
green_pc        TEXT ,
blue_weight     TEXT ,
red_weight      TEXT ,
yellow_weight   TEXT ,
green_weight    TEXT ,
blue_tab        TEXT ,
red_tab         TEXT ,
yellow_tab      TEXT ,
green_tab       TEXT ,
date            TEXT,
run             TEXT
);''')

cur.execute('''create table if not exists activities(
activity text,
acft text
)''')

colors = [
'blue pc', 'red pc', 'yellow pc', 'green pc', 'blue weight', 'red weight', 'yellow weight', 'green weight', 'blue tab',
    'red tab', 'yellow tab', 'green tab']

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
                   self.acft_activated,
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
        for i in range(len(current)):
            if 2 <= i <= 13 and current[i] != '':
                if '+' not in current[i] and '-' not in current[i]:
                    print(current[i])
                    msg = Qt.QMessageBox()
                    msg = Qt.QMessageBox.information(msg,'Message',"Need '+' or '-' in each adjustment", Qt.QMessageBox.Ok)

                    return None

        return current
    def add_changes(self):
        if self.acft_activated != '':
            if self.current_text():
                cur.execute('insert into track values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', self.current_text())
                print(self.current_text())
                conn.commit()

    def add_activity(self):

        activity = self.ui.activity_edit.text()

        if self.acft_activated != '':
            cur.execute("INSERT INTO activities VALUES('{}', '{}')".format(activity,self.acft_activated))
            conn.commit()
            self.ui.activity_comboBox.clear()
            self.fill_activity()
            self.fill_tree()


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

    def create_item(self, text, parent, index):
        after = None

        if index != 0:
            after = self.childAt(parent, index - 1)

        if parent is not None:
            item = Qt.QTreeWidgetItem(parent, after)
        else:
            item = Qt.QTreeWidgetItem(self, after)

        item.setText(0, text)
        return item

    def fill_tree(self):
        tree_list = []
        test = Qt.QTreeWidgetItem(self.ui.history_tree)
        test.setText(0,'test')
        test1 = Qt.QTreeWidgetItem(test)
        test1.setText(0, 'test')
        for i in range(len(self.acft_list)):
            acft_level = self.create_item(self.acft_list[i],self.ui.history_tree,0)
            activity = cur.execute('select activity from activities where acft="{}"'.format(self.acft_list[i])).fetchall()
            # print(activity)
            for j in range(len(activity)):
                activity_level = self.create_item(activity[j][0], acft_level, 0)
                runs = cur.execute('select run from track  where activity="{}" and acft="{}"'.format(activity[j][0], self.acft_list[i])).fetchall()
                print(runs)
                for run in runs:
                    run_level = self.create_item(str(run[0]), activity_level,0)

                    adjustments = cur.execute('''select blue_pc, red_pc, yellow_pc, green_pc, blue_weight, red_weight,
                                        yellow_weight, green_weight, blue_tab, red_tab, yellow_tab, green_tab
                                        from track where activity="{}" and acft="{}" and run="{}"
                                         '''.format(activity[j][0], self.acft_list[i], str(run[0]))).fetchall()
                    print(adjustments)
                    modifier = ''
                    for adjust in range(len(adjustments[0])):
                        print(adjust)
                        if adjustments[0][adjust] != '':
                            if 'pc' in colors[adjust]:
                                modifier = 'flats'
                            elif 'weight' in colors[adjust]:
                                modifier = 'grams'
                            elif 'tab' in colors[adjust]:
                                modifier = 'mm'
                            adjustment = '{}: {} {}'.format(colors[adjust], adjustments[0][adjust], modifier)
                            self.create_item(adjustment, run_level, 0)










def main():
    app = Qt.QApplication([])
    main_view = Main()
    main_view.show()

    app.exec_()


if __name__ == "__main__":
    main()
    conn.close()