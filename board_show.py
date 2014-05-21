#!/usr/bin/python
#-*-coding:utf-8-*-
from PyQt4.QtGui import QLabel, QPixmap, QPainter
import os
__author__ = 'gzs2482'

class Board(QLabel):
    def __init__(self, layoutWidget):
        QLabel.__init__(self, layoutWidget)
        self.resize(490,490)

        #建立棋盘
        self.board = QPixmap()
        self.board.load("img\\board.png")
        self.setPixmap(self.board)

        self.whiteChess = QPixmap()
        self.whiteChess.load("img\\white.png")

        self.blackChess = QPixmap()
        self.blackChess.load("img\\black.png")

        self.boardArray = [[0 for col in range(15)] for row in range(15)]
    def mousePressEvent(self, QMouseEvent):
        self.setPixmap(self.board)
        x = None
        if ((QMouseEvent.x() - 20) % 32) < 16:
            x = (QMouseEvent.x() - 20) / 32
        else:
            x = ((QMouseEvent.x() - 20) / 32 + 1)

        y = None
        if ((QMouseEvent.y() - 20) % 32) < 16:
            y = (QMouseEvent.y() - 20) / 32
        else:
            y = ((QMouseEvent.y() - 20) / 32 + 1)

        if (x >= 15) | (y >= 15):
            return

        if self.boardArray[x][y] == 1:
            self.boardArray[x][y] = 0
        else:
            self.boardArray[x][y] = 1

        self.update()
    def paintEvent(self, QPaintEvent):
        QLabel.paintEvent(self, QPaintEvent)
        painter = QPainter(self)

        for i in range(15):
            for j in range(15):
                if self.boardArray[i][j] == 1:
                    painter.drawPixmap(i * 32 + 5, j * 32 + 5, self.whiteChess)

    def setBoardImg(self):
        self.setPixmap(self.board)

if __name__ == '__main__':
    pass