# -*- coding: utf-8 -*-
'''
Created on Apr 3, 2014

@author: TuanNA
'''
from datetime import datetime
import json

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from myapp.models.Action import Action
from myapp.models.Category import Category
from myapp.models.Curriculumn import Curriculumn
from myapp.models.Material import Material
from myapp.models.MaterialType import MaterialType
from myapp.models.Mentor import Mentor


@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		print("method is get")
		name="ádasdasfas"
		context = {'name':name}
		return render(request, 'myapp/mentor-post.html', context)
	elif request.method == 'POST':

		numberMaterial=int(request.POST['numberMaterial'])
		
		mentor = Mentor.objects.get(user=request.user)
		
		category_id =request.POST['childrenCategory']
		category =Category.objects.get(id=category_id)
		#curriculum
		course_name = request.POST['course_name']
		description =request.POST['curriculumn_description']
		duration = request.POST['duration']
		duration_type = request.POST['duration_type']
		start_date = request.POST['start_date']
		end_date = request.POST['end_date']
		curriculumn = Curriculumn()
		curriculumn.name = course_name
		curriculumn.duration = duration
		curriculumn.description=str(description.encode('utf-8'))
		curriculumn.duration_type = duration_type
		curriculumn.from_date = datetime.strptime(start_date,'%m/%d/%Y')
		curriculumn.to_date = datetime.strptime(end_date,'%m/%d/%Y')
		curriculumn.mentor = mentor
		curriculumn.category=category
		curriculumn.save()
		#material
		try:
			for n in range(numberMaterial):
				material_title = request.POST['material_title'+str(n+1)]
				material_type = request.POST['material_type'+str(n+1)]
				material_url = request.POST['material_url'+str(n+1)]
				material_description = request.POST['material_description'+str(n+1)]
				material_hide = request.POST['material_hide'+str(n+1)]
				material = Material()
				material.name = material_title
				material.type = MaterialType.objects.get(name=material_type)
				material.url = material_url
				material.description = str(material_description.encode('utf-8'))
				if material_hide == '0':
					material.save()
					curriculumn.material.append(material)
					curriculumn.save()
			#action
			action_name = request.POST['action_name']
			action_description = request.POST['action_description']
			action = Action()
			action.name = action_name
			action.description = str(action_description.encode('utf-8'))
			if request.POST['action_name'] :
				action.save()
				curriculumn.action.append(action)
				curriculumn.save()
		except Exception as ex:
			print("CreateCurriculumn.add material: "+ex)
			curriculumn.delete()
		return HttpResponseRedirect('/mentorview')

# 		materialId="insert material "
# 		return HttpResponse(json.dumps({"formdata": materialId}),content_type="application/json")
