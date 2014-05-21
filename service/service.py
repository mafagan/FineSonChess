#!/usr/bin/python
#-*-coding:utf-8-*-
__author__ = 'Winterma'

class service(object):
    def __init__(self, sid = 0):
        self.service_id = sid
        self.__command_map = {}

    def handle(self, msg, owner):
        cid = msg.cid

        if not cid in self.__command_map:
            raise Exception("bad command %s"%cid)
        f = self.__command_map[cid]
        return f(msg, owner)

    def registsr(self, cid, function):
        self.__command_map[cid] = function

    def registers(self, commandDict):
        self.__command_map = {}
        for cid in commandDict:
            self.registsr(cid, commandDict[cid])
        return 0