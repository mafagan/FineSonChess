#!/usr/bin/python
#-*-coding:utf-8-*-
__author__ = 'gzs2482'

import socket
from time import ctime

host = ''
port = 23456
bufsiz = 1024
ADDR = (host, port)

tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

try:
    while True:

        print('wait for connection')
        tcpSerSock, addr = tcpSerSock.accept()
        print('...connect from ', addr)

        while True:
            data = tcpSerSock.recv(bufsiz)

            if not data:
                break
            tcpSerSock.send('[%s] %s' % (ctime(), data))
except BaseException, e:
    tcpSerSock.close()