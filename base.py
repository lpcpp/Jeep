# -*- coding: utf-8 -*-

import tornado.web
from admin import dao as admin_dao


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        username = self.get_cookie('username')
        if username:
            user = admin_dao.get_user_by_username(username)
            return user
