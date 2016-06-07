# -*- coding: utf-8 -*-
import mongoengine as models
import datetime
from auth import enums


class User(models.Document):
    number = models.StringField()
    name = models.StringField()
    age = models.IntField()
    sex = models.IntField(choices=enums.SEX_LIST)
    department = models.StringField()
    position = models.StringField()
    mobile = models.StringField()
    emergency_contact = models.StringField()
    create_time = models.DateTimeField(default=datetime.datetime.now)
    status = models.IntField(default=enums.USER_STATUS_NORMAL, choices=enums.USER_STATUS_LIST)
