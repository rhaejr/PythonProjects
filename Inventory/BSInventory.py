import sys

from PyQt4 import Qt
from PyQt4.uic import loadUi


class Main(Qt.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = loadUi("gui.ui", self)





def main():
    app = Qt.QApplication(sys.argv)
    main_view = Main()
    main_view.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()