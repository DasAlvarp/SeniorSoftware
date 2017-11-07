# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from main.models import UserProfile

# Register your models here.

from .models import Team, Category, Member, ScoringCriteria, Score


class MemberAdmin(admin.ModelAdmin):
	pass

class TeamAdmin(admin.ModelAdmin):
	pass

class CategoryAdmin(admin.ModelAdmin):
	pass

class ScoringCriteriaAdmin(admin.ModelAdmin):
	pass

class ScoreAdmin(admin.ModelAdmin):
	pass

class ProfileAdmin(admin.ModelAdmin):
    def username(self, instance):
        return instance.user.username

    list_display = ('user_type', username)

admin.site.register(ScoringCriteria, ScoringCriteriaAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Score)
admin.site.register(UserProfile, ProfileAdmin)

