'''
Created on Apr 3, 2014

@author: TuanNA
'''
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from mongoengine.django.auth import User

from myapp.models.MentorPost import MentorPost


@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		print("method is get")
		context = {}
		return render(request, 'myapp/mentor-post.html', context)
	elif request.method == 'POST':
		print("method is get")
		Title = request.POST['txtTitle']
		Imagelink = request.POST['txtImagelink']
		Videolink = request.POST['txtVideolink']
		Amazonlink = request.POST['txtAmazonlink']
		Content = request.POST['txtContent']
		PostType = request.POST['slPostType']
		if PostType != '0':
			FromDate = request.POST['dtpfromdate']
			ToDate = request.POST['dtptodate']
			Place = request.POST['txtPlace']
		user_id = User.objects.get(id=request.session['_auth_user_id'])
		print(user_id)
		mp = MentorPost()
		mp.title = Title
		mp.videolink = Videolink
		mp.imagelink = Imagelink
		mp.amazonlink = Amazonlink
		mp.content = Content
		mp.user_id = user_id
		mp.post_type = PostType
		mp.status = "1"
		if PostType != '0':
			mp.from_date = FromDate
			mp.to_date = ToDate
			mp.place = Place
		mp.save()
		return HttpResponseRedirect('/home')
