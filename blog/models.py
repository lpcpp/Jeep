# -*- coding: utf-8 -*-
import mongoengine as models


class Blog(models.Document):
    create_time = models.IntField(default=None)
    title = models.StringField()
