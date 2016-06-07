from base import BaseHandler


class IndexHandler(BaseHandler):
    def get(self):
        self.redirect('/blog/list/')
