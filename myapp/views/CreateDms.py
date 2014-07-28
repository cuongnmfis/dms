'''
Created on Apr 3, 2014
@author: TuanNA
'''
from datetime import date, datetime, time
from dateutil.relativedelta import relativedelta

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from mongoengine.django.auth import User
from mongoengine.fields import ReferenceField

from myapp.models.CusDebit import CusDebit
from myapp.models.CusDebitDetail import CusDebitDetail
from myapp.models.Customer import Customer
from myapp.models.Payment import Payment
from myapp.models.PaymentDetail import PaymentDetail

@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		try:
			user=request.user
			#createcustomer(user)
			#createcusdebit(user)
			#close_cycle_all()
			getCustomerDebitInfo(user)
		except Exception as ex:
			print(ex)
		context = {'msg':'done'}
		return render(request,'myapp/CreateDms.html', context)

def getCustomerInfo(ownner):
	customer = Customer.objects(debt_owner = ownner)
	return customer
def getCustomerDebitInfo(owner):
	listcus =  getCustomerInfo(owner)
	allcustomerdebit = CusDebit.objects()
	cusdebitafterfilter  = []
	for	l in listcus:
		for cd in allcustomerdebit:
			if(cd.cus_id ==l.cus_id):
				cusdebitafterfilter.append(cd)
	for aaa  in cusdebitafterfilter:
		print(aaa.cus_id)
	
	
	cusdebitafterfilter = CusDebit.objects.filter(cus_id__in=listcus)
	for aaa  in cusdebitafterfilter:
		print(aaa.cus_id)
	
	
	return cusdebitafterfilter

def getCustomerDebitDetail():
	listcus =  getCustomerInfo()
	allcustomerdebitdetail = CusDebitDetail.objects()
	cusdebitdetailafterfilter  = []
	for	l in listcus:
		for cdd in allcustomerdebitdetail:
			if(cdd.cus_id == l.cus_id ):
				cusdebitdetailafterfilter.append(cdd)
	return cusdebitdetailafterfilter

def getPaymentHistory():
	listcus =  getCustomerInfo()
	allpaymentdetail = Payment.objects()
	paymentafterfilter  = []
	for	l in listcus:
		for pm in allpaymentdetail:
			if(pm.cus_id == l.cus_id ):
				paymentafterfilter.append(pm)
	return paymentafterfilter
def createMakePayment(vCus_id,vPayment_date,vPayment,loan_type):
	
		cus=Customer.objects.get(id=vCus_id)
		lsCusDebit =CusDebit.objects(cus_id = cus.id,status = 1).order_by('loan_date')
		createEstimatePayment(vCus_id,vPayment_date,vPayment)
	
	#	create new a payment
		p = Payment()
		p.cus_id = cus
		p.pay_date = vPayment_date
		p.amount = vPayment
		p.status = 1
		p.save()
		
		for cusDebit in lsCusDebit :
					cs=cusDebit
					if cs.total_debit_trailer > 0 and cs.total_debit_trailer < cs.total_debit :
						
						lsCus_debit_detail = CusDebitDetail.objects(cus_debit_id = cs.id)
						for c in lsCus_debit_detail :
							c.delete()
					
						lsCus_debit_detail_trailer = CusDebitDetailTrailer.objects(cus_debit_id = cs.id)
						for  Cus_debit_detail_trailer in lsCus_debit_detail_trailer:
							cdt = Cus_debit_detail_trailer
							
							cd = CusDebitDetail()
							
							cd.cus_id  = cdt.cus_id
							cd.cus_debit_id  = cdt.cus_debit_id
							cd.from_date= cdt.from_date
							cd.to_date= cdt.to_date
							cd.rate = cdt.rate
							cd.start_cycle = cdt.start_cycle
							cd.amount = cdt.amount
							cd.payment = cdt.payment
							cd.end_cycle = cdt.end_cycle
							cd.debit = cdt.debit
							cd.status = cdt.status
							cd.days = cdt.days
							cd.create_date= cdt.create_date
							cd.flag = cdt.flag
							cd.index = cdt.index
							
							cd.save()
							
						cus_debit_detail_trailer = CusDebitDetailTrailer.objects.get(cus_debit_id = cs.id,flag = 1)
						
						cs.total_debit =cs.total_debit_trailer
						cs.status = 0
						cs.payment = cus_debit_detail_trailer.payment
						cs.last_close_date = cus_debit_detail_trailer.to_date
						
						cs.save()
						
						#insert payment_detail
						pd = PaymentDetail()
						pd.payment_id = p
						pd.cus_debit_id = cs
						pd.cus_id = cus
						pd.debit = cus_debit_detail_trailer.payment
						pd.payment = cus_debit_detail_trailer.payment
						pd.cus_debit_detail_id = cus_debit_detail_trailer
						pd.status = 1
						
						pd.save()
						
						#insert record missing
						createcusdebit(cus,cs.last_close_date,cs.total_debit,cs.rate,cs.cycle,loan_type,'')
						
					elif cs.total_debit_trailer == 0 :
						print("update status=0")
						cus_debit_detail_trailer = CusDebitDetailTrailer.objects.get(cus_debit_id = cs.id,flag = 1)
						
						cs.total_debit =cs.total_debit_trailer
						cs.status = 0
						cs.payment = cus_debit_detail_trailer.payment
						cs.last_close_date = cus_debit_detail_trailer.to_date
						
						cs.save()
						
						#insert payment_detail
						pd = PaymentDetail()
						pd.payment_id = p
						pd.cus_debit_id = cs
						pd.cus_id = cus
						pb.debit = cus_debit_detail_trailer.payment
						pd.payment = cus_debit_detail_trailer.payment
						pb.cus_debit_detail_id = cus_debit_detail_trailer
						pd.status = 1
						
						pd.save()
						
					elif cs.total_debit_trailer == cs.total_debit :
						print("no update ")
