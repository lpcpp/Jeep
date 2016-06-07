# -*- coding: utf-8 -*-
from business import views
from auth import views as auth_views


urlpatterns = (
    (r"/?", views.IndexHandler),
    (r"/login/?", auth_views.LoginHandler),
    (r"/logout/?", auth_views.LogoutHandler),

    (r"/test_sync/?", views.TestSyncHandler),
    (r"/test_async/?", views.TestAsyncHandler),
)
