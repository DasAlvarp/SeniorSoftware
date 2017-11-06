# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *


def index(request):
    return HttpResponse("Welcome to index.")

def teams(request):
	teamList = Team.objects.all()
	template = loader.get_template('teams.html')
	context = {
		'teamList':teamList,
	}

	return HttpResponse(template.render(context,request))

def judgeTeam(request):
	# Get the team name from the url
	team = request.GET['team']

	#load template
	template = loader.get_template('judge.html')

	# get the list of categories the team entered in
	categoryList = Team.objects.get(teamName__exact=team)
	categoryList = categoryList.category.all()

	# 2d array of the criteria
	criteria = [[crit for crit in cat.criteria.all()] for cat in categoryList]

	# create a dictionary of the categories and their criteria
	catAndCrit = dict(zip(categoryList, criteria))

	context = {
		'team':team,
		'catAndCrit':catAndCrit,
	}
	return HttpResponse(template.render(context,request))