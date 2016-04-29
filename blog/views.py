from base import BaseHandler


class BlogHandler(BaseHandler):
    def get(self):
        self.write('8888')
