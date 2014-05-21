#!/usr/bin/python
#-*-coding:utf-8-*-
__author__ = 'gzs2482'
from PyQt4.QtGui import QMainWindow
from PyQt4 import QtCore
from UI.loginWondow import LoginWin
from PyQt4.QtGui import QPalette, QColor
from PyQt4 import Qt
class loginWindow(LoginWin):
    def __init__(self):
        self.setupUI()

    def setupUI(self):
        self.window = QMainWindow()
        qss = QtCore.QFile("qss/loginWindow.qss")
        qss.open(QtCore.QFile.ReadOnly)
        qssStr = QtCore.QLatin1String(qss.readAll())
        self.setupUi(self.window)
        #self.pushButton.click.connect()
        self.window.show()
        self.window.setStyleSheet(qssStr)
        #self.pushButton.clicked.connect(self.clo)

    def clo(self):
        self.window.close()