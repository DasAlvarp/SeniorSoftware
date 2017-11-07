from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /registrar/
    url(r'^$', views.registrar, name='registrar'),
]

'''
    # ex: /registrar/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /registrar/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /registrar/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
'''
