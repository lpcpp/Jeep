# -*- coding: utf-8 -*-
from admin import views


urlpatterns = [
    (r"/register/?", views.RegisterHandler),
    (r"/login/?", views.LoginHandler),
]
