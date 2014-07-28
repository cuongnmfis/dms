from _io import StringIO
import hashlib
import json
import os

from PIL import Image
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from mongoengine import django
from mongoengine.django.auth import User

from myapp.forms import DocumentForm
from myapp.models.UserProfile import UserProfile


@login_required(login_url='/signin')
def index(request):
	form = DocumentForm()
	if request.method == 'GET':
		user=User.objects.get(username=str(request.user))
		thisupro = UserProfile.objects(user_id=user)[:1]
		context={"UserProfile":thisupro[0],'form': form}
		return render(request, 'myapp/account-setting.html', context)
	elif request.method == 'POST':
		form = DocumentForm()
		user=User.objects.get(username=str(request.user))
		thisupro = UserProfile.objects(user_id=user)[:1]
		fromType = request.POST['formType']
		if	fromType == "frmImage" :
			err_message=""
			
			try:
				form = DocumentForm(request.POST, request.FILES)
				if form.is_valid():
					handle_uploaded_image(request.user,request.FILES['image'],request)
					
			except Exception as e:
				print(e)
				err_message = e
			context={"UserProfile":thisupro[0],'form': form}
			return render(request, 'myapp/account-setting.html', context)
		elif fromType == "frmProfile" :
			err_message=""
			success=""
			try:
				txtJob = request.POST['txtJob']
				txtCompany = request.POST['txtCompany']
				txtWorking = request.POST['txtWorking']
				txtEducation = request.POST['txtEducation']
				txtSkill = request.POST['txtSkill']
				txaAbout = request.POST['txaAbout']
				user=User.objects.get(username=str(request.user))
				thisupro = UserProfile.objects(user_id=user)[:1]
				if len(thisupro)>0:
					supro=thisupro[0]
					supro.job_title = txtJob
					supro.company = txtCompany
					supro.work_field = txtWorking
					supro.edu = txtEducation
					supro.skill = txtSkill
					supro.about = txaAbout
					supro.save()
					success="success"
			except Exception as e:
				print(e)
				err_message = e
				success=e
			context={"UserProfile":thisupro[0],'form': form}
			return render(request, 'myapp/account-setting.html', context)
def handle_uploaded_file(user,f):
	folder_path = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__),os.pardir),os.pardir))+"/common/upload/"+user.username+"/";
	if os.path.isdir(folder_path) == False:
		os.makedirs(folder_path)
	with open(os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__),os.pardir),os.pardir))+"/common/upload/"+user.username+"/"+f.name, 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
def handle_uploaded_image(user,i,request):	
	try:
		imageImage = Image.open(i)
	except:
		print("Image was broken or not an image")
		
	size = (128, 128)
	imageImage.thumbnail(size)
	
	user=User.objects.get(username=str(request.user))
	thisuprolist = UserProfile.objects(user_id=user)[:1]
	userprofile = thisuprolist[0]
	userprofile.fileImage.put(imageImage, content_type='image/jpeg')
	userprofile.save()
	
	
	#folder_path = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__),os.pardir),os.pardir))+"/common/upload/";
	#if os.path.isdir(folder_path) == False:
	#	os.makedirs(folder_path)
	#with open(os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__),os.pardir),os.pardir))+"/common/upload/"+user.username+"-avatar.jpg", 'wb+') as destination:
	#	imageImage.save(destination)
	#request.session['user_images'] = "/upload/" +user.username+"-avatar.jpg"
	