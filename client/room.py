#!/usr/bin/python
#-*-coding:utf-8-*-
__author__ = 'gzs2482'
from PyQt4.QtGui import QMainWindow, QGridLayout, QWidget, \
    QListWidget, QLabel, QVBoxLayout, QTextEdit, QLineEdit, \
    QPushButton, QHBoxLayout
from UI.desk import Desk
from PyQt4 import QtCore

class roomWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUI()
        self.setSheet()



    def setupUI(self):
        self.desks = []

        for i in range(16):
            self.desks.append(Desk(i))

        #桌子显示布局
        self.deskLayout = QGridLayout()

        for i in range(16):
            self.deskLayout.addWidget(self.desks[i], i / 4, i % 4)

        #在线玩家列表布局
        self.onlineLabel = QLabel()
        #self.onlineLabel.setText(self.tr(u'在线玩家'))
        self.onlineList = QListWidget()

        self.onlineLayout = QVBoxLayout()
        self.onlineLayout.addWidget(self.onlineLabel)
        self.onlineLayout.addWidget(self.onlineList)

        #聊天窗口布局
        self.chatLabel = QLabel()
        #self.chatLabel.setText(self.tr(u'聊天室'))
        self.chatWindow = QTextEdit()
        self.chatLayout = QVBoxLayout()
        self.chatLayout.addWidget(self.chatLabel)
        self.chatLayout.addWidget(self.chatWindow)


        #发送信息窗口布局
        self.textInputWindow = QLineEdit()
        self.sendButton = QPushButton()
        #self.sendButton.setText(self.tr(u'发送'))
        self.sendLayout = QHBoxLayout()
        self.sendLayout.addWidget(self.textInputWindow)
        self.sendLayout.addWidget(self.sendButton)

        #右边信息显示布局
        self.rightInfoLayout = QVBoxLayout()
        self.rightInfoLayout.addLayout(self.onlineLayout)
        self.rightInfoLayout.addLayout(self.chatLayout)
        self.rightInfoLayout.addLayout(self.sendLayout)

        #主窗口布局
        self.mainLayout = QHBoxLayout()
        self.mainLayout.addLayout(self.deskLayout)
        self.mainLayout.addLayout(self.rightInfoLayout)

        tempWidget = QWidget()
        tempWidget.setLayout(self.mainLayout)

        self.setCentralWidget(tempWidget)
        self.show()

    def setSheet(self):
        qss = QtCore.QFile("qss/roomWindow.qss")
        qss.open(QtCore.QFile.ReadOnly)
        qssStr = QtCore.QLatin1String(qss.readAll())
        self.setStyleSheet(qssStr)