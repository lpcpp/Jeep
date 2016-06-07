# -*- coding: utf-8 -*-
from blog import models
from bson import ObjectId
import datetime


def get_blog_by_id(blog_id):
    try:
        blog = models.Blog.objects.get(id=ObjectId(blog_id))
    except:
        return None
    return blog


def get_blog_list_by_member_id(member_id):
    blog_list = models.Blog.objects.filter(member_id=member_id)
    return blog_list


def get_blog_list():
    blog_list = models.Blog.objects.all()
    return blog_list


def add_blog(member_id, title, content):
    blog = models.Blog(member_id=member_id, title=title, content=content)
    blog.save()

    return blog


def update_blog(blog_id, **params):
    blog = get_blog_by_id(blog_id)
    if blog:
        for key, value in params.iteritems():
            blog[key] = value

        blog.update_time = datetime.datetime.now()
        blog.save()

    return blog
