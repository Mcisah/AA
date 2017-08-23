from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Category(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    contestants_no = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Contestant(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    names = models.CharField(max_length=255)
    category = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    percentage = models.IntegerField(default=0)

    def __str__(self):
        return self.names


class Vote(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    ip_ad = models.GenericIPAddressField(max_length=255)
    contestant = models.IntegerField(default=0)
    category = models.IntegerField(default=0)

    def __str__(self):
        return self.ip_ad


class Sum(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.IntegerField(default=0)
    sum = models.IntegerField(default=0)

    def __str__(self):
        return "Summer"