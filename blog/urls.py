# -*- coding: utf-8 -*-
from blog import views


urlpatterns = [
    (r"/blog/list/?", views.BlogListHandler),
    (r"/blog/add/?", views.AddBlogHandler),
    (r"/blog/update/([a-z0-9]+)/?", views.UpdateBlogHandler),
]
