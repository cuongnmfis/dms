'''
Created on Apr 3, 2014
@author: TuanNA
'''
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from mongoengine.django.auth import User

from myapp.models.Curriculumn import Curriculumn
from myapp.models.Mentor import Mentor
from myapp.util import context_processors
from myapp.models.Category import Category


@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
# 		cl = Curriculumn.objects(mentor=mentor)
# 		mentor = Mentor.objects.get(user=re)
# 		mentor_id = '5375ce146c02298c9af00e00'
		lisCategory =Category.objects()
		user_id=request.GET['user_id']
		user = User.objects.get(id=user_id)
		mentor = Mentor.objects.get(user=user)
		cl = Curriculumn.objects(mentor=mentor)
		has_curriculum = False
		is_mentor = False
		try:
			is_mentor = request.session['is_mentor']
		except Exception as e:
			print(e)
		if len(cl):
			has_curriculum = True
		clTaken = 0
		clLike = 0
		mtTaken = 0
		mtLike = 0
		actTaken = 0
		actLike = 0
		mtTotal = 0
		actTotal = 0
		for c in cl:
			if len(c.joined_user)>0 :
				for u in c.joined_user:
					print(u)
		context = {'user_id':user_id,
					'username':request.user,
					'cl':cl,
					'author':mentor.user.username,
					'author_id':user_id,
					'is_mentor':is_mentor,
					'clTaken':clTaken,
					'clLike':clLike,
					'mtTaken':mtTaken,
					'mtLike':mtLike,
					'actTaken':actTaken,
					'actLike':actLike,
					'mtTotal':mtTotal,
					'actTotal':actTotal,
					'has_curriculum':has_curriculum,
					'listCategory':lisCategory,}
		return render(request,'myapp/studentview.html', context)