# -*- coding: utf-8 -*-
'''
Created on Apr 3, 2014

@author: TuanNA
'''
from django.contrib.auth import logout, login
from django.core.context_processors import csrf
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from mongoengine.django.auth import User
import mongoengine.errors

from myapp.models.Student import Student
from myapp.models.UserProfile import UserProfile
from myapp.util import context_processors


def signupsns(request):
	user1=User.objects.get(username=str(request.user))
	thisstudent = Student.objects(user=user1.id)
	if len(thisstudent) > 0:
		request.session['is_mentor'] = False
	else: 
		studentnew = Student()
		studentnew.user = user1
		studentnew.save()
		request.session['is_mentor'] = False
	return HttpResponseRedirect('/search-mentor')
def index(request):
	firstname = "";
	lastname = "";
	username = "";
	password = "";
	email = "";
	if request.method == 'GET':
		return render(request, 'myapp/signup.html', {'rangerDay':range(1,32),'rangerYear':range(2014,1905,-1),})
	elif request.method == 'POST':
		firstname = request.POST['txtFirstName']
		lastname = request.POST['txtLastName']
		username = request.POST['txtUserName']
		password = request.POST['txtPassWord']
		email= request.POST['txtEmail']
		try:
			user = User()
			user.username = username
			user.first_name = firstname
			user.last_name = lastname
			user.email = email
			user.set_password(password);
			user.save()
			
			_profile = UserProfile()
			_profile.user_id = user
			_profile.save()
			
			st = Student()
			st.user = user
			st.save()
			
			user.backend = 'mongoengine.django.auth.MongoEngineBackend'
			logout(request)
			login(request, user)
			request.session['is_mentor'] = False
			return HttpResponseRedirect('/search-mentor')
		except mongoengine.errors.NotUniqueError as e:
				return getSignupError(request,'ユーザーはすでに存在しています！',firstname,lastname,username,password,email)
def getSignupError(request,e,firstname,lastname,username,password,email):
	c = {
			'error_message':e,
			'firstname':firstname,
			'lastname':lastname,
			'username':username,
			'password':password,
			'email':email,
			'rangerDay':range(1,31),
			'rangerYear':range(2014,1905,-1),
		}
	c.update(csrf(request))
	c.update(context_processors.user(request))
	return render_to_response("myapp/signup.html", c)