# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Teamname, Category

admin.site.register(Teamname)
admin.site.register(Category)
