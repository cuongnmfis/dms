'''
Created on Apr 3, 2014

@author: TuanNA
'''
from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import ReferenceField, DateTimeField,\
	FloatField
import myapp.models.Customer as Customer

class Payment(Document):
	cus_id  = ReferenceField(Customer)
	create_date= DateTimeField(default=datetime.now)
	pay_date= DateTimeField(default=datetime.now)
	amount = FloatField()
	status = int()
	meta = {
			'ordering': ['-create_date']
			}

def getPaymentofadebtowner(debt_owner):
	listcus = Customer.getlistCustomerbyDebtOwner(debt_owner)
	paymentafterfilter = Payment.objects.filter(cus_id__in=listcus)
	return paymentafterfilter