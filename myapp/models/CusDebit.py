'''
Created on Apr 3, 2014

@author: TuanNA
'''
from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import ReferenceField, StringField, DateTimeField,\
	FloatField

from myapp.models.Customer import Customer
from myapp.models.LoanType import LoanType

import myapp.models.Customer as Cus

class CusDebit(Document):
	cus_id  = ReferenceField(Customer)
	loan_type  = ReferenceField(LoanType)
	month = DateTimeField(default=datetime.now)
	debit = FloatField()
	total_debit = FloatField()
	rate = FloatField()
	cycle = FloatField()
	payment = FloatField()
	create_date = DateTimeField(default=datetime.now)
	loan_date = DateTimeField(default=datetime.now)
	last_close_date = DateTimeField(default=datetime.now)
	status = FloatField()
	note = StringField()
	meta = {
			'ordering': ['-create_date']
			}

def getCusDebitofadebtowner(debt_owner):
	listcus = Cus.getlistCustomerbyDebtOwner(debt_owner)
	cusdebitafterfilter = CusDebit.objects.filter(cus_id__in=listcus)
	return cusdebitafterfilter