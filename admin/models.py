# -*- coding: utf-8 -*-
import mongoengine as models
import datetime


class User(models.Document):
    username = models.StringField(max_length=50)
    create_time = models.DateTimeField(default=datetime.datetime.now)
    password = models.StringField()
    mobile = models.StringField()
    email = models.EmailField()
