#!/usr/bin/python
#-*-coding:utf-8-*-
__author__ = 'Winterma'

class dispatcher(object):
    def __init__(self):
        self.__service_map = {}

    def dispatch(self, msg, owner):
        sid = msg.id
        if not sid in self.__service_map:
            raise Exception('bad service %d'%sid)
        svc = self.__service_map[sid]
        svc.handle(msg, owner)

    def register(self, sid, svc):
        self.__service_map[sid] = svc