# -*- coding: utf-8 -*-
import json
from base import BaseHandler
from common.log import getLogger
from common.utils import md5
from admin import dao

log = getLogger('admin/views')


class LoginHandler(BaseHandler):
    def get(self):
        log.debug('Login get')
        if self.get_current_user():
            self.redirect('/blog/list')

        self.render('login.html')

    def post(self):
        log.debug('Login post')
        username = self.get_argument('username')
        password = self.get_argument('password')
        user = dao.get_user_by_username(username)
        if user and user.password == md5(password):
            self.set_cookie('username', username)
            self.write(json.dumps({'status': 'success'}))
        else:
            self.write(json.dumps({'status': 'fail', 'err_msg': u'用户名和密码不匹配'}))


class RegisterHandler(BaseHandler):
    def get(self):
        log.debug('register')
        username = 'luopeng'
        password = '123456'
        if not dao.get_user_by_username(username):
            dao.create_user(username, password)
            self.write('success')
            return

        self.write(u'用户已存在')
