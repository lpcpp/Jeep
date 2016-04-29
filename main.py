# -*- coding: utf-8 -*-
import tornado.web
import tornado.ioloop
from common.utils import connect_db
import settings
from urls import urlpatterns
from tornado.httpserver import HTTPServer


if __name__ == "__main__":
    connect_db()
    application = tornado.web.Application(urlpatterns, **settings.settings)
    httpserver = HTTPServer(application, xheaders=True)
    httpserver.listen(settings.PORT)
    tornado.ioloop.IOLoop.instance().start()
