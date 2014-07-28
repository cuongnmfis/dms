'''
Created on Apr 3, 2014

@author: TuanNA
'''
from datetime import datetime
import json

from django.conf.locale import fa
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from mongoengine.django.auth import User

from myapp.models import Comment, Student, Impression
from myapp.models.Curriculumn import Curriculumn
from myapp.models.CurriculumnLog import CurriculumnLog
from myapp.models.CurriculumnStudyProgress import CurriculumnStudyProgress
from myapp.models.Material import Material
from myapp.models.Mentor import Mentor
from myapp.models.ProgressType import ProgressType
from myapp.models.Statistic import Statistic
from myapp.models.StatisticDetail import StatisticDetail
from myapp.util import context_processors


@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		vCourse_id = request.GET['course_id']
		author_id=request.GET['user_id']
		author = User.objects.get(id=author_id)
		cl = Curriculumn.objects(id=vCourse_id)
		has_curriculum = False
		try:
			is_mentor = request.session['is_mentor']
		except Exception as e:
			is_mentor = False
		user=User.objects.get(username=str(request.user))
		student=Student.objects(user=user.id)
		status = "1"

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

		is_joined = False
		if len(student):
			progress = CurriculumnStudyProgress.objects(curriculumn=cl[0].id,student=student[0].id)
			if len(progress)>0:
				is_joined = True
		lscl = []
		lscl = cl[0]
		
		for i in lscl.__getattribute__('material'):
			i.note='0'
			try:
				is_like = StatisticDetail.objects(object_id=str(i.id),status=status,user=user.id)
				if len(is_like):
					i.note='1'
					i.__getattribute__('statistic').currentLikeNumber -=1
			except Exception as e:
				print(e)
		avatar = ""
		try:
			avatar = request.session['avatar']
		except Exception as e:
			request.session['avatar'] = ""
			print(e)
		
		context = {	'cl':lscl,
					'is_joined':is_joined,
					'user_id':request.user,
					'course_id':vCourse_id,
					'author_id':author_id,
					'author':author.username,
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
					'avatar':avatar
					}
		return render(request, 'myapp/course-detail.html', context)
	elif request.method == 'POST':
		if request.POST['posttype'] == "likeMaterial":
			user=User.objects.get(username=str(request.user))
			print(request.POST['posttype'])
			materialId=request.POST['materialId']
			status =request.POST['status']#like or dislike
			
			#update status=0 for recors last with status=1,user_id,material
			sdLast=StatisticDetail.objects(user=user.id,object_id=str(materialId),status='1').order_by('published_date')[:10]
			if len(sdLast):
				for sdUpdate in sdLast:
					sdUpdate.status='0'
					sdUpdate.save()
			else:
				print('no update ')
			sdNew=StatisticDetail()
			sdNew.user=user
			sdNew.object_id=str(materialId)
			if status =='0':
				sdNew.status='1'
			else :
				sdNew.status='0'
			sdNew.save()
			#update or insert statistic
			stCurent=Statistic.objects(object_id=str(materialId)).order_by('create_date')[:1]
			stNew=Statistic()
			if len(stCurent) >0:
				stNew=stCurent[0]
				if status == '1':
					stNew.currentLikeNumber -= 1
				else:
					stNew.currentLikeNumber += 1
				stNew.type='1'
				stNew.save()
			else:
				if status == '0':
					stNew.currentLikeNumber=1
				else:
					stNew.currentLikeNumber=0
				stNew.object_id=str(materialId)
				stNew.type='1'
				stNew.save()
			#update material 
			mtCurrent=Material.objects.get(id=materialId)
			mtCurrent.statistic=stNew
			mtCurrent.note='0'
			mtCurrent.save()
			
			return HttpResponse(json.dumps({"formdata": materialId}),content_type="application/json")
		elif request.POST['posttype']== "frmJoincourse":
			curriculum_id = request.POST['curriculum_id']
			user_id=request.POST['user_id']
			print(curriculum_id)
			curriculum = Curriculumn.objects.get(id=curriculum_id)
			
			user=User.objects.get(username=str(request.user))
			student=Student.objects(user=user.id)
			
			planstart = request.POST['planstart']
			planend = request.POST['planend']
			impression = request.POST['impression']
			description = request.POST['description']
			# Save CurriculumnStudyProgress
			csp = CurriculumnStudyProgress()
			if len(student) :
				st=student[0]
				csp.student=st
			csp.curriculumn = curriculum
			csp.PlanStartDate = datetime.strptime(planstart,'%m/%d/%Y')
			csp.PlanEndDate = datetime.strptime(planend,'%m/%d/%Y')
			csp.impression = Impression.objects.get(showpiority=impression)
			csp.description = description
			csp.save()
			
			#UPDATE Curriculumn
			print(user.id)
			curri=Curriculumn()
			
			curri = Curriculumn.objects.get(id=curriculum_id)
			curri.joined_user.append(user);
			
			curri.save()
			# Save CurriculumnLog
			lisProgressType = ProgressType.objects().order_by('rate')
			progressType =lisProgressType[0]
			
			curriLog=CurriculumnLog()
			
			curriLog.curriculumn=curri
			curriLog.process=progressType
			curriLog.data='[]'
			curriLog.user_id=user
			
			curriLog.save()
			#SHOW Record
			cl = Curriculumn.objects(id=curriculum_id)
			has_curriculum = False
			is_mentor=False
			mentor=Mentor.objects(user=user.id)
			if len(mentor):
				is_mentor=True
			if len(cl):
				has_curriculum = True
			print(has_curriculum)
			clTaken = 0
			clLike = 0
			mtTaken = 0
			mtLike = 0
			actTaken = 0
			actLike = 0
			mtTotal = 0
			actTotal = 0
			try:
				for c in cl:
					if c.statistic.currentTakenNumber:
						clTaken += c.statistic.currentTakenNumber
					if c.statistic.currentLikeNumber:
						clLike += c.statistic.currentLikeNumber
					for mt in c.material:
						if mt.statistic.currentTakenNumber:
							mtTaken += mt.statistic.currentTakenNumber
						if mt.statistic.currentLikeNumber:
							mtLike += mt.statistic.currentLikeNumber
							mtTotal += 1
					for act in c.action:
						if act.statistic.currentTakenNumber:
							actTaken += act.statistic.currentTakenNumber
						if act.statistic.currentLikeNumber:
							actLike += act.statistic.currentLikeNumber
							actTotal +=1
			except Exception as e:
				print(e)
			is_joined = False
			if len(student) :
				progress = CurriculumnStudyProgress.objects(curriculumn=cl[0].id,student=student[0].id)
				if len(progress)>0:
					is_joined = True
			context = {	'cl':cl[0],'is_joined':is_joined,
						'user_id':request.user,
						'course_id':curriculum_id,
						'author':user.username,
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
						}
			return HttpResponseRedirect('course-detail?course_id='+ curriculum_id +'&user_id='+user_id )
		elif request.POST['posttype']== "deleteComment":
			try:
				comment_status='0'
				comment_id=request.POST['hd_comment_id']
				course_id = request.POST['hd_course_id']
				author_id=request.POST['hd_author_course_id']
				user_id = request.session['_auth_user_id']
				
				cmt=Comment.objects.get(id=comment_id)
				cmt.status=comment_status
				cmt.save()
				status = "1"
				author = User.objects.get(id=author_id)
				cl = Curriculumn.objects(id=course_id)
				has_curriculum = False
				is_mentor = request.session['is_mentor']
				user=User.objects.get(username=str(request.user))
				student=Student.objects.get(user=user.id)
				
				
				
				clTaken = 0
				clLike = 0
				mtTaken = 0
				mtLike = 0
				actTaken = 0
				actLike = 0
				mtTotal = 0
				actTotal = 0
				try :
					for c in cl:
						if c.statistic.currentTakenNumber:
							c.statistic.currentTakenNumber=10
							clTaken += c.statistic.currentTakenNumber
						if c.statistic.currentLikeNumber:
							clLike += c.statistic.currentLikeNumber
						
						for mt in c.material:
							if mt.statistic.currentTakenNumber:
								mtTaken += mt.statistic.currentTakenNumber
							if mt.statistic.currentLikeNumber:
								mtLike += mt.statistic.currentLikeNumber
								mtTotal += 1
							print(mt.name)
						for act in c.action:
							if act.statistic.currentTakenNumber:
								actTaken += act.statistic.currentTakenNumber
							if act.statistic.currentLikeNumber:
								actLike += act.statistic.currentLikeNumber
								actTotal +=1
				except Exception as e:
					print(e)
					
				progress = CurriculumnStudyProgress.objects(curriculumn=cl[0].id,student=student.id)
				is_joined = False
				if len(progress)>0:
					is_joined = True
					
				lscl = []
				lscl = cl[0]
				for i in lscl.__getattribute__('material'):
					i.note='0'
					try:
						is_like = StatisticDetail.objects(object_id=str(i.id),status=status,user=user.id)
						if len(is_like):
							i.note='1'
							i.__getattribute__('statistic').currentLikeNumber -=1
					except Exception as e:
						print(e)
				
				context = {	'cl':lscl,'is_joined':is_joined,
							'user_id':request.user,
							'course_id':course_id,
							'author_id':author_id,
							'author':author.username,
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
							}
			except Exception as e:
				print(e)
			finally:
				return render(request, 'myapp/course-detail.html', context)
		elif request.POST['posttype']== "editComment":
			try:
				comment=request.POST['txtcommentName']
				comment_id=request.POST['hd_comment_id']
				course_id = request.POST['hd_course_id']
				author_id=request.POST['hd_author_course_id']
				user_id = request.session['_auth_user_id']
				
				cmt=Comment.objects.get(id=comment_id)
				cmt.content=comment
				cmt.save()
				status = "1"
				author = User.objects.get(id=author_id)
				cl = Curriculumn.objects(id=course_id)
				has_curriculum = False
				is_mentor = request.session['is_mentor']
				user=User.objects.get(username=str(request.user))
				student=Student.objects.get(user=user.id)
				
				
				
				clTaken = 0
				clLike = 0
				mtTaken = 0
				mtLike = 0
				actTaken = 0
				actLike = 0
				mtTotal = 0
				actTotal = 0
				try :
					for c in cl:
						if c.statistic.currentTakenNumber:
							c.statistic.currentTakenNumber=10
							clTaken += c.statistic.currentTakenNumber
						if c.statistic.currentLikeNumber:
							clLike += c.statistic.currentLikeNumber
						
						for mt in c.material:
							if mt.statistic.currentTakenNumber:
								mtTaken += mt.statistic.currentTakenNumber
							if mt.statistic.currentLikeNumber:
								mtLike += mt.statistic.currentLikeNumber
								mtTotal += 1
							print(mt.name)
						for act in c.action:
							if act.statistic.currentTakenNumber:
								actTaken += act.statistic.currentTakenNumber
							if act.statistic.currentLikeNumber:
								actLike += act.statistic.currentLikeNumber
								actTotal +=1
				except Exception as e:
					print(e)
					
				progress = CurriculumnStudyProgress.objects(curriculumn=cl[0].id,student=student.id)
				is_joined = False
				if len(progress)>0:
					is_joined = True
					
				lscl = []
				lscl = cl[0]
				for i in lscl.__getattribute__('material'):
					i.note='0'
					try:
						is_like = StatisticDetail.objects(object_id=str(i.id),status=status,user=user.id)
						if len(is_like):
							i.note='1'
							i.__getattribute__('statistic').currentLikeNumber -=1
					except Exception as e:
						print(e)
				
				context = {	'cl':lscl,'is_joined':is_joined,
							'user_id':request.user,
							'course_id':course_id,
							'author_id':author_id,
							'author':author.username,
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
							}
			except Exception as e:
				print(e)
			finally:
				return render(request, 'myapp/course-detail.html', context)
		else :
			comment = request.POST['txtComment']
			course_id = request.POST['hd_course_id']
			material_id = request.POST['hd_material_id']
			user_id = request.session['_auth_user_id']
			author_id=request.POST['hd_author_course_id']
			ur = request.user
			cmt = Comment()
			cmt.user = request.user
			cmt.content=comment
			cmt.save()
			cl = Curriculumn.objects.get(id=course_id)
			mt = Material.objects.get(id=material_id)
			mt.comment.append(cmt);
			mt.save()
			cl.save()
			status = "1"
			print(author_id)
			author = User.objects.get(id=author_id)
			cl = Curriculumn.objects(id=course_id)
			has_curriculum = False
			is_mentor = request.session['is_mentor']
			user=User.objects.get(username=str(request.user))
			student=Student.objects.get(user=user.id)
	
			clTaken = 0
			clLike = 0
			mtTaken = 0
			mtLike = 0
			actTaken = 0
			actLike = 0
			mtTotal = 0
			actTotal = 0
			try :
				for c in cl:
					if c.statistic.currentTakenNumber:
						c.statistic.currentTakenNumber=10
						clTaken += c.statistic.currentTakenNumber
					if c.statistic.currentLikeNumber:
						clLike += c.statistic.currentLikeNumber
					
					for mt in c.material:
						if mt.statistic.currentTakenNumber:
							mtTaken += mt.statistic.currentTakenNumber
						if mt.statistic.currentLikeNumber:
							mtLike += mt.statistic.currentLikeNumber
							mtTotal += 1
						print(mt.name)
					for act in c.action:
						if act.statistic.currentTakenNumber:
							actTaken += act.statistic.currentTakenNumber
						if act.statistic.currentLikeNumber:
							actLike += act.statistic.currentLikeNumber
							actTotal +=1
			except Exception as e:
				print(e)
				
			progress = CurriculumnStudyProgress.objects(curriculumn=cl[0].id,student=student.id)
			is_joined = False
			if len(progress)>0:
				is_joined = True
				
			lscl = []
			lscl = cl[0]
			for i in lscl.__getattribute__('material'):
				i.note='0'
				try:
					is_like = StatisticDetail.objects(object_id=str(i.id),status=status,user=user.id)
					if len(is_like):
						i.note='1'
						i.__getattribute__('statistic').currentLikeNumber -=1
				except Exception as e:
					print(e)
			
			context = {	'cl':lscl,'is_joined':is_joined,
						'user_id':request.user,
						'course_id':course_id,
						'author_id':author_id,
						'author':author.username,
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
						}
			return render(request, 'myapp/course-detail.html', context)