def load_from_table(self):
    rowID = self.ui.tableWidget.currentRow()
    items = []

    # if len(self.ui.tableWidget.selectedItems()) == self.ui.tableWidget.columnCount():
    #
    #     items = self.ui.tableWidget.selectedItems()
    #     for cell in items:
    #         cell = cell.text()
    # else:
    for i in range(self.ui.tableWidget.columnCount()):
        items.append(self.ui.tableWidget.itemAt(rowID, i).text())
        print((rowID, i))
    self.ui.nsn_edit.setText(items[0])
    self.ui.pn_edit.setText(items[1])
    self.ui.niin_edit.setText(items[2])
    self.ui.loc_edit.setText(items[3])
    self.ui.desc_edit.setText(items[4])
    self.ui.remarks_edit.setText(items[5])