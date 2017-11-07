# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect

def index(request):
    return HttpResponse("Main Home Page. Please select from below")

def home(request):
    return render(request, "home.html")

def homepage(request):
    return HttpResponseRedirect('/main')

def judge(request):
    return HttpResponse('judge section')

def registrar(request):
    return HttpResponse('registrar section')
