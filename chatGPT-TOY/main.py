# база
import sys
from PyQt6 import QtWidgets 
from PyQt6.QtWidgets import QDialog, QApplication, QGraphicsDropShadowEffect

# окно
import MainWin

# чат гпт даёт ответы
import GPT as G


class MainWindow(QtWidgets.QMainWindow, MainWin.Ui_MainWindow, QDialog):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        user_message = []
        bot_answer = []
        history_ = []

        # основные настройки окна
        # self.QMainWindow.setWindowTitle("ChatieThing")

        # косметические настрйоки окна 
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setOffset(2)
        self.btn_commit.setGraphicsEffect(shadow)
        self.te_gptAnswer.setGraphicsEffect(shadow)
        self.te_userEnter.setGraphicsEffect(shadow)

        # нажатие кнопушки и Enter 
        self.btn_commit.clicked.connect(self.get_answer)
        

    def get_answer(self):
        user_message = []
        bot_answer = []
        history_ = []

        question = str(self.te_userEnter.toPlainText())
        answer = str(G.askGpt(question))

        user_message.append(question)
        bot_answer.append(answer)

        for i in user_message and bot_answer:
            history_.append("Вы:" + user_message[i] + "чат-GPT:" + bot_answer[i] )
            self.te_gptAnswer.setText(history_)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MainWindow()
    m.show()
    sys.exit(app.exec())
