# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin


class Category(models.Model):

    category = models.CharField(max_length=200)
    SCORES = (('1', '1'),
              ('2', '2'),
              ('3', '3'),

                    )
    score = models.CharField(max_length = 5, choices = SCORES, default = 0)

    def __str__(self):
        return self.category


class Member(models.Model):
    memberName = models.CharField(max_length = 100)

    def __str__(self):
        return self.memberName



class Team(models.Model):
    teamName = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    member = models.ManyToManyField(Member, blank = True)

    def __str__(self):
        return self.teamName
