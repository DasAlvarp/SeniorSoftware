from django.conf.urls import url
from . import views

urlpatterns = [
    	url(r'^$', views.index, name='index'),
	url(r'teams/', views.teams, name='teams'),
	url(r'judgeTeam/', views.judgeTeam, name='judgeTeam'),
]
