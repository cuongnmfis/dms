'''
Created on Apr 3, 2014

@author: TuanNA
'''
from django.contrib.auth import logout, login
from django.core.context_processors import csrf
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from mongoengine.django.auth import User

from myapp.models.Mentor import Mentor
from myapp.models.Student import Student
from myapp.models.UserLogin import UserLogin
from myapp.models.Curriculumn import Curriculumn
from myapp.models.UserProfile import UserProfile
from myapp.util import context_processors


def signinsns(request):
	is_mentor = False
	is_join = False
	defaultUserImage = "/images/avatar/default.png"
	
	if 'next' in request.GET:
		nextpage = request.GET['next']
	else:
		nextpage = ""
	user1=User.objects.get(username=str(request.user))
	thismentor = Mentor.objects(user=user1.id)
	thisstudent = Student.objects(user=user1.id)
	thiscurrijoined = Curriculumn.objects()
	
	username=str(request.user)
	avatar = ""
	user_images = ""
	try:
		thisprofile = UserProfile.objects(user_id=user1)
		request.session['user_images'] = thisprofile[0].images
		user_images= request.session['user_images']

	except Exception as e:
		upro = UserProfile()
		upro.user_id = user1
		upro.images = defaultUserImage
		upro.save()
		request.session['user_images'] = defaultUserImage
		print(e)
			
	for cl in thiscurrijoined:
		if username in cl.joined_user:
			is_join = True	
	
	if len(thisstudent) ==  0:
		studentnew = Student()
		studentnew.user = user1
		studentnew.save()

	if len(thismentor) > 0:
		is_mentor = True
		
	request.session['is_mentor'] = is_mentor
	context = 	{
				'avatar':avatar,
				'user_images':user_images
				}
	if nextpage:
		return HttpResponseRedirect(nextpage,context)
	else:
		if is_mentor:
			return HttpResponseRedirect('/mentorview',context )
		else:
			if is_join:
				return HttpResponseRedirect('/student-home',context)
			else:
				return HttpResponseRedirect('/search-mentor',context)
def index(request):
	username = ""
	password = ""
	is_mentor=False
	is_join = False
	defaultUserImage = "/images/avatar/default.png"
	
	username=str(request.user)
	
	thiscurrijoined1 = Curriculumn.objects()
	
	for cl in thiscurrijoined1:
		if username in cl.joined_user:
			is_join = True	
			
	if request.method == 'GET':
		return render(request, 'myapp/signin.html', {})
	elif request.method == 'POST':
		username = request.POST['txtUserName']
		password = request.POST['txtPassWord']
		
		if 'next' in request.GET:
			nextpage = request.GET['next']
		else:
			nextpage = ""
		try: 
			
			user = User.objects.get(username=username)
			transaction = UserLogin()
			transaction.user = user
			transaction.save()
			if user.check_password(password):
				logout(request)
				user.backend = 'mongoengine.django.auth.MongoEngineBackend'
				login(request, user)

				mentor = Mentor.objects(user=user)
				if len(mentor) > 0:
					is_mentor = True
				request.session['is_mentor'] = is_mentor

				user_images = ""
				try:
					profile = UserProfile.objects(user_id=user)
					user_images = profile[0].images
					request.session['user_images'] = "/upload/" +user.username+"-avatar.jpg"
				except Exception as e:
					upro = UserProfile()
					upro.user_id = user
					upro.images = defaultUserImage
					upro.save()
					request.session['user_images'] = defaultUserImage
					print(e)
				context = 	{
							'user_images':user_images,
							}
				if nextpage:
					return HttpResponseRedirect(nextpage,context)	
				else:
					if is_mentor:
						return HttpResponseRedirect('/mentorview',context)	
					else:
						if is_join:
							return HttpResponseRedirect('/student-home',context)
						else:
							return HttpResponseRedirect('/search-mentor',context)
						#return HttpResponseRedirect('/search-mentor')
			else:
				c = {
						'error_message':"User name or password does not correct",
						'username':username,
						'password':password,
					}
				c.update(csrf(request))
				c.update(context_processors.user(request))
				return render_to_response("myapp/signin.html", c)
		except Exception as e:
				c = {
						'error_message':e,
					}
				c.update(csrf(request))
				c.update(context_processors.user(request))
				return render_to_response("myapp/signin.html", c)
	return render(request, 'myapp/signin.html', {})