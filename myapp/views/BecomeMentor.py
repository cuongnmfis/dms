'''
Created on Apr 3, 2014

@author: ducdienpt
'''
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from myapp.models import Mentor


@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		return render(request, 'myapp/become-mentor.html', {})
	elif request.method == 'POST':
		#check user exist mentor ?
		lsmentor = Mentor.objects(user=request.user.id)
		if len(lsmentor) >0:
			request.session['is_mentor'] = True
		else:
			mentor = Mentor()
			mentor.user = request.user
			mentor.save()
			request.session['is_mentor'] = True
		return HttpResponseRedirect('/mentor-course?user_id='+str(request.user.id))
# 	return render(request, 'myapp/become-mentor.html', c)