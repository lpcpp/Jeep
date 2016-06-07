# -*- coding: utf-8 -*-
import mongoengine as models
import datetime
from blog import enums as blog_enums


class Blog(models.Document):
    memebr_id = models.StringField()
    create_time = models.DateTimeField(default=datetime.datetime.now)
    update_time = models.DateTimeField(default=datetime.datetime.now)
    title = models.StringField()
    content = models.StringField()
    status = models.IntField(default=blog_enums.BLOG_STATUS_NORMAL)


class Comment(models.Document):
    blog_id = models.StringField()
    create_time = models.DateTimeField(default=datetime.datetime.now)
    content = models.StringField()
    status = models.IntField(default=blog_enums.COMMENT_STATUS_NORMAL)
    who = models.StringField()    # 由谁留下的评论, 可以是一个邮箱，手机或者ＱＱ号
    ip = models.StringField()    # 发表评论的IP地址
