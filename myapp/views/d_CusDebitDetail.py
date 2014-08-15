'''
Created on Apr 3, 2014
@author: TuanNA
'''
# from dateutil.relativedelta import relativedelta
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from mongoengine.django.auth import User

from myapp.models import CusDebitDetailTrailer
from myapp.models.CusDebit import CusDebit
from myapp.models.CusDebitDetail import CusDebitDetail
from myapp.models.Customer import Customer
from myapp.models.Customer import getlistCustomerbyDebtOwner
from myapp.models.LoanType import LoanType
from myapp.views.CreateDms import createcusdebit, close_cycle_all,createMakePayment,createEstimatePayment,change_rate
from myapp.models.CusDebitDetail import getCusDebitDetailofadebtowner
from myapp.models.CusDebit import getCusDebitofadebtowner
@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		try:
			lsCDTT = CusDebitDetailTrailer.objects()
			if len(lsCDTT) > 0:
				for l in lsCDTT:
					l.delete()
				
			close_cycle_all()
			type_name =''
			user_name = str(request.user)
			debt_owner = User.objects.get(username=user_name)
			lsCusomer = getlistCustomerbyDebtOwner(debt_owner)
			lsCusDebit =  getCusDebitofadebtowner(debt_owner)
			lsCusDebitDetail = getCusDebitDetailofadebtowner(debt_owner)
			
			if 'type' in request.GET:
				if request.GET['type']=='loan':
					type_name = 'loan'
					type_post = 'loan'
				elif request.GET['type']=='payment':
					type_name = 'payment'
					type_post = 'payment'
		except Exception as ex:
			print(ex)
		finally:
			context = {'type':type_name,'type_post':type_post,'lsCusomer':lsCusomer,'lsCusDebit':lsCusDebit,'lsCusDebitDetail':lsCusDebitDetail}
		return render(request,'myapp/d-CustomerDebitDetail.html', context)
	elif request.method == 'POST':
		if request.POST['type'] == "cusLoan":
			try:
				
				cus_id = request.POST['hd_cus_id']
				Loan_date = datetime.strptime(request.POST['cus_loan_date'],'%m/%d/%Y')
				amount = float(request.POST['hd_cus_amount'])
				rate = float(request.POST['hd_cus_rate'])
				cycle = float(request.POST['cus_cycle'])
				note = ''
				if request.POST['txtnote'] :
					note = request.POST['txtnote']
					
				lt =LoanType.objects.get(code = 'LN',unit = 'D')
				cus =Customer.objects.get(id=cus_id)
				
				createcusdebit(cus, Loan_date, amount, rate, cycle, lt, note)
				
				#get data show on view
				print('add cusdebit ')
				type_name = 'payment'
				type_post = 'payment'
				
				user_name = str(request.user)
				debt_owner=User.objects.get(username = user_name)
				lsCusomer=getlistCustomerbyDebtOwner(debt_owner)
				lsCusDebit = getCusDebitofadebtowner(debt_owner)
				lsCusDebitDetail = getCusDebitDetailofadebtowner(debt_owner)
				
			except Exception as ex:
				print("cusLoan :"+ex)
			finally:
				context = {'type':type_name,'type_post':type_post,'lsCusomer':lsCusomer,'lsCusDebit':lsCusDebit,'lsCusDebitDetail':lsCusDebitDetail,'cus_id':cus_id}
				return render(request,'myapp/d-CustomerDebitDetail.html', context)
		elif request.POST['type'] == "estimatePayment":
			try:
				
				cus_id = request.POST['hd_payment_cus_id']
				payment_date = datetime.strptime(request.POST['cus_payment_date_payment'],'%m/%d/%Y')
				payment_amount = float(request.POST['hd_cus_amount_payment'])
				note=''
				if request.POST['txtnote'] :
					note = request.POST['txtnote']
					
				createEstimatePayment(cus_id, payment_date, payment_amount)
# 				get data show on view
				print("estimatePayment")
				type_name = 'payment'
				type_post = 'estimatePayment'
				
				user_name = str(request.user)
				debt_owner=User.objects.get(username=user_name)
				lsCusomer=getlistCustomerbyDebtOwner(debt_owner)
				lsCusDebit = getCusDebitofadebtowner(debt_owner)
				lsCusDebitDetail = CusDebitDetailTrailer.objects(status=1).order_by('cus_debit_id')
				
			except Exception as ex:
				print("estimatePayment: "+ex)
			finally:
				context = {'type':type_name,"type_post":type_post,'lsCusomer':lsCusomer,'lsCusDebit':lsCusDebit,'lsCusDebitDetail':lsCusDebitDetail,'cus_id':cus_id,'payment_date':payment_date,'payment_amount':payment_amount,'note':note }
				return render(request,'myapp/d-CustomerDebitDetail.html', context)
		elif request.POST['type'] == "changeRate":
			try:
				cus_debit_id = request.POST['hd_change_rate_cus_debit_id']
				cus_id = request.POST['hd_change_cus_id']
				
				cus_debit_detail_id = request.POST['hd_change_rate_cus_debit_detail_id']
				rate = 0
				if request.POST['txt_rate'] :
					rate = float(request.POST['txt_rate'])
# 				
				cusDebit = CusDebit.objects.get( id = cus_debit_id)
				cusDebitDetail = CusDebitDetail.objects.get( id = cus_debit_detail_id)
				
				change_rate(cusDebit, cusDebitDetail, rate)
				print('change rate')
				#get data to show view
				type_name = 'payment'
				type_post = 'payment'
				
				user_name = str(request.user)
				debt_owner = User.objects.get(username=user_name)
				lsCusomer = getlistCustomerbyDebtOwner(debt_owner)
				lsCusDebit = getCusDebitofadebtowner(debt_owner)
				lsCusDebitDetail = getCusDebitDetailofadebtowner(debt_owner)
			except Exception as ex:
				print("changeRate: "+ex)
			finally:
				context = {'type':type_name,"type_post":type_post,'lsCusomer':lsCusomer,'lsCusDebit':lsCusDebit,'lsCusDebitDetail':lsCusDebitDetail,'cus_id':cus_id }
				return render(request,'myapp/d-CustomerDebitDetail.html', context)
		elif request.POST['type'] == "makePayment":
			try:
				cus_id = request.POST['hd_payment_cus_id']
				payment_date = datetime.strptime(request.POST['cus_payment_date_payment'],'%m/%d/%Y')
				payment_amount = float(request.POST['hd_cus_amount_payment'])
				note=''
				if request.POST['txtnote'] :
					note = request.POST['txtnote']
				
				lt =LoanType.objects.get(code = 'LN',unit = 'D')
				cus = Customer.objects.get(id = cus_id)
				
				createMakePayment(cus_id, payment_date, payment_amount, lt,note)
				#get data to show view
				type_name = 'payment'
				type_post = 'makePayment'
				
				user_name = str(request.user)
				debt_owner = User.objects.get(username=user_name)
				lsCusomer = getlistCustomerbyDebtOwner(debt_owner)
				lsCusDebit = getCusDebitofadebtowner(debt_owner)
				lsCusDebitDetail = getCusDebitDetailofadebtowner(debt_owner)
			except Exception as ex:
				print("makePayment: "+ex)
			finally:
				context = {'type':type_name,"type_post":type_post,'lsCusomer':lsCusomer,'lsCusDebit':lsCusDebit,'lsCusDebitDetail':lsCusDebitDetail,'cus_id':cus_id }
				return render(request,'myapp/d-CustomerDebitDetail.html', context)