def createEstimatePayment(vCus_id,vPayment_date,vPayment_trailer):
	try:
		lsCDTT = CusDebitDetailTrailer.objects()
		for l in lsCDTT:
			l.delete()
			
		cus_id = vCus_id
		payment_date=vPayment_date
		payment_trailer = vPayment_trailer
				
		cus=Customer.objects.get(id=cus_id)
		lsCusDebit =CusDebit.objects(cus_id = cus.id,status = 1).order_by('loan_date')
#  		estimate payment
		for cus_debit in lsCusDebit :
			insert_missing_debit_detail_trailer(cus,cus_debit,cus_debit.loan_date,payment_date,cus_debit.debit,cus_debit.rate)
		for cus_debit_temp in lsCusDebit :
			cus_debit = cus_debit_temp
			if payment_trailer > 0:
				if payment_trailer < cus_debit.total_debit_trailer:
					cus_debit.total_debit_trailer -= payment_trailer
# 							cus_debit.payment = payment_trailer
					
					cus_debit_detail_last =CusDebitDetailTrailer.objects.get(cus_debit_id =cus_debit.id ,flag=1)
					
					cus_debit_detail_last.payment = payment_trailer
					cus_debit_detail_last.status = 0
					cus_debit_detail_last.end_cycle = cus_debit.total_debit_trailer
					cus_debit_detail_last.payment = payment_trailer
					payment_trailer = 0
					cus_debit_detail_last.save()
					cus_debit.save()
				else :
					payment_trailer -= cus_debit.total_debit_trailer
					cus_debit_detail_last =CusDebitDetailTrailer.objects.get(cus_debit_id =cus_debit.id ,flag=1)
					
					cus_debit_detail_last.status = 0
					cus_debit_detail_last.end_cycle = 0
					cus_debit_detail_last.payment = cus_debit.total_debit_trailer
					cus_debit.total_debit_trailer = 0
					cus_debit_detail_last.save()
					cus_debit.save()
	except Exception as ex:
		print("createEstimatePayment: "+ex)
def getPaymentDetail():
	listcus =  getCustomerInfo()
	allpaymentdetaildetail = PaymentDetail.objects()
	paymentdetailafterfilter  = []
	for	l in listcus:
		for pmd in allpaymentdetaildetail:
			if(pmd.cus_id == l.cus_id ):
				paymentdetailafterfilter.append(pmd)
	return paymentdetailafterfilter
	
