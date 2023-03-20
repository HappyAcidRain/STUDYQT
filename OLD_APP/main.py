from PyQt6 import QtWidgets
import sys
import subprocess
import mainWin
import setings
import sqlite3


class ConfPart(QtWidgets.QMainWindow, setings.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # подключаем кнопку
        self.btn_save.clicked.connect(self.save_data)
        self.btn_save.setText("Сохранить!")

        # пути в полях (placeholder'ы)

        # подключаемся к БД
        connect = sqlite3.connect("OLD_APP\conf.db")
        cursor = connect.cursor()

        # выборка данных (IDE_way)
        cursor.execute("SELECT IDE_way FROM settings WHERE rowid = 1")
        ide_way = str(cursor.fetchone())

        # выборка данных (browser_way)
        cursor.execute("SELECT browser_way FROM settings WHERE rowid = 1")
        browser_way = str(cursor.fetchone())

        # устанавливаем placeholder'ы
        self.le_IDEway.setPlaceholderText(ide_way)
        self.le_browserWay.setPlaceholderText(browser_way)

        # закрываем подключение к БД
        connect.close()

    # кнопка сохранения
    def save_data(self):
        # подключаемся к БД
        connect = sqlite3.connect("OLD_APP\conf.db")
        cursor = connect.cursor()

        # получение данных с полей ввода
        ide_way = self.le_IDEway.text()
        browser_way = self.le_browserWay.text()

        # запись в БД
        cursor.execute(f"UPDATE settings SET IDE_way = '{ide_way}' WHERE rowid = 1 ")
        cursor.execute(f"UPDATE settings SET browser_way = '{browser_way}' WHERE rowid = 1 ")
        connect.commit()

        connect.close()
        print("DATA SAVED !")


class MainPart(QtWidgets.QMainWindow, mainWin.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # основное окно
    def main_window(self):
        # кнопки
        self.btn_start.clicked.connect(self.start_app)
        self.btn_conf.clicked.connect(self.conf_window)

    # окно настроек
    def conf_window(self):
        self.config_window = ConfPart()
        self.config_window.show()

    # запуск приложений
    def start_app(self):
        # подключаемся к БД
        connect = sqlite3.connect("OLD_APP\conf.db")
        cursor = connect.cursor()

        # выборка данных (IDE_way)
        cursor.execute("SELECT IDE_way FROM settings WHERE rowid = 1")
        ide_way = cursor.fetchone()

        # выборка данных (browser_way)
        cursor.execute("SELECT browser_way FROM settings WHERE rowid = 1")
        browser_way = cursor.fetchone()

        # открываем приложения
        subprocess.Popen(ide_way)
        subprocess.Popen(browser_way)

        # закрываем подключение к БД
        connect.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainPart()
    w.show()
    w.main_window()
    sys.exit(app.exec_())
