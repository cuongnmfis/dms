#!/usr/bin/env python
# -*- coding: utf8 -*-
'''
Created on Apr 3, 2014
@author: TuanNA
'''

import json

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from mongoengine.django.auth import User

from myapp.models.CurriculumnLog import CurriculumnLog
from myapp.models.ProgressType import ProgressType


@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		
		username=request.user
		user=User.objects.get(username=str(request.user))
		
		listProgress = ProgressType.objects().order_by('rate')
		listcurrilog = CurriculumnLog.objects(user_id=user).order_by('process','published_date','-curriculumn')
		
		if len(listcurrilog)>0:
			currilog=listcurrilog[0]
		datalog="[]"
		flag = '0' ;
		if len(listcurrilog) > 0:
			flag = '1'
		if len(listcurrilog)>0:
			context = {'username':username,
						'listProgress' : listProgress,
						'listcurrilog': listcurrilog,
						'datalog': datalog,
						'firstcurrilog':currilog,
						'flag' : flag
					}
		else:
			context = {'username':username,
						'listProgress' : listProgress,
						'listcurrilog': listcurrilog,
						'datalog': datalog,
						'flag' : flag
					}
		return render(request,'myapp/studyLog.html', context)
	
	elif request.method == 'POST':
		fromType = request.POST['formType']
		if	fromType == "frmCalendar" :
			err_message="Error: "
			try:
				datacontent = request.POST['datacontent']
				currilogid = request.POST['curriculumnlog_id']
				user=User.objects.get(username=str(request.user))
				currilog = CurriculumnLog.objects(id=currilogid)[:1]
				
				
				if len(datacontent) >0:
					if len(currilog) <= 0:
						err_message += "can not find curriculumn_log "
					else:
						err_message="[Start update]"
						print('update')
						cl=currilog[0]
# 						s=datacontent.decode('utf-8')
						cl.data=str(datacontent.encode('utf-8'))
						cl.save()
						err_message +="-[success]"
						err_message += "-[Finish update]"
				else:
					err_message += "can not find data content "
			except Exception as e:
				print(e)
				err_message = e
			finally:
				return HttpResponse(json.dumps({"formdata": err_message,"datacontent":datacontent,"currilogid":currilogid }),content_type="application/json")
		elif fromType == "frmProgress" :
			err_message=""
			
			try:
				
				currilogid = request.POST['curriculumnlog_progress_id']
				progressid = request.POST['progress_id']
				
				currilog = CurriculumnLog.objects(id=currilogid)[:1]
				newprogress = ProgressType.objects(id=progressid)[:1]
				print(currilogid)
				print(progressid)
				cl = currilog[0]
				cl.process = newprogress[0]
				cl.save()
				success="successful"
			except Exception as e:
				print(e)
				err_message = e
			return HttpResponse(json.dumps({"formdata": err_message,"success": success}),content_type="application/json")