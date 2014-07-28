# -*- coding: utf-8 -*-
'''
Created on Apr 3, 2014

@author: TuanNA
'''
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from myapp.models.Category import Category
from myapp.models.Curriculumn import Curriculumn
from myapp.models.Material import Material
from myapp.models.MaterialType import MaterialType


@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		print("method is get")
		name="edit material"
		context = {'name':name}
		return render(request, 'myapp/mentor-post.html', context)
	elif request.method == 'POST':
		curriculumn_id=request.POST['edit_curriculumn_id']
		curriculumn_name = request.POST['editName']
		curriculumn_duration = request.POST['editDuration']
		curriculumn_duration_type = request.POST['editDurationType']
		curriculumn_category = request.POST['changeChildrenCategory']
		curriculumn_from_date=request.POST['curriculumstartdate']
		curriculumn_to_date = request.POST['curriculumenddate']
		curriculumn_description = request.POST['editDescription']
		
		
		curriculumn = Curriculumn.objects.get(id=curriculumn_id)
		curriculumn.name = curriculumn_name
		curriculumn.duration = curriculumn_duration
		curriculumn.duration_type = curriculumn_duration_type
		curriculumn.category = Category.objects.get(id=curriculumn_category)
		curriculumn.from_date=datetime.strptime(curriculumn_from_date,'%m/%d/%Y')
		curriculumn.to_date=datetime.strptime(curriculumn_to_date,'%m/%d/%Y')
		curriculumn.description = curriculumn_description
		curriculumn.save()
		print('edit curriculumn edit curriculumn ')
		return HttpResponseRedirect('/mentorview')
