# -*- coding: utf-8 -*-
import functools
import urlparse
import urllib
import hashlib
import mongoengine
import settings
from tornado.web import HTTPError
from blog import dao


def connect_db():
<<<<<<< HEAD
    from settings import DB_ADDRESS, DB_NAME, DB_PORT
    from mongoengine.connection import connect

    connect(DB_NAME, host=DB_ADDRESS, port=DB_PORT)
=======
    mongoengine.connect(settings.DB_NAME, host=settings.DB_HOST, port=settings.DB_PORT)


def md5(astring):
    return hashlib.md5(astring).hexdigest()


def owner_authenticated(method):
    """Decorate methods with this to require that the user be logged in."""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self.current_user:
            if self.request.method in ("GET", "HEAD"):
                url = self.get_login_url()
                if "?" not in url:
                    if urlparse.urlsplit(url).scheme:
                        # if login url is absolute, make next absolute too
                        next_url = self.request.full_url()
                    else:
                        next_url = self.request.uri
                    url += "?" + urllib.urlencode(dict(next=next_url))
                self.redirect(url)
                return

            raise HTTPError(403)
        blog_id = args[0]
        print 'owern_authenticated:', blog_id
        try:
            blog = dao.get_blog_by_blog_id(blog_id)
            if blog.member_id != self.current_user['id']:
                self.write("Access denied!")
                return
        except:
            pass
        return method(self, *args, **kwargs)
    return wrapper
>>>>>>> d8c7f8f8b87241e8511d07f10af33957316f1857
