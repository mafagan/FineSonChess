from client.room import roomWindow
from client.login import loginWindow
from client.game import gameWindow

__author__ = 'gzs2482'


class client(object):
    def __init__(self):
        self.loginShow()
        #self.roomShow()
        pass

    def loginShow(self):
        self.loginWin = loginWindow()
        self.loginWin.pushButton.clicked.connect(self.login)

    def login(self):
        self.loginWin.window.close()
        self.roomShow()

    def roomShow(self):
        self.roomWin = roomWindow()