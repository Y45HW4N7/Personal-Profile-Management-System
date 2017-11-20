# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.views.generic import CreateView
from django.http import HttpResponseRedirect

# Create your views here.

#def index(request):
    #return HttpResponse("<h1>Please fill in the following details</h1>")

def index(request):
    name = "Yashwant"
    html = "<html><body>Hi %s, this seems to be working!</body></html>" % name
    return HttpResponse(html)