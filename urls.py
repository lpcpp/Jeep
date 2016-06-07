# -*- coding: utf-8 -*-
<<<<<<< HEAD
from business import views
from auth import views as auth_views
=======
import index
import blog.urls
import admin.urls
>>>>>>> d8c7f8f8b87241e8511d07f10af33957316f1857

urlpatterns = [
    (r"/?", index.IndexHandler),
]

<<<<<<< HEAD
urlpatterns = (
    (r"/?", views.IndexHandler),
    (r"/login/?", auth_views.LoginHandler),
    (r"/logout/?", auth_views.LogoutHandler),

    (r"/test_sync/?", views.TestSyncHandler),
    (r"/test_async/?", views.TestAsyncHandler),
)
=======

urlpatterns += blog.urls.urlpatterns + admin.urls.urlpatterns

print urlpatterns
>>>>>>> d8c7f8f8b87241e8511d07f10af33957316f1857
