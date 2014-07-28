'''
Created on Apr 3, 2014

@author: TuanNA
'''
import os

from django.contrib.auth.decorators import login_required
from django.core.context_processors import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from mongoengine.django.auth import User

from myapp.forms import DocumentForm
from myapp.models import UserProfile
from myapp.models.Documents import Documents
from PIL import Image


@login_required(login_url='/signin')
def index(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		# Redirect to the document list after POST
		if form.is_valid():
			handle_uploaded_file(request.user,request.FILES['docfile'])
		return HttpResponseRedirect("")
	else:
		form = DocumentForm() # A empty, unbound form
		# Load documents for the list page
		documents = Documents.objects.all()
		user=User.objects.get(username=str(request.user))
		up = UserProfile.objects.get(user_id=user.id)
		user_image = up.images
		print(user_image)
			# Render list page with the documents and the form
	return render_to_response(
							'myapp/documents.html',
							{'documents': documents, 
							'form': form,
							'user_image':user_image,
							},
							context_instance=RequestContext(request)
							)
def handle_uploaded_file(user,f):
	folder_path = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__),os.pardir),os.pardir))+"/common/upload/"+user.username+"/";
	print(f.name)
	print(user)
	if os.path.isdir(folder_path) == False:
		os.makedirs(folder_path)
	with open(os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__),os.pardir),os.pardir))+"/common/upload/"+user.username+"/"+f.name, 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
	update_user_image(user,f.name)
	imageResize(folder_path+f.name)
def	update_user_image(vuser,filename):
	user=User.objects.get(username=str(vuser))
	up = UserProfile.objects.get(user_id=user.id)
	print('/upload/' + str(vuser) + '/' + filename)
	newimage = '/upload/' + str(vuser) + '/' + filename
	print(newimage)
	up.images = newimage
	up.save()
def imageResize(filepath):
    file_dir=os.path.split(filepath)
    img = Image.open(filepath)

    if img.size[0] > img.size[1]:
        aspect = img.size[1]/120
        new_size = (img.size[0]/aspect, 120)
    else:
        aspect = img.size[0]/120
        new_size = (120, img.size[1]/aspect)
    img.resize(new_size).save(file_dir[0]+'/ico'+file_dir[1][3:])
    img = Image.open(file_dir[0]+'/ico'+file_dir[1][3:])

    if img.size[0] > img.size[1]:
        new_img = img.crop( (
            (((img.size[0])-120)/2),
            0,
            120+(((img.size[0])-120)/2),
            120
        ) )
    else:
        new_img = img.crop( (
            0,
            (((img.size[1])-120)/2),
            120,
            120+(((img.size[1])-120)/2)
        ) )

    new_img.save(file_dir[0]+'/ico'+file_dir[1][3:])