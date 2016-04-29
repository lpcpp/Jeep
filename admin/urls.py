# -*- coding: utf-8 -*-
from admin import views


urlpatterns = [
    (r"/register/?", views.LoginHandler),
    (r"/login/?", views.RegisterHandler),
]
