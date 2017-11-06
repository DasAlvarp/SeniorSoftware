# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Team


def index(request):
    return HttpResponse("Welcome to index.")

def teams(request):
	teamList = Team.objects.all()
	template = loader.get_template('teams.html')
	context = {
		'teamList':teamList,
	}

	return HttpResponse(template.render(context,request))