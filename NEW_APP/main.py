import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication

import maxVid
import minVid


class MaxVid(QtWidgets.QMainWindow, maxVid.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def main_window(self):
        self.btn_slim.clicked.connect(self.nextVid())

    def nextVid(self):
        screen2 = MinVid()
        w.addWidget(screen2)
        w.setCurrentIndex(w.currentIndex()+1)


class MinVid(QtWidgets.QMainWindow, minVid.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MaxVid()
    w.show()
    w.main_window()
    sys.exit(app.exec_())
