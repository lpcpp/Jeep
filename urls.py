# -*- coding: utf-8 -*-
import index
import blog.urls
import admin.urls

urlpatterns = [
    (r"/?", index.IndexHandler),
]


urlpatterns += blog.urls.urlpatterns + admin.urls.urlpatterns

print urlpatterns
