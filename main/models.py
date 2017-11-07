# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from  django.contrib.auth.models import User



#  current landing is plce is good.
#
#  one off task - create a user profile for each of the existing users
#  user django admin's save

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    JUDGE = 1
    REGISTRAR = 2
    USER_TYPE_CHOICES = (  (JUDGE, 'Judge'), (REGISTRAR, 'Registrar') )
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES)