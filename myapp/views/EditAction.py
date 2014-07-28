# -*- coding: utf-8 -*-
'''
Created on Apr 3, 2014

@author: TuanNA
'''

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from myapp.models.Action import Action


@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		print("method is get")
		name="edit material"
		context = {'name':name}
		return render(request, 'myapp/mentor-post.html', context)
	elif request.method == 'POST':	
		action_name = request.POST['action_name']
		action_description = request.POST['action_description']
		action_id=request.POST['action_id']
		
		action = Action.objects.get(id=action_id)
		action.name = action_name
		action.description = action_description
		action.save()
		print('edit action edit action ')
		return HttpResponseRedirect('/mentorview')
