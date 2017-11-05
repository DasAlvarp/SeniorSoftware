# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django import forms
from django.core.validators import MaxValueValidator





class ScoringCriteria(models.Model):
    criteriaName = models.CharField(max_length = 100)
    score =  models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10),])

    def __str__(self):
        return self.criteriaName


class Category(models.Model):

    category = models.CharField(max_length=200)
    criteria = models.ManyToManyField(ScoringCriteria, blank = True)

    def __str__(self):
        return self.category


class Member(models.Model):
    memberName = models.CharField(max_length = 100)

    def __str__(self):
        return self.memberName


class Team(models.Model):
    teamName = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    member = models.ManyToManyField(Member, blank=True)
    score = models.IntegerField()

    def __str__(self):
        return self.teamName
