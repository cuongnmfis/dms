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

from myapp.models.Customer import Customer


#@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		context={}
		return render(request, 'myapp/d-NewCus.html', context)
	elif request.method == 'POST':
		firstname = request.POST['txtFirstName']
		lastname = request.POST['txtLastName']
		idNo = request.POST['txtidNo']
		Address = request.POST['txtAddress']
		HomeAddress = request.POST['txtHomeAddress']
		PhoneNumber = request.POST['txtPhoneNumber']
		About = request.POST['txaAbout']

		try:
			user_name='student'
			debt_owner=User.objects.get(username=user_name)
			
			user = User()
			user.username = firstname + lastname
			user.first_name = firstname
			user.last_name = lastname
			user.set_password(idNo);
			user.save()
			
			_customer = Customer()
			_customer.cus_id = user
			_customer.id_no = idNo
			_customer.cus_code=firstname
			_customer.address = Address
			_customer.home_address = HomeAddress
			_customer.fone_number = PhoneNumber
			_customer.about = About
			_customer.status = 1
			_customer.debt_owner = debt_owner
			_customer.save()
			
			user.backend = 'mongoengine.django.auth.MongoEngineBackend'
			context={"status":"success"}
			return render(request, 'myapp/d-mainScreen.html', context)
		except Exception as e:
			print(e)

	