# -*- coding: utf-8 -*-
import os
import logging

DEBUG = True

<<<<<<< HEAD
DB_ADDRESS = '127.0.0.1'
DB_NAME = 'office'
=======
DB_HOST = '115.28.15.67'
DB_NAME = 'blog'
>>>>>>> d8c7f8f8b87241e8511d07f10af33957316f1857
DB_PORT = 27017

PORT = '8000'
SECRET_KEY = 'xw886xItZp007qK9nyutCgGSEaojaGsrrZF8NzWL'

settings = dict(
    cookie_secret=SECRET_KEY,
    login_url="/login/",
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    root_path=os.path.dirname(__file__),
    xsrf_cookies=True,
    autoescape="xhtml_escape",
    debug=DEBUG,
    xheaders=True,
)


LOG_LEVEL = logging.DEBUG if DEBUG else logging.INFO
