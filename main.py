import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication
import pageOne
import pageTwo


class MainWindow(QtWidgets.QMainWindow, pageOne.Ui_MainWindow, QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.btn_next.clicked.connect(self.nextPage)

    def nextPage(self):
        screen2 = Screen2()
        w.addWidget(screen2)
        w.setCurrentIndex(w.currentIndex()+1)


class Screen2(QtWidgets.QMainWindow, pageTwo.Ui_MainWindow, QDialog):
    def __init__(self):
        super(Screen2, self).__init__()
        self.setupUi(self)

        self.btn_back.clicked.connect(self.pervPage)

    def pervPage(self):
        w.setCurrentIndex(w.currentIndex()-1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    w = QtWidgets.QStackedWidget()
    w.addWidget(mainWindow)

    w.setFixedHeight(93)
    w.setFixedWidth(186)

    w.show()
    sys.exit(app.exec())
    