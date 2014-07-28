from requests import HTTPError
from myapp.models.UserProfile import UserProfile

def save_profile_picture(strategy, user, response, details,is_new=False,*args,**kwargs):
	
	if strategy.backend.name == 'facebook':
		imgpro = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
	elif strategy.backend.name == 'twitter':
		imgpro = response.get('profile_image_url', '').replace('_normal', '')
	elif strategy.backend.name == 'google-oauth2' and "picture" in response:
		imgpro = response['picture']
	else:
		imgpro = ""
	
	
	try:
		if imgpro:
			try:
				thisprofile = UserProfile.objects(user_id=user)
				#ThaiNN Please review this code
				if len(thisprofile) == 0:
					upro = UserProfile()
					upro.user_id = user
					upro.images = imgpro
					upro.save()
				else:
					mypro = thisprofile[0]
					mypro.images = imgpro
					mypro.save()
			except Exception as e:
					print(e)
	except HTTPError:
		pass