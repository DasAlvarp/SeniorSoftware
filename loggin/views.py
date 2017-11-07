# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect

from main.models import UserProfile

from django.contrib.auth.models import User


def aa(request):

    '''
    user_id = request.user.id
    grp_id   = User.objects.get(pk=user_id).groups.all()[0].id
    grp_name = User.objects.get(pk=user_id).groups.all()[0].name

    grps = User.objects.get(pk=user_id).groups.all()
    if len(grps) > 0:
        return HttpResponse(" -> " + grps[0].name)

    else:
        return HttpResponse(" no grp for " + str(user_id))

    return HttpResponse(str(User.objects.get(pk=user_id).username) + " - " + str(grp_id) + " - " + grp_name)
    # return HttpResponse( str(request.user.id) + " - " + str( Group.objects.all()[0].name) )
    '''

    if request.user.is_authenticated:
        user_id = request.user.id
        grp_id = User.objects.get(pk=user_id).groups.all()[0].id
        grp_name = User.objects.get(pk=user_id).groups.all()[0].name.lower()

        return HttpResponseRedirect("/" + grp_name)
        #if User.objects.get(pk=request.user.id).groups.all()[0].id == 3:
        #    return HttpResponse("login successful - judge profile ")
        #
        #else:
        #    return HttpResponse("fail")

