# база
import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication

# окно
import win


class MaxVid(QtWidgets.QMainWindow, win.Ui_MainWindow, QDialog):
    def __init__(self):
        super(MaxVid, self).__init__()
        self.setupUi(self)

    def draw(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = win()
    w.show()
    w.main_window()
    sys.exit(app.exec())
