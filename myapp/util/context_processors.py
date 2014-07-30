from mongoengine.django.auth import User



def user(request):
	"""A context processor that adds the user to template context"""
	profile = {}
	if (request.user.is_authenticated()==True) and(request.user is not None):
		try:
			user_images = request.session['user_images']
		except Exception as e:
			user_images = ""
	if (request.user.is_authenticated()==True) and(request.user is not None):
		loggedUser = User.objects(username=str(request.user))
		return {
			'user': request.user,
			'profile':profile,
			'loggedUser':loggedUser[0],
			'user_images':user_images
		}
	else:
		return {
		'user': request.user,
		'profile':profile,
		'loggedUser':[],
		'user_images':""
	}