# -*- coding: utf-8 -*-
'''
Created on Apr 3, 2014

@author: TuanNA
'''
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from myapp.models.Curriculumn import Curriculumn
from myapp.models.MaterialType import MaterialType
from myapp.models.Material import Material

@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		print("method is get")
		name="edit material"
		context = {'name':name}
		return render(request, 'myapp/mentor-post.html', context)
	elif request.method == 'POST':	
		material_title = request.POST['material_title']
		material_type = request.POST['material_type']
		material_url = request.POST['material_url']
		material_description = request.POST['material_description']
		material_id=request.POST['material_id']
		
		material = Material.objects.get(id=material_id)
		material.name = material_title
		material.type = MaterialType.objects.get(name=material_type)
		material.url = material_url
		material.description = material_description
		material.save()
		print('edit material edit material ')
		return HttpResponseRedirect('/mentorview')
