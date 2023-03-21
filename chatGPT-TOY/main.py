# база
import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication

# окно
import MainWin

# чат гпт даёт ответы
import GPT as G


class MainWindow(QtWidgets.QMainWindow, MainWin.Ui_MainWindow, QDialog):
    # конструктор
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # кнопушка
        self.btn_getAnswer.clicked.connect(self.GetDaFuckingAnswer)

    def GetDaFuckingAnswer(self):

        question = str(self.te_userEnter.toPlainText())
        answer = str(G.fuckGpt(question))

        self.le_gptAnswer.setText(answer)


# СТАРТУЕММММ!!!
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    w = QtWidgets.QStackedWidget()
    w.addWidget(mainWindow)
    w.show()
    sys.exit(app.exec())
