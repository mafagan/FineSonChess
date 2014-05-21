#!/usr/bin/python
#-*-coding:utf-8-*-
from service.service import service
__author__ = 'Winterma'

class login_service(service):
    SERVICE_ID = 2000
    def __init__(self):
        super(test_service, self).__init__(sid)
        commands = {
            1000 : self.handle_login
        }

    def handle_login(self, msg, who):
        pass
