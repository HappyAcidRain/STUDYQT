# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\а\Desktop\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(323, 118)
        MainWindow.setMinimumSize(QtCore.QSize(323, 118))
        MainWindow.setMaximumSize(QtCore.QSize(323, 118))
        MainWindow.setStyleSheet("QWidget{\n"
"    background: rgb(57, 57, 57);\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background: rgb(88, 94, 211);\n"
"    border: 2px solid rgb(0, 198, 216);\n"
"    border-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background:rgb(0, 170, 255);\n"
"    border: 2px solid rgb(0, 198, 216) ;\n"
"    border-radius: 15px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_conf = QtWidgets.QPushButton(self.centralwidget)
        self.btn_conf.setGeometry(QtCore.QRect(10, 80, 121, 31))
        self.btn_conf.setObjectName("btn_conf")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(140, 80, 171, 31))
        self.btn_start.setObjectName("btn_start")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_conf.setText(_translate("MainWindow", "Настройки"))
        self.btn_start.setText(_translate("MainWindow", "СТАРТ!"))
        self.label.setText(_translate("MainWindow", "Запуск разрабокти!"))
