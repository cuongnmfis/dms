'''
Created on Apr 3, 2014

@author: TuanNA
'''
from datetime import datetime

from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import ReferenceField, DateTimeField,\
	FloatField, IntField

from myapp.models.CusDebit import CusDebit
from myapp.models.Customer import Customer

import myapp.models.Customer as Cus

class CusDebitDetail(Document):
	cus_id  = ReferenceField(Customer)
	cus_debit_id  = ReferenceField(CusDebit)
	from_date= DateTimeField(default=datetime.now)
	to_date= DateTimeField(default=datetime.now)
	rate = FloatField()
	start_cycle = FloatField()
	amount = FloatField()
	payment = FloatField()
	end_cycle = FloatField()
	debit = FloatField()
	status = FloatField()
	days = FloatField()
	create_date= DateTimeField(default=datetime.now)
	is_current_month = FloatField()
	flag = IntField(default=0)
	index = IntField()
	meta = {
			'ordering': ['-create_date']
			}
# retrive all record in CusDebitDetail that have specific input debt_owner 
def getCusDebitDetailofadebtowner(debt_owner):
	listcus = Cus.getlistCustomerbyDebtOwner(debt_owner)
	cusdebitdetailafterfilter = CusDebitDetail.objects.filter(cus_id__in=listcus)
	return cusdebitdetailafterfilter

def getCusDebitDetailbyCusdebitID(cusdebit_ID):
	listcus = Cus.getlistCustomerbyDebtOwner(debt_owner)
	cusdebitdetailafterfilter = CusDebitDetail.objects.filter(cus_id__in=listcus)
	return cusdebitdetailafterfilter