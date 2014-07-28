from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':	
		context = {}
		return render(request,'myapp/community.html', context)