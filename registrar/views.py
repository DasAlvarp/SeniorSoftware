from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def registrar(request):
    return HttpResponse("Hello, world. You're at the registrar index.")
