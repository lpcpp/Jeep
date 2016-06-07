from base import BaseHandler
from auth.models import User
# from auth import enums


class LoginHandler(BaseHandler):
    def get(self):
        # users = User.objects.all()
        # u = User(number='001', name='Jack', age=18, sex=enums.MALE, department='market', position='manager', mobile='12345', emergency_contact='54321')
        # u.save()
        # users = User.objects.all()
        # self.write(users.to_json())
        # print self.request.cookies
        self.render('auth/login.html')

    def post(self):
        self.redirect('/')
        pass

    def check_xsrf_cookie(self):
       return


class LogoutHandler(BaseHandler):
    def post(self):
        pass
