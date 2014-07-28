'''
Created on Apr 3, 2014

@author: TuanNA
'''
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from mongoengine.django.auth import User

from myapp.models import MentorPost


@login_required(login_url='/signin')
def mypost(request):
	vuser_id = request.session['_auth_user_id']
	print(vuser_id)
	#post = MentorPost.objects.get(user_id=vuser_id)
	posts = MentorPost.objects(user_id=User.objects.get(id=request.session['_auth_user_id']))
	context = {'posts':posts,'user_type':request.session['user_type']}
	return render(request,'myapp/index.html', context)