#!/usr/bin/python
#-*-coding:utf-8-*-
__author__ = 'gzs2482'

from PyQt4.QtGui import QWidget, QPixmap, QLabel
from PyQt4.QtCore import QSize

class Desk(QLabel):
    def __init__(self, deskID):
        QLabel.__init__(self)
        self.ID = deskID
        self.setupUI()
        pass

    def setupUI(self):
        self.setFixedSize(QSize(120, 120))

        self.desk = QPixmap()
        self.desk.load("img\\desk.png")
        self.setPixmap(self.desk)


    def mousePressEvent(self, QMouseEvent):
        pass