def createcustomer(user,id_no, address,home_address, fone_number, about):
		try:
			vtoday = date.today()
			ct = Customer()
			ct.cus_id= user
			ct.cus_code = user.username
			ct.first_name = user.first_name
			ct.last_name = user.last_name
			ct.full_name = user.first_name + user.last_name
			ct.id_no = id_no
			ct.address = address
			ct.home_address = home_address
			ct.fone_number = fone_number
			ct.create_date = vtoday
			ct.status = 1
			ct.about = about
			ct.save()
		except Exception as ex:
			print(ex)
def createcusdebit(vUser, vLoan_date, vAmount, vRate,vCycle,vLoan_type,vNote):
		try:
			vtoday = date.today()
			cd = CusDebit()
			cd.cus_id  = vUser
			cd.month = vLoan_date
			cd.debit = vAmount
			cd.total_debit = vAmount
			cd.payment = 0.00
			cd.create_date = vtoday
			cd.loan_date = vLoan_date
			cd.loan_type = vLoan_type
			cd.rate = vRate
			cd.cycle = vCycle
			cd.status = 1
			cd.note =vNote
			cd.save()
			createcusdebitdetail(vUser,cd,vLoan_date,vAmount,vRate)
		except Exception as ex:
			print("createcusdebit: "+ex)
def createcusdebitdetail(vUser,vCus_debit,vLoan_date,vAmount,vRate):
		try:
			vtoday = datetime.strptime(str(date.today()),'%Y-%m-%d')
			print(vCus_debit.loan_date)
			vLoan_cycles = (float(str((vtoday - vLoan_date).days)) +1 )/vCus_debit.cycle
			print('Loan cycles: '+str(vLoan_cycles))
			close_cycle_cus(vUser,vLoan_date,vAmount,vRate,vCus_debit.cycle,vCus_debit)
		except Exception as ex:
			print("createcusdebitdetail: "+ex)
def close_cycle_all():
		try:
			vtoday = datetime.strptime(str(date.today()),'%Y-%m-%d')
			lscd = CusDebit.objects(last_close_date__lt = vtoday ).order_by('loan_date')
			for cd in lscd :
				cus=Customer.objects.get(id=cd.cus_id.id)
				cus_debit_detail=CusDebitDetail.objects.get(cus_debit_id=cd.id,flag = 1)
				insert_missing_debit_detail_test(cus, cd, cus_debit_detail)
		except Exception as ex:
			print(ex)
def close_cycle_cus(vCus,vLoan_date,vAmount,vRate,vCycle,vCus_debit):
		try:
# 			lscd = CusDebit.objects(cus_id = vCus.id,status=1).order_by('loan_date')
# 			for cd in lscd:
# 				analyze_debit_detail(vCus,vCus_debit,cd.loan_date,vAmount,vRate,cd.cycle)
			analyze_debit_detail(vCus,vCus_debit,vCus_debit.loan_date,vAmount,vRate,vCus_debit.cycle)
		except Exception as ex:
			print(ex)
def analyze_debit_detail(vCus,vCus_debit,vLoan_date,vEnd_cycle,vRate,vCycle):
		try:
			vToday = datetime.strptime(str(date.today()),'%Y-%m-%d')
# 			lsCdt = CusDebitDetail.objects(cus_debit_id = vCus_debit.id).order_by('from_date')
			
			vdiff=(float(str(((vToday -vLoan_date).days)))+1)/vCycle
			print(int(vdiff))
# 			vLoan_months = (vToday.month - vLoan_date.month)
			if vdiff > 0 :
				#Thieu ban ghi chi tiet
				insert_missing_debit_detail(vCus,vCus_debit,vLoan_date,vEnd_cycle,vRate)
		except Exception as ex:
			print(ex)
