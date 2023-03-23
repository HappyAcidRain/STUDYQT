# база
import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QGraphicsDropShadowEffect

# окно
import MainWin

# чат гпт даёт ответы
import GPT as G


class MainWindow(QtWidgets.QMainWindow, MainWin.Ui_MainWindow, QDialog):
    # конструктор
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # настройки окна
        self.setWindowTitle("ChatieThing")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setOffset(2)
        self.btn_commit.setGraphicsEffect(shadow)

        # кнопушка
        self.btn_commit.clicked.connect(self.getAnswer)

    def getAnswer(self):
        question = str(self.te_userEnter.toPlainText())
        answer = str(G.askGpt(question))

        self.te_gptAnswer.setText(answer)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    w = QtWidgets.QStackedWidget()
    w.addWidget(mainWindow)
    w.show()
    sys.exit(app.exec())
