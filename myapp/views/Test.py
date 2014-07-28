'''
Created on Apr 3, 2014
@author: TuanNA
'''
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from mongoengine.django.auth import User

from myapp.models.CommentPost import CommentPost
from myapp.models.Esay import Esay
from myapp.models.MentorPost import MentorPost
from myapp.util import context_processors


@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		context = {}
		return render(request,'myapp/test.html', context)
	