def make_payment(vCus_id,vAmount,vPay_date):
		try:
			vtoday = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
			#vuser = User.objects.get(id=vCus_id)
			vCustomer = Customer.objects(cus_id = vCus_id)
			lscd = CusDebit.objects(cus_id = vCus_id,status=1).order_by('loan_date')
			#Insert data in to Payment
			#-------------------------------------------------------------------------
			pt = Payment.objects()
			
			pt.cus_id  = vCustomer
			pt.create_date= vtoday
			pt.pay_date= vPay_date
			pt.amount = vAmount
			pt.status = 1
			#-------------------------------------------------------------------------
			for cd in lscd:
				analyze_payment(vCus_id,cd.id,vAmount,pt.id)
				
		except Exception as ex:
			print(ex)
def analyze_payment(vCus_id,vcus_debit_id,vAmount,vPayment_id):
	try:
		vToday = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
		vRemainAmount = vAmount
		lscdt = CusDebitDetail.objects(cus_debit_id = vcus_debit_id,status=1).order_by('loan_date')
		pdt = PaymentDetail.objects()
		
		for cd in lscdt:
			payment_amount = 0.00
			current_debit = cd.end_cycle
			if vRemainAmount > 0:
				if cd.end_cycle >= vAmount:
					payment_amount = vAmount
					cd.payment = payment_amount
					remain_debit = cd.end_cycle - payment_amount
					cd.end_cycle = remain_debit
					vRemainAmount = 0.00
				else:
					payment_amount = cd.end_cycle
					cd.payment = payment_amount
					remain_debit = cd.end_cycle - payment_amount
					cd.end_cycle = remain_debit
					vRemainAmount = vAmount - payment_amount
				#Insert into payment detail
				
				pdt.payment_id = vPayment_id
				pdt.cus_debit_id = vcus_debit_id
				pdt.cus_id  = vCus_id
				pdt.create_date= vToday
				pdt.debit = current_debit
				pdt.payment = payment_amount
				pdt.remain = pdt.debit - pdt.payment 
				pdt.status = 1
				pdt.save()
		#End for
		if vRemainAmount > 0:
			analyze_payment(vCus_id,vcus_debit_id,vRemainAmount,vPayment_id)
	except Exception as ex:
		print(ex)
def insert_missing_debit_detail(vCus,vCus_debit,vFrom_date,vStart_cycle,vRate):
	try:
		vToday = datetime.strptime(str(date.today()),'%Y-%m-%d')
		vTodate = vFrom_date + relativedelta(days=+vCus_debit.cycle)
		vTodate =vTodate + relativedelta(days=-1)
		vStart_cycle_temp=vStart_cycle
		
		vdiff=((vToday -vFrom_date).days)/vCus_debit.cycle
		vdiff_round=int(vdiff)
		index = 1
		print(vdiff_round)
		
		
		while vdiff_round > 0:
			print(str(vdiff_round))
			cdt = CusDebitDetail()
			cdt.cus_id  = vCus
			cdt.cus_debit_id  = vCus_debit
			cdt.from_date= vFrom_date
			cdt.rate = vRate
			cdt.start_cycle = vStart_cycle_temp
			
			cdt.amount = (vStart_cycle_temp*vCus_debit.cycle*cdt.rate)/1000000
			cdt.to_date= vTodate
			
			cdt.payment = 0
			cdt.end_cycle = cdt.start_cycle + cdt.amount - cdt.payment
			cdt.debit = 0
			cdt.status = 1
			cdt.days = float(str((cdt.to_date -cdt.from_date).days))+1
			cdt.index =index
			#---------------------------------------------------------------------
			# Assign for next cycle
			vFrom_date = cdt.to_date + relativedelta(days=+1)
			vTodate = vFrom_date + relativedelta(days=+vCus_debit.cycle)
			vTodate =vTodate + relativedelta(days=-1)
			vStart_cycle_temp = cdt.end_cycle
			index += 1
			vdiff_round -= 1
			#---------------------------------------------------------------------
			cdt.save()
		if (((vToday -vFrom_date).days)%vCus_debit.cycle) >= 0 :
			cdt = CusDebitDetail()
			cdt.cus_id  = vCus
			cdt.cus_debit_id = vCus_debit
			cdt.from_date= vFrom_date
			cdt.rate = vRate
			cdt.start_cycle = vStart_cycle_temp
			cdt.amount = (vStart_cycle_temp*(((vToday -vFrom_date).days)%vCus_debit.cycle +1)*cdt.rate)/1000000
			cdt.to_date = vToday
			cdt.payment = 0
			cdt.end_cycle = cdt.start_cycle + cdt.amount - cdt.payment
			cdt.debit = 0
			cdt.status = 1
			cdt.days = float(str((cdt.to_date -cdt.from_date).days))+1
			cdt.flag = 1
			cdt.index= index
			#---------------------------------------------------------------------
			# Assign for next cycle
			vFrom_date = cdt.to_date
			vTodate = vFrom_date + relativedelta(months=+1)
			vStart_cycle_temp = cdt.end_cycle
			#---------------------------------------------------------------------
			cdt.save()
			#total debit and last_close_date
			vCus_debit.total_debit = cdt.end_cycle
			vCus_debit.total_debit_trailer = cdt.end_cycle
			vCus_debit.last_close_date = cdt.to_date
			vCus_debit.save()
			
	except Exception as ex:
		print(ex)
