# -*- coding: utf-8 -*-
from blog import views


urlpatterns = (
    (r"/?", views.BlogHandler),
)
