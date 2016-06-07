import json
from base import BaseHandler
from common.log import getLogger
from common.utils import owner_authenticated
from blog import dao

log = getLogger('blog/views')


class BlogListHandler(BaseHandler):
    def get(self):
        log.debug('BlogList get')
        blog_list = dao.get_blog_list()
        self.render('blog.html', blog_list=blog_list)


class AddBlogHandler(BaseHandler):
    def get(self):
        self.render('add_blog.html')

    def post(self):
        log.debug('AddBlog post')
        user = self.get_current_user()
        title = self.get_argument('title', '')
        content = self.get_argument('content', '')
        dao.add_blog(user.oid, title, content)
        self.write(json.dumps({'status': 'success'}))


class UpdateBlogHandler(BaseHandler):
    @owner_authenticated
    def post(self, blog_id):
        dao.update_blog(blog_id)
        self.write({'status': 'success'})
