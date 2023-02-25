# база
import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie, QRegion
from PyQt6.QtCore import Qt

# гант
import matplotlib.pyplot as plt

# окно
import win


class MainWin(QtWidgets.QMainWindow, win.Ui_MainWindow, QDialog):
    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi(self)

        self.btn_commit.clicked.connect(lambda: self. startGif())

        self.movie = QMovie("roblox-baller.gif")
        self.lbl_view.setMovie(self.movie)

    # animation gif start
    def startGif(self):
        self.movie.start()


    def draw(self):

        # Declaring a figure "gnt"
        fig, gnt = plt.subplots()

        # Setting Y-axis limits
        gnt.set_ylim(0, 80)

        # Setting X-axis limits
        gnt.set_xlim(0, 62)

        # Setting labels for x-axis and y-axis
        gnt.set_xlabel('Даты')
        gnt.set_ylabel('Номера')

        # не работает
        # changing diamentionshe
        # gnt.set_figwidth(52)
        # gnt.set_figheight(20)

        # Setting ticks on x-axis
        gnt.set_xticks([2, 4, 6, 8, 10, 12, 14, 16,
                        18, 20, 22, 24, 26, 28, 30,
                        32, 34, 36, 38, 40, 42, 44,
                        46, 48, 50, 52, 54, 56, 58,
                        60, 62])

        # Labelling tickes of x-axis
        gnt.set_xticklabels(["2", "", "", "", "", "", "", "16",
                             "", "", "", "", "", "28", "", "1",
                             "", "", "", "", "", "15", "", "",
                             "", "", "", "", "", "31", ""])

        # Setting ticks on y-axis
        gnt.set_yticks([5, 15, 25, 35, 45, 55, 65, 75])

        # Labelling tickes of y-axis
        gnt.set_yticklabels(['1', '2 ', '3', '4', '5', '6', '7', '8'])

        # Setting graph attribute
        gnt.grid(True)

        def rum_calc(x):
            а = x * 10 - 10
            return а

        def ins_cust(start_time, end_time, room, color):

            duration = int(end_time) - int(start_time)
            row = rum_calc(room)

            # добавление в график данных
            gnt.broken_barh([(start_time, duration)], (row, 10), facecolors=f'tab:{color}')

        ins_cust(10, 31, 4, 'blue')

        ins_cust(25, 34, 6, 'orange')

        ins_cust(12, 41, 5, 'red')

        plt.savefig("gant.png")

        pixmap = QPixmap('gant.png')
        self.lbl_view.setPixmap(pixmap)

    def testDate(self):

        date = self.de_date.date()
        print(date)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWin()
    w.show()
    sys.exit(app.exec())