def insert_missing_debit_detail_trailer(vCus,vCus_debit,vFrom_date,today,vStart_cycle,vRate):
	try:
		vToday = today
		vTodate = vFrom_date + relativedelta(days=+vCus_debit.cycle)
		vTodate =vTodate + relativedelta(days=-1)
		vStart_cycle_temp=vStart_cycle
		
		vdiff=((vToday -vFrom_date).days)/vCus_debit.cycle
		vdiff_round=int(vdiff)
		index = 1
		print(vdiff_round)
		
		
		while vdiff_round > 0:
			print(str(vdiff_round))
			cdtt = CusDebitDetailTrailer()
			cdtt.cus_id  = vCus
			cdtt.cus_debit_id  = vCus_debit
			cdtt.from_date= vFrom_date
			cdtt.rate = vRate
			cdtt.start_cycle = vStart_cycle_temp
			
			cdtt.amount = (vStart_cycle_temp*vCus_debit.cycle*cdtt.rate)/1000000
			cdtt.to_date= vTodate
			
			cdtt.payment = 0
			cdtt.end_cycle = cdtt.start_cycle + cdtt.amount - cdtt.payment
			cdtt.debit = 0
			cdtt.status = 1
			cdtt.days = float(str((cdtt.to_date -cdtt.from_date).days))+1
			cdtt.index =index
			#---------------------------------------------------------------------
			# Assign for next cycle
			vFrom_date = cdtt.to_date + relativedelta(days=+1)
			vTodate = vFrom_date + relativedelta(days=+vCus_debit.cycle)
			vTodate =vTodate + relativedelta(days=-1)
			vStart_cycle_temp = cdtt.end_cycle
			index += 1
			vdiff_round -= 1
			#---------------------------------------------------------------------
			cdtt.save()
		if (((vToday -vFrom_date).days)%vCus_debit.cycle) >= 0 :
			cdtt = CusDebitDetailTrailer()
			cdtt.cus_id  = vCus
			cdtt.cus_debit_id = vCus_debit
			cdtt.from_date= vFrom_date
			cdtt.rate = vRate
			cdtt.start_cycle = vStart_cycle_temp
			cdtt.amount = (vStart_cycle_temp*(((vToday -vFrom_date).days)%vCus_debit.cycle +1)*cdtt.rate)/1000000
			cdtt.to_date = vToday
			cdtt.payment = 0
			cdtt.end_cycle = cdtt.start_cycle + cdtt.amount - cdtt.payment
			cdtt.debit = 0
			cdtt.status = 1
			cdtt.days = float(str((cdtt.to_date -cdtt.from_date).days))+1
			cdtt.flag = 1
			cdtt.index= index
			#---------------------------------------------------------------------
			# Assign for next cycle
			vFrom_date = cdtt.to_date
			vTodate = vFrom_date + relativedelta(months=+1)
			vStart_cycle_temp = cdtt.end_cycle
			#---------------------------------------------------------------------
			cdtt.save()
# 			total debit and last_close_date
			vCus_debit.total_debit_trailer = cdtt.end_cycle
			vCus_debit.save()
			
	except Exception as ex:
		print(ex)
