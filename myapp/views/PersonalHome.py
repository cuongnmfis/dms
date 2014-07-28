'''
Created on Apr 3, 2014
@author: TuanNA
'''
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from mongoengine.django.auth import User

from myapp.models.CommentPost import CommentPost
from myapp.models.Esay import Esay
from myapp.models.MentorPost import MentorPost
from myapp.util import context_processors
from myapp.models import RatingPost


@login_required(login_url='/signin')
def index(request):
	if request.method == 'GET':
		posts = MentorPost.objects
		user_type = ""
		try:
			user_type = request.session['user_type']
		except Exception:
			user_type = ""
			
		context = {'posts':posts,'user_type':user_type,'user_id':request.user,}
		return render(request,'myapp/personalhome.html', context)
	elif request.method == 'POST':
		posttype = request.POST['posttype']
		#post type = 2 mean lecture;
		if posttype == '2':
			#user_id = request.session['_auth_user_id']
			print("creating post...")
			Title = request.POST['txtTitle']
			Content = request.POST['txtContent']
			#FromDate = request.POST['dtpfromdate']
			#ToDate = request.POST['dtptodate']
			Amazonlink = request.POST['txtAmazonLink']
			#Cost = request.POST['txtCost']
			user_id = User.objects.get(id=request.session['_auth_user_id'])
			print(user_id)
			mp = MentorPost()
			mp.title = Title
			# 			mp.videolink = Videolink
			# 			mp.imagelink = Imagelink
			# 			mp.amazonlink = Amazonlink
			mp.content = Content
			mp.user_id = user_id
			mp.post_type = "2"
			mp.status = "1"
			#mp.from_date = FromDate
			#mp.to_date = ToDate
			mp.amazonlink = Amazonlink
			mp.save()
			#post created
			posts = MentorPost.objects
			user_type = ""
			try:
				user_type = request.session['user_type']
			except Exception:
				user_type = ""
				
			context = {'posts':posts,'user_type':user_type,'user_id':request.user,}
			return HttpResponseRedirect('/personalhome')
		elif posttype == '1':
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
			return HttpResponseRedirect('/personalhome')
		elif posttype == '3':
			title = request.POST['txtTitle']
			content = request.POST['txtContent']
			post_id = request.POST['post_id']
			user_id = request.session['_auth_user_id']
# 			cmt = CommentPost()
# 			cmt.content=comment
# 			cmt.user_id=User.objects.get(id=user_id)
# 			cmt.post_id=MentorPost.objects.get(id=post_id)
# 			cmt.save()
			esay = Esay()
			esay.title = title
			esay.content = content
			esay.save()
			post = MentorPost.objects.get(id=post_id)
			post.esay.append(esay);
			post.save()
			posts = MentorPost.objects
			user_type = ""
			try:
				user_type = request.session['user_type']
			except Exception:
				user_type = ""
			context = {'post':post,'user_type':user_type,'user_id':request.user,}
			context.update(csrf(request))
			context.update(context_processors.user(request))
		elif posttype == '4':
			comment = request.POST['txaComment']
			post_id = request.POST['post_id']
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
			return HttpResponseRedirect('/personalhome')
		elif posttype == '5':
			rate = request.POST['txtrate']
			post_id = request.POST['post_id']
			user_id = request.session['_auth_user_id']

			rate = RatingPost()
			rate.starnumber=rate
			rate.user_id=User.objects.get(id=user_id)
			rate.post_id=MentorPost.objects.get(id=post_id)
			rate.save()# 		user_id = request.session
			post = MentorPost.objects.get(id=post_id)
			post.rating.append(rate);
			post.save()
			user_type = ""
			try:
				user_type = request.session['user_type']
			except Exception:
				user_type = ""
			context = {'post':post,'user_type':user_type,'user_id':request.user,}
			context.update(csrf(request))
			context.update(context_processors.user(request))
			return HttpResponseRedirect('/personalhome')
		return HttpResponseRedirect('/personalhome')