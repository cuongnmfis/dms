'''
Created on Apr 3, 2014

@author: TuanNA
'''
from django.core.context_processors import csrf
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from mongoengine.django.auth import User

from myapp.models.CommentPost import CommentPost
from myapp.models.MentorPost import MentorPost
from myapp.util import context_processors


# @login_required(login_url='/signin')
def index(request):
	if (request.user.is_authenticated()==False) or(request.user is None):
		return render(request, 'myapp/home1.html', {})
	elif request.method == 'GET':
# 		posts = MentorPost.objects
# 		user_type = ""
# 		try:
# 			user_type = request.session['user_type']
# 			is_mentor = request.session['is_mentor']
# 			if is_mentor:
# 				return HttpResponseRedirect('/mentor-course?user_id='+str(request.user.id))	
# 			else:
# 				return HttpResponseRedirect('/search-mentor')
# 		except Exception:
# 			user_type = ""
		try:
			is_mentor = request.session['is_mentor']
		except Exception as e:
			is_mentor = False	
		if is_mentor:
			return HttpResponseRedirect('/mentor-course?user_id='+str(request.user.id))	
		else:
			return HttpResponseRedirect('/student-home')	
# 		context = {'posts':posts,'user_type':user_type,'user_id':request.user,}
# 		return render(request,'myapp/index.html', context)
# 		return HttpResponseRedirect('/personalhome')
#		return render(request, 'myapp/home.html', {})
	elif request.method == 'POST':
		comment = request.POST['txtComment']
		post_id = request.POST['hd_post_id']
		user_id = request.session['_auth_user_id']
		cmt = CommentPost()
		cmt.content=comment
		cmt.user_id=User.objects.get(id=user_id)
		cmt.post_id=MentorPost.objects.get(id=post_id)
		cmt.save()# 		user_id = request.session
		post = MentorPost.objects.get(id=post_id)
		post.comments.append(cmt);
		post.save()
		user_type = ""
		try:
			user_type = request.session['user_type']
		except Exception:
			user_type = ""
		context = {'post':post,'user_type':user_type,'user_id':request.user,}
		context.update(csrf(request))
		context.update(context_processors.user(request))
		return render_to_response("myapp/index.html", context)