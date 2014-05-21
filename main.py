#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
from mainWindow_show import MainWindow
from PyQt4.QtGui import QApplication, QMainWindow
from PyQt4 import QtCore
from client.game import gameWindow
from client.login import loginWindow
from client.room import roomWindow
from client.clientMain import client
def clo():
    loginWin.window.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName('FiveSonChess')
    app.setQuitOnLastWindowClosed(True)

    Client = client()
    #gameWin = gameWindow()
    #roomWin = roomWindow()
    #window.show()

    sys.exit(app.exec_())


