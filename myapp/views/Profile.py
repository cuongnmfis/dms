'''
Created on Apr 3, 2014

@author: TuanNA
'''
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from mongoengine.django.auth import User

from myapp.models import SocialProfile
from myapp.models.JobTitle import JobTitle
from myapp.models.UserProfile import UserProfile
from myapp.models.UserType import UserType
from myapp.models.WorkField import WorkField
from myapp.util import context_processors


@login_required(login_url='/signin')
def index(request):
	try:
		user_id = request.GET['user_id']
		ListSocialProfiles = SocialProfile.objects(user_id=User.objects.get(id=user_id))
		profile = UserProfile.objects.get(user_id=User.objects.get(id=user_id))
		ListProfiles = UserProfile.objects
		context = {'profile':profile, 'ListSocialProfile':ListSocialProfiles, "ListProfiles":ListProfiles}
		return render(request, 'myapp/profile.html', context)
	except Exception:
		profile = UserProfile()
		profile.user_id = User.objects.get(id="user_id")
		profile = UserProfile.objects.get(user_id=User.objects.get(id=user_id))
		context = {'profile':profile, }
		return render(request, 'myapp/profile.html', context)
@login_required(login_url='/signin')
def createProfile(request):
	context = {}
	return render(request, 'myapp/create-profile.html', context)
@login_required(login_url='/signin')
def updateProfile(request):
	if request.method == 'GET':
		job_titles = JobTitle.objects
		work_fields = WorkField.objects
		context = {'job_titles':job_titles, 'work_fields':work_fields, 'acccount_type':request.GET['acccount_type'], }
		return render(request, 'myapp/create-profile-update.html', context)
	elif request.method == 'POST':
		try:
			acccount_type = request.POST['acccount_type']
			jobTitle = request.POST['slJobTitle']
			workField = request.POST['slWorkField']
			company = request.POST['txtCompany']
			about = request.POST['txtAbout']
			_profile = UserProfile.objects.get(user_id=request.user)
			_profile.job_title = JobTitle.objects.get(id=jobTitle)
			_profile.work_field = WorkField.objects.get(id=workField)
			_profile.user_type = UserType.objects.get(code=acccount_type)
			_profile.user_id = request.user
			_profile.company = company
			_profile.about = about
			_profile.save()
			request.session['user_type'] = acccount_type
			return HttpResponseRedirect('/home')
		except Exception as e:
			print(e)
			c = {
				'error_message':e, 'job_titles':JobTitle.objects, 'work_fields':WorkField.objects, 'acccount_type':request.GET['acccount_type'],
				}
			c.update(csrf(request))
			c.update(context_processors.user(request))
			return render_to_response("myapp/create-profile-update.html", c)
