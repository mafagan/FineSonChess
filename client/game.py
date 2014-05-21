#!/usr/bin/python
#-*-coding:utf-8-*-
__author__ = 'gzs2482'
from PyQt4.QtGui import QMainWindow
from PyQt4 import QtCore
from UI.gameWindow import GameWindow
from PyQt4.QtGui import QPalette, QColor
from PyQt4 import Qt

class gameWindow(GameWindow):
    def __init__(self):
        self.setupUI()

    def setupUI(self):
        self.window = QMainWindow()
        qss = QtCore.QFile("qss/gameWindow.qss")
        qss.open(QtCore.QFile.ReadOnly)
        qssStr = QtCore.QLatin1String(qss.readAll())
        self.setupUi(self.window)

        self.label.setPixmap(self.label.board)
        self.label_2.setText('')
        self.label_3.setText('')
        self.window.setStyleSheet(qssStr)
        self.window.show()