'''
Created on Apr 3, 2014

@author: TuanNA
'''
from datetime import datetime

from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import ReferenceField, DateTimeField,\
	FloatField

from myapp.models.CusDebit import CusDebit
from myapp.models.Payment import Payment
import myapp.models.Customer as Cus

class PaymentDetail(Document):
	payment_id = ReferenceField(Payment)
	cus_debit_id = ReferenceField(CusDebit)
	cus_id  = ReferenceField(User)
	create_date= DateTimeField(default=datetime.now)
	pay_date= DateTimeField(default=datetime.now)
	debit = FloatField()
	payment = FloatField()
	remain = FloatField()
	status = int()
	meta = {
			'ordering': ['-create_date']
			}

def getPaymentdetailofadebtowner(debt_owner):
	listcus = Cus.getlistCustomerbyDebtOwner(debt_owner)
	paymentdetailafterfilter = PaymentDetail.objects.filter(cus_id__in=listcus)
	return paymentdetailafterfilter
