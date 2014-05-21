#!/usr/bin/python
#-*-coding:utf-8-*-
from PyQt4.QtGui import QMainWindow, QHBoxLayout, QWidget
from board_show import Board

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        board = Board()
        self.setCentralWidget(board)
        self.setWindowTitle('FiveSonChess')