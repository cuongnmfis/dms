'''
Created on Apr 3, 2014

@author: TuanNA
'''
from datetime import datetime

from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import ReferenceField, DateTimeField,\
	FloatField
import myapp.models.Customer as Cus

class Payment(Document):
	cus_id  = ReferenceField(User)
	create_date= DateTimeField(default=datetime.now)
	pay_date= DateTimeField(default=datetime.now)
	amount = FloatField()
	status = int()
	meta = {
			'ordering': ['-create_date']
			}

def getPaymentofadebtowner(debt_owner):
	listcus = Cus.getlistCustomerbyDebtOwner(debt_owner)
	paymentafterfilter = Payment.objects.filter(cus_id__in=listcus)
	return paymentafterfilter