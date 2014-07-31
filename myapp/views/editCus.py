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
from myapp.models.Customer import getlistCustomerbyDebtOwner

@login_required(login_url='/signin')
def index(request):
	debt_owner1= User.objects.get(username=str(request.user))
	if request.method == 'GET':
		lsCusomer = getlistCustomerbyDebtOwner(debt_owner1)
		context={'lsCusomer':lsCusomer}
		return render(request, 'myapp/editCus.html', context)
	elif request.method == 'POST':
		firstname = request.POST['txtFirstName']
		lastname = request.POST['txtLastName']
		idNo = request.POST['txtidNo']
		Address = request.POST['txtAddress']
		HomeAddress = request.POST['txtHomeAddress']
		PhoneNumber = request.POST['txtPhoneNumber']
		About = request.POST['txaAbout']
		type = request.POST['typeSave']
		cusID = request.POST['cusID']
		
		try:
			
			
			#user = User()
			
			#user.username = firstname + lastname
			#user.first_name = firstname
			#user.last_name = lastname
			#user.set_password(idNo);
			#user.save()
			cus = Customer.objects(id=cusID)[:1]
			_customer=cus[0]
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
			#user.backend = 'mongoengine.django.auth.MongoEngineBackend'
		except Exception:
			print(Exception)
		
		if type == "normalsave":
			return HttpResponseRedirect('/editCus')			
		elif type == "saveandredirect":
			return HttpResponseRedirect('/custom-debit-detail?type=loan')