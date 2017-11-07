# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from main.models import UserProfile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    def username(self, instance):
        return instance.user.username

    list_display = ('user_type', username)

#
#

admin.site.register(UserProfile, ProfileAdmin)