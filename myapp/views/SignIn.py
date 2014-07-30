'''
Created on Apr 3, 2014

@author: TuanNA
'''
from django.contrib.auth import logout, login
from django.core.context_processors import csrf
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from mongoengine.django.auth import User

from myapp.models.UserProfile import UserProfile
from myapp.util import context_processors


def index(request):
	username = ""
	password = ""
	defaultUserImage = "/images/avatar/default.png"
	
	if 'next' in request.GET:
		nextpage = request.GET['next']
	else:
		nextpage = ""
			
	if request.method == 'GET':
		return render(request, 'myapp/signin.html', {})
	elif request.method == 'POST':
		username = request.POST['txtUserName']
		password = request.POST['txtPassWord']
		
		try: 
			
			user = User.objects.get(username=username)
			
			if user.check_password(password):
				logout(request)
				user.backend = 'mongoengine.django.auth.MongoEngineBackend'
				login(request, user)


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
					return HttpResponseRedirect('/mainscreen')
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