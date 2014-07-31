# -*- coding: utf8 -*-
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
import mongoengine.errors
from django.core.context_processors import csrf
from myapp.util import context_processors
from django.shortcuts import render, render_to_response

from myapp.models.Customer import Customer


@login_required(login_url='/signin')
def index(request):
	debt_owner1= User.objects.get(username=str(request.user))
	firstname = ""
	lastname = ""
	idNo = ""
	Address = ""
	HomeAddress = ""
	PhoneNumber = ""
	About = ""
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
		type = request.POST['typeSave']
		
		try:
			
			
			user = User()
			
			user.username = firstname + lastname
			user.first_name = firstname
			user.last_name = lastname
			user.set_password(idNo);
			user.save()
			
			_customer = Customer()
			_customer.cus_id = user
			_customer.id_no = idNo
			_customer.first_name = firstname
			_customer.last_name = lastname
			_customer.full_name = firstname +' '+ lastname
			_customer.cus_code = lastname
			_customer.address = Address
			_customer.home_address = HomeAddress
			_customer.fone_number = PhoneNumber
			_customer.about = About
			_customer.status = 1
			_customer.debt_owner = debt_owner1
			_customer.save()
			
			user.backend = 'mongoengine.django.auth.MongoEngineBackend'
		except mongoengine.errors.NotUniqueError as e:
			return getNewCusError(request,'Đã tồn tại trong hệ thống',firstname,lastname,idNo,Address,HomeAddress,PhoneNumber,About)
		if type == "normalsave":
			return HttpResponseRedirect('/newcustomer')			
		elif type == "saveandredirect":
			return HttpResponseRedirect('/custom-debit-detail?type=loan')
def getNewCusError(request,e,firstname,lastname,idNo,address,homeaddress,phonenumber,about):
	c = {
			'error_message':e,
			'firstname':firstname,
			'lastname':lastname,
			'txtidNo':idNo,
			'txtAddress':address,
			'txtHomeAddress':homeaddress,
			'txtPhoneNumber':phonenumber,
			'txtAbout':about,
			'rangerDay':range(1,31),
			'rangerYear':range(2014,1905,-1),
		}
	c.update(csrf(request))
	c.update(context_processors.user(request))
	return render_to_response("myapp/d-NewCus.html", c)