'''
Created on Apr 3, 2014

@author: TuanNA
'''
from datetime import datetime

from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import ReferenceField, StringField, DateTimeField ,\
	FloatField


class Customer(Document):
	cus_id  = ReferenceField(User)
	cus_code = StringField()
	first_name = StringField()
	last_name = StringField()
	full_name = StringField()
	id_no = StringField()
	address = StringField()
	home_address = StringField()
	fone_number = StringField()
	create_date = DateTimeField(default=datetime.now)
	status = FloatField()
	about = StringField()
	debt_owner =ReferenceField(User)
	meta = {
			'ordering': ['-create_date']
			}
	
def getlistCustomerbyDebtOwner(debt_owner):
	return Customer.objects(debt_owner=debt_owner)
	