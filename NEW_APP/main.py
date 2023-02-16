import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication

# окошки
import maxVid
import minVid

# фетчим погоду
from weather import getWeather


# большое окно
class MaxVid(QtWidgets.QMainWindow, maxVid.Ui_MainWindow, QDialog):
    def __init__(self):
        super(MaxVid, self).__init__()
        self.setupUi(self)

        # кнопка смены вида
        self.btn_slim.clicked.connect(self.nextVid)

        # получаем погоду
        city = self.le_city.text()

        weather = getWeather(city)

        self.lbl_temp.setText(int(weather[0]))

    # возврат на маленькое окно
    def nextVid(self):
        screen2 = MinVid()
        w.setFixedHeight(150)
        w.setFixedWidth(338)
        w.addWidget(screen2)
        w.setCurrentIndex(w.currentIndex()+1)


# маленькое окно
class MinVid(QtWidgets.QMainWindow, minVid.Ui_MainWindow, QDialog):
    def __init__(self):
        super(MinVid, self).__init__()
        self.setupUi(self)

        # кнопка смены вида
        self.btn_max.clicked.connect(self.pervPage)

    # возврат на большое окно
    def pervPage(self):
        w.setFixedHeight(260)
        w.setFixedWidth(338)
        w.setCurrentIndex(w.currentIndex() - 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MaxVid()
    w = QtWidgets.QStackedWidget()
    w.addWidget(mainWindow)

    w.show()
    sys.exit(app.exec())
