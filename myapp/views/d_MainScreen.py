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

from myapp.models.Customer import Customer
from myapp.models.CusDebit import CusDebit



@login_required(login_url='/signin')
def index(request):
	try:
		user=User.objects.get(username=str(request.user))
		
		listcus = Customer.objects(debt_owner=user)
		cusdebitafterfilter = CusDebit.objects.filter(cus_id__in=listcus)
		
		for a in cusdebitafterfilter:
			print(a.cus_id.cus_id)
	except Exception as e:
		print(e)
	context={}
	return render(request, 'myapp/d-mainScreen.html', context)

	