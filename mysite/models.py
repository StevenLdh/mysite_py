#!/usr/bin/env python
# -*-coding:utf-8-*-

__author__ = 'Steven'
from django.db import models


class Slideshow(models.Model):
    # 图片地址
    Slideshow_img_url = models.CharField(max_length=200, blank=True, null=True)
    # 图片链接地址
    Slideshow_url = models.CharField(max_length=200, blank=True, null=True)
    # 图片提示
    Slideshow_title = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'slideshow'


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.title
