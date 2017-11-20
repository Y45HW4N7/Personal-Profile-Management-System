# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
#from signup.models import UserProfile

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #first_name = models.CharField(max_length=250)
    #last_name = models.CharField(max_length=250)
    birthdate = models.DateField(max_length=100)
    age = models.IntegerField()
    #email = models.EmailField(max_length=250)
    number = models.IntegerField()
    profession = models.CharField(max_length=600)
    hobbies = models.CharField(max_length=600)
    location = models.CharField(max_length=100)

    def __unicode__(self):
        return str(self.user) + '-' + str(self.age)