import tornado.httpclient
import tornado.web
import tornado.gen
from base import BaseHandler
from common.log import getLogger

log = getLogger('business/views')


class IndexHandler(BaseHandler):
    def get(self):
        self.write('zhangsanlaile')


class TestSyncHandler(BaseHandler):
    def get(self):
        client = tornado.httpclient.HTTPClient()
        client.fetch('http://192.168.1.189:8001')
        self.write('success')


class TestAsync1Handler(BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch('http://192.168.1.189:8001', callback=self.on_response)

    def on_response(self, response):
        self.write('success async')
        self.finish()


class TestAsyncHandler(BaseHandler):
    @tornado.gen.coroutine
    def get(self):
        client = tornado.httpclient.AsyncHTTPClient()
        yield client.fetch('http://192.168.1.189:8001')
        self.write('success')
