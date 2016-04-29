# -*- coding: utf-8 -*-
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
        password = self.get_arguemnt('password')
        user = dao.get_user_by_username(username)
        if user and user.password == md5(password):
            self.set_cookie('username', username)
            self.redirect('/blog/list/')
        else:
            self.write({'status': 'fail', 'err_msg': u'用户名和密码不匹配'})


def RegisterHandler(BaseHandler):
    def get(self):
        dao.create_user('luopeng', '123456')
