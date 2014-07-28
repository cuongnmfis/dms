'''
Created on Apr 3, 2014

@author: TuanNA
'''
from django.contrib.auth import logout
from django.http.response import HttpResponseRedirect


def index(request):
	request.session['user_images'] = ""
	logout(request)
	return HttpResponseRedirect('/')