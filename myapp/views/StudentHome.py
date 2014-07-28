'''
Created on Apr 3, 2014
@author: TuanNA
'''
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from mongoengine.django.auth import User
from mongoengine.queryset.visitor import Q

from myapp.models.Curriculumn import Curriculumn
from myapp.models.CurriculumnLog import CurriculumnLog
from myapp.models.Material import Material
from myapp.util import context_processors


@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		#user = request.user
		user = User.objects.get(username=str(request.user))
		user_id = user.id
		lsCourse = []
		lsjoined = CurriculumnLog.objects(user_id = user_id)
		for ls in lsjoined:
			Course = Curriculumn.objects.get(id=ls.curriculumn.id)
			lsmt = []
			lsac = []
			for mt in Course.material:
				mt={"name":mt.name,"description":mt.description,"url": mt.url}
				lsmt.append(mt)
			if len(Course.action)>0:
				for ac in Course.action:
					ac={"name":ac.name,"description":ac.description}
					lsac.append(ac)
			lsCourseDetail={
							"id": Course.id,
							"author_id":Course.mentor.user.id,
							"name":Course.name,
							"duration":Course.duration,
							"duration_type":Course.duration_type,
							"from_date":Course.from_date,
							"lsmt":lsmt,
							"lsac":lsac
							}
			lsCourse.append(lsCourseDetail)
		#List recomment by admin
		lsRecomment = Curriculumn.objects().all().order_by('published_date')[:5]
		
		context = {	'lsCourse':lsCourse,
					'lsRecomment':lsRecomment
				}
		return render(request,'myapp/student-home.html', context)
	