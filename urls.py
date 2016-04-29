# -*- coding: utf-8 -*-
import index
import blog.urlpatterns
import admin.urlpatterns

urlpatterns = (
    (r"/?", index.IndexHandler),
)


urlpatterns += blog.urlpatterns + admin.urlpatterns
