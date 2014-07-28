'''
Created on Apr 3, 2014
@author: TuanNA
'''
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		error_message = request.GET['error_message']
		
		context = {'error_message':error_message}
		return render(request,'myapp/error-page.html', context)
	