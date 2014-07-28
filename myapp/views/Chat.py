'''
Created on Apr 3, 2014

@author: TuanNA
'''
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from myapp.models.UserProfile import UserProfile


@login_required(login_url='/signin')
def index(request):
	profiles = UserProfile.objects
	context = {'profiles':profiles,}
	return render(request, 'myapp/chat.html', context)
	