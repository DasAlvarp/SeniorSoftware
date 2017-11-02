# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin






class Category(models.Model):
    #team = models.ForeignKey(Teamname, on_delete=models.CASCADE)
    category_text = models.CharField(max_length=200)

    def __str__(self):
        return self.category_text

class Teamname(models.Model):
    teamname_text = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.teamname_text


class Teammember(models.Model):
    teammember_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.teammember_name
