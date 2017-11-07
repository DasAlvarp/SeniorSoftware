# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.template import loader
from django.http import HttpResponse
from .models import *


def index(request):
    return HttpResponse("Welcome to index.")

def home(request):
    return render(request, 'dir.html')

def teams(request):
    #get list of all teams
	teamList = Team.objects.all()

    #get list of categories corresponding to teams
	category = [[cat for cat in team.category.all()] for team in teamList]

    #put into dictionary
	categoryAndTeam = dict(zip(teamList, category))
    
	template = loader.get_template('teams.html')
	context = {
		'teamList':teamList,
		'categoryAndTeam' :categoryAndTeam,
	}
	return HttpResponse(template.render(context,request))


def judgeTeam(request):
	# Get the team name and category entered from the url
	team = request.GET['team']
	category = request.GET['category']

	# Retrieve team object and category object from DB to list scoring criteria on the form
	teamObj = Team.objects.get(teamName__exact=team)
	cat = Category.objects.get(category__exact=category)
	crit = list(cat.criteria.all())
	criteria = [c.criteriaName for c in crit]

	# Load the model form
	form = ScoreForm()

	# check if this judge has already scored this team for this category, load their scores if they have
	score = Score.objects.filter(teamName=teamObj, category=cat, judge=request.user)
	update = False
	if score:
		update = True
		form.fields['score1'].initial = score[0].score1
		form.fields['score2'].initial = score[0].score2
		form.fields['score3'].initial = score[0].score3

	# update entry if judge already scored, create a new score if they haven't
	if request.method == 'POST' and update:
		form = ScoreForm(request.POST, instance=score[0])
		if form.is_valid():
			form.save()
		return redirect('/teams')
	elif request.method =='POST':
		form = ScoreForm(request.POST)
		if form.is_valid():
			score = form.save(commit=False)
			score.teamName = teamObj
			score.category = cat
			score.judge = request.user
			score.save()
		return redirect('/teams')

	context = {
		'team':team,
		'category':category,
		'criteria':criteria,
		'ScoreForm':form,
	}
	return render(request, 'judge.html', context)
>>>>>>> master
