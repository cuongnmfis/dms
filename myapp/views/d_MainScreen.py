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

from myapp.models.UserProfile import UserProfile

from myapp.models.Customer import Customer
from myapp.models.CusDebit import CusDebit
from myapp.models.CusDebit import getCusDebitofadebtowner
from dateutil.relativedelta import relativedelta
import datetime
@login_required(login_url='/signin')
def index(request):
	debt_owner1= User.objects.get(username=str(request.user))
	cus = Customer.objects(debt_owner = debt_owner1)
	numCus = len(cus)
	lscusdebt = getCusDebitofadebtowner(debt_owner1)
	numdebt = len(lscusdebt)
	
	data = []
	datenow = datetime.date.today()
	for i in 5:
		date1month = datenow + relativedelta(months=1)
		inmonth = CusDebit.objects(create_date__lt=datenow,create_date__gt=date1month) 
		data.append(len(inmonth))
		datenow = datenow + relativedelta(months=1)
		print(str(len(inmonth)))
	context={
			"numCus":numCus,
			"numdebt":numdebt
			}
	return render(request, 'myapp/d-mainScreen.html', context)

	