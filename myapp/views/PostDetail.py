'''
Created on Apr 3, 2014

@author: TuanNA
'''
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.shortcuts import render, render_to_response
from mongoengine.django.auth import User

from myapp.models.CommentPost import CommentPost
from myapp.models.MentorPost import MentorPost
from myapp.util import context_processors


@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		vpost_id = request.GET['post_id']
		post = MentorPost.objects.get(id=vpost_id)
# 		comments = CommentPost.objects(post_id=vpost_id).all()
		comments = post.comments
		context = {	'post':post,'comments':comments,
					'user_type':request.session['user_type'],
					'user_id':request.user,
					}
		return render(request, 'myapp/post-detail.html', context)
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
# 		comments = CommentPost.objects(post_id=post_id).all()
		comments = post.comments
		c = {'post':post,'comments':comments,'user_type':request.session['user_type']}
		c.update(csrf(request))
		c.update(context_processors.user(request))
		return render_to_response("myapp/blog-single.html", c)