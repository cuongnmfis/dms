'''
Created on Apr 3, 2014

@author: ducdienpt
'''

from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.shortcuts import render, render_to_response
from mongoengine.django.auth import User
from mongoengine.queryset.visitor import Q

from myapp.models import UserProfile, Curriculumn, Category
from myapp.models.Mentor import Mentor
from myapp.util import context_processors


@login_required(login_url='/signin')
def index(request):
	lisUserProfile = {}
# 	listParentCategory = Category.objects(parentCategory = None)
	lisCategory =Category.objects()
# 	print('begin')
# 	for user in listCategory:
# 		if user.parentCategory is not None :
# 			print(user.parentCategory.categoryName)
# 	print('finish')
	
	if len(lisCategory) > 0:
		category=lisCategory[0]
		c = {'lisUserProfile':lisUserProfile,'listCategory':lisCategory,'category':category}
	else:
		c = {'lisUserProfile':lisUserProfile,'listCategory':lisCategory}
	if request.method == 'GET':
		return render(request, 'myapp/search-mentor.html', c)
	elif request.method == 'POST':
		
		try:
			lisUserProfile={}
			listCurriculumn={}
			lisCategory =Category.objects()
			user=User.objects.get(username=str(request.user))
			mentor=Mentor.objects(user=user.id)
			
			keyword = request.POST['search']
			parentCategory = request.POST['parentCategory'];
			childrenCategory =request.POST['childrenCategory'];
			#search data
# 			users = User.objects(Q(first_name__icontains=keyword) | Q(last_name__icontains=keyword))
# 			lisUserProfile = UserProfile.objects(user_id__in=users,is_mentor=True)
			
# 			categoryObject =Category.objects.get(id=childrenCategory)
			if len(mentor)>0:
				mt=mentor[0]
				listCurriculumn =Curriculumn.objects(category=childrenCategory ,name__icontains=keyword).order_by('published_date')
			else:
				listCurriculumn =Curriculumn.objects(category=childrenCategory ,name__icontains=keyword).order_by('published_date')
# 			listCurriculumn =Curriculumn.objects(name__icontains=keyword)
			c = {'lisUserProfile':lisUserProfile,'listCurriculumn':listCurriculumn,'listCategory':lisCategory,'search':keyword,'parentCategory':parentCategory,'childrenCategory':childrenCategory}
			#get data from mongodb
			c.update(csrf(request))
			c.update(context_processors.user(request))
			return render_to_response("myapp/search-mentor.html", c)
		except Exception:
			lisUserProfile={}
			listCurriculumn={}
			lisCategory =Category.objects()
			user=User.objects.get(username=str(request.user))
			mentor=Mentor.objects(user=user.id)
			keyword = request.POST['search']
			parentCategory = request.POST['parentCategory'];
			if len(mentor)>0:
				mt=mentor[0]
				listCurriculumn =Curriculumn.objects(name__icontains=keyword).order_by('published_date')
			else:
				listCurriculumn =Curriculumn.objects(name__icontains=keyword).order_by('published_date')
			c = {'lisUserProfile':lisUserProfile,'listCurriculumn':listCurriculumn,'listCategory':lisCategory,'search':keyword,'parentCategory':parentCategory}
			c.update(csrf(request))
			c.update(context_processors.user(request))
			return render_to_response("myapp/search-mentor.html", c)
	return render(request, 'myapp/search-mentor.html', c)