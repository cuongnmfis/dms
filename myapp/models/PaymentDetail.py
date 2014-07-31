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
from myapp.models.Customer import Customer
from myapp.models.CusDebitDetail import CusDebitDetail

class PaymentDetail(Document):
	payment_id = ReferenceField(Payment)
	cus_debit_id = ReferenceField(CusDebit)
	cus_debit_detail_id =ReferenceField(CusDebitDetail)
	cus_id  = ReferenceField(Customer)
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
	listcus = Customer.getlistCustomerbyDebtOwner(debt_owner)
	paymentdetailafterfilter = PaymentDetail.objects.filter(cus_id__in=listcus)
	return paymentdetailafterfilter