def insert_missing_debit_detail_test(vCus, vCd, vCus_debit_detail):
	try:
# 		update last cus_debit_detail ????
# 		vToday = datetime.strptime(str(date.today()),'%Y-%m-%d')
# 		vdiff= vToday - vCd.last_close_date
# # 		vMissingDay = vCd.cycle - vCus_debit_detail.days
# 		if vdiff/vCd.cycle <1:
# 			print("update last cus_debit_detail")
# 			vCus_debit_detail.amount = abc
# 		else:
# 			print('update,insert')
		vFrom_date = vCus_debit_detail.from_date
		index = vCus_debit_detail.index
		vStart_cycle = vCus_debit_detail.start_cycle
		vRate = vCus_debit_detail.rate
		
		insert_missing_debit_detail_test1(vCus,vCd,vFrom_date,vStart_cycle,vRate,index,vCus_debit_detail)
	except Exception as ex:
		print(ex)
def insert_missing_debit_detail_test1(vCus,vCus_debit,vFrom_date,vStart_cycle,vRate,index,vCus_debit_detail):
	try:
		vToday = datetime.strptime(str(date.today()),'%Y-%m-%d')
		vTodate = vFrom_date + relativedelta(days=+vCus_debit.cycle)
		vTodate =vTodate + relativedelta(days=-1)
		vStart_cycle_temp=vStart_cycle
		
		vdiff=((vToday -vFrom_date).days)/vCus_debit.cycle
		vdiff_round=int(vdiff)
		index = index
		print(vdiff_round)
		
		
		while vdiff_round > 0:
			print(str(vdiff_round))
			cdt = CusDebitDetail()
			cdt.cus_id  = vCus
			cdt.cus_debit_id  = vCus_debit
			cdt.from_date= vFrom_date
			cdt.rate = vRate
			cdt.start_cycle = vStart_cycle_temp
			
			cdt.amount = (vStart_cycle_temp*vCus_debit.cycle*cdt.rate)/1000000
			cdt.to_date= vTodate
			
			cdt.payment = 0
			cdt.end_cycle = cdt.start_cycle + cdt.amount - cdt.payment
			cdt.debit = 0
			cdt.status = 1
			cdt.days = float(str((cdt.to_date -cdt.from_date).days))+1
			cdt.index =index
			#---------------------------------------------------------------------
			# Assign for next cycle
			vFrom_date = cdt.to_date + relativedelta(days=+1)
			vTodate = vFrom_date + relativedelta(days=+vCus_debit.cycle)
			vTodate =vTodate + relativedelta(days=-1)
			vStart_cycle_temp = cdt.end_cycle
			index += 1
			vdiff_round -= 1
			#---------------------------------------------------------------------
			cdt.save()
		if (((vToday -vFrom_date).days)%vCus_debit.cycle) >= 0 :
			cdt = CusDebitDetail()
			cdt.cus_id  = vCus
			cdt.cus_debit_id = vCus_debit
			cdt.from_date= vFrom_date
			cdt.rate = vRate
			cdt.start_cycle = vStart_cycle_temp
			cdt.amount = (vStart_cycle_temp*(((vToday -vFrom_date).days)%vCus_debit.cycle +1)*cdt.rate)/1000000
			cdt.to_date = vToday
			cdt.payment = 0
			cdt.end_cycle = cdt.start_cycle + cdt.amount - cdt.payment
			cdt.debit = 0
			cdt.status = 1
			cdt.days = float(str((cdt.to_date -cdt.from_date).days))+1
			cdt.flag = 1
			cdt.index= index
			#---------------------------------------------------------------------
			# Assign for next cycle
			vFrom_date = cdt.to_date
			vTodate = vFrom_date + relativedelta(months=+1)
			vStart_cycle_temp = cdt.end_cycle
			#---------------------------------------------------------------------
			cdt.save()
			#total debit and last_close_date
			vCus_debit.total_debit = cdt.end_cycle
			vCus_debit.total_debit_trailer = cdt.end_cycle
			vCus_debit.last_close_date = cdt.to_date
			vCus_debit.save()
			vCus_debit_detail.delete()
	except Exception as ex:
		print(ex)