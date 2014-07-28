'''
Created on Apr 3, 2014

@author: ducdienpt
'''
from django.core.context_processors import csrf
from django.shortcuts import render, render_to_response
from mongoengine.django.auth import User

from myapp.models import UserProfile
from myapp.util import context_processors

def index(request):
	lisUserProfile = UserProfile.objects
# 	print('begin')
# 	for user in lisUserProfile:
# 		print(user.images)
# 	print('finish')
	c = {'lisUserProfile':lisUserProfile,}
	if request.method == 'GET':
		return render(request, 'myapp/people-directory.html', c)
	elif request.method == 'POST':
		try:
			keyword = request.POST['keyword']
			users = User.objects(first_name__icontains=keyword)#search data
			lisUserProfile = UserProfile.objects(user_id__in=users)
			c = {'lisUserProfile':lisUserProfile,'keyword':keyword}
# 			profile = Profile()
# 			profile.name = 'Nusja Nawancali'
# 			profile.image_url='images/user3.png'
# 			profile.address='Phuket, Thailand'
# 			profile.location='Product Manager'
# 			profile.company='SomeCompany, Inc.'
# 			profile.save()

			#get data from mongodb
			c.update(csrf(request))
			c.update(context_processors.user(request))
			return render_to_response("myapp/people-directory.html", c)
		except Exception:
			c.update(csrf(request))
			c.update(context_processors.user(request))
			return render_to_response("myapp/people-directory.html", c)
	return render(request, 'myapp/test.html', c)