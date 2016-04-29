from base import BaseHandler
from common.log import getLogger

log = getLogger('blog/views')


class BlogHandler(BaseHandler):
    def get(self):
        log.debug('test')
        self.render('blog.html')
