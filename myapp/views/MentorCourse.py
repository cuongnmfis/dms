'''
Created on Apr 3, 2014
@author: TuanNA
'''
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from mongoengine.django.auth import User

from myapp.models import Material, MaterialType, UserProfile,\
	CurriculumnStudyProgress, Impression
from myapp.models.Action import Action
from myapp.models.Curriculumn import Curriculumn
from myapp.models.Mentor import Mentor


@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		try:
			user_id = request.GET['user_id']
		except Exception:
			user_id = request.user
		user = User.objects.get(id=user_id)
		context = {'mentor':user}
		return render(request,'myapp/mentor-course.html', context)
	elif request.method == 'POST':
# 		profile = UserProfile.objects.get(user_id=request.user)
# 		profile.is_mentor = True
# 		profile.save()
# 		mentor = Mentor()
# 		mentor.user = request.user
# 		mentor.save()
		mentor = Mentor.objects.get(user=request.user)
		#curriculum
		course_name = request.POST['course_name']
		duration = request.POST['duration']
		duration_type = request.POST['duration_type']
		start_date = request.POST['start_date']
		end_date = request.POST['end_date']
		curriculumn = Curriculumn()
		curriculumn.name = course_name
		curriculumn.duration = duration
		curriculumn.duration_type = duration_type
		curriculumn.from_date = datetime.strptime(start_date,'%m/%d/%Y')
		curriculumn.to_date = datetime.strptime(end_date,'%m/%d/%Y')
		curriculumn.mentor = mentor
		curriculumn.save()
		#material
		material_title = request.POST['material_title']
		material_type = request.POST['material_type']
		material_url = request.POST['material_url']
		material_code = ""
		material_description = request.POST['material_description']
		material = Material()
		material.name = material_title
		material.type = MaterialType.objects.get(name=material_type)
		material.url = material_url
		material.code = material_code
		material.description = material_description
		material.save()
		curriculumn.material.append(material)
		curriculumn.save()
		#action
		action_name = request.POST['action_name']
		action_description = request.POST['action_description']
		action = Action()
		action.name = action_name
		action.description = action_description
		if request.POST['action_name']:
			action.save()
			curriculumn.action.append(action)
			curriculumn.save()
		return HttpResponseRedirect('/');
@login_required(login_url='/signin')
def add_action(request):
	if request.method == 'POST':
		#curriculum
		curriculum_id = request.POST['curriculum_id']
		curriculum = Curriculumn.objects.get(id=curriculum_id)
		#action
		action_name = request.POST['action_name']
		action_description = request.POST['action_description']
		action = Action()
		action.name = action_name
		action.description = str(action_description.encode('utf-8'))
		action.save()
		#curriculum
		curriculum.action.append(action)
		curriculum.save()
		return HttpResponseRedirect('/mentorview');
@login_required(login_url='/signin')
def add_material(request):
	if request.method == 'POST':
		#curriculum
		try:
			curriculum_id = request.POST['curriculum_id']
			curriculum = Curriculumn.objects.get(id=curriculum_id)
			#material
			material_title = request.POST['material_title']
			material_type = request.POST['material_type']
			material_url = request.POST['material_url']
			material_code = ""
			material_description = request.POST['material_description']
		except Exception as e:
			c = {
					'error_message':e,
				}
		material = Material()
		material.name = material_title
		material.type = MaterialType.objects.get(name=material_type)
		material.url = material_url
		material.code = material_code
		material.description = str(material_description.encode('utf-8'))
		material.save()
		#curriculum
		curriculum.material.append(material)
		curriculum.save()
		return HttpResponseRedirect('/mentorview');
@login_required(login_url='/signin')
def join_course(request):
	if request.method == 'POST':
		curriculum_id = request.POST['curriculum_id']
		curriculum = Curriculumn.objects.get(id=curriculum_id)
		planstart = request.POST['planstart']
		planend = request.POST['planend']
		impression = request.POST['impression']
		description = request.POST['description']
		
		stp = CurriculumnStudyProgress()
		stp.curriculumn = curriculum 
		stp.PlanStartDate = datetime.strptime(planstart,'%m/%d/%Y')
		stp.PlanEndDate = datetime.strptime(planend,'%m/%d/%Y')
		stp.impression = Impression.objects.get(showpiority=impression)
		stp.description = str(description.encode('utf-8'))
		stp.user = request.user
		stp.save()

		return HttpResponseRedirect('/course-detail?course_id=' + curriculum_id);
