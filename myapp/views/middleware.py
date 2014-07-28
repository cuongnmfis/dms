from datetime import datetime, timedelta

from django.conf import settings
from django.contrib import auth
from django.http import HttpResponseRedirect
from social import exceptions as social_exceptions
from django.shortcuts import render
from social.apps.django_app.middleware import SocialAuthExceptionMiddleware


class ExceptionMiddleware(object):
    def process_exception(self, request, exception):
        if exception:
            ex = exception
            context={"ex":ex}
            return render(request,'myapp/error-page.html', context)

        
class SocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def process_exception(self, request, exception):
        if hasattr(social_exceptions, 'AuthFailed'):
            print(social_exceptions)
            return HttpResponseRedirect('/error-authenticate')
        else:
            raise exception
class AutoLogout:
    def process_request(self, request):
        if not request.user.is_authenticated() :
            #Can't log out if not logged in
            return
        if 'last_touch' not in request.session:
            request.session['last_touch'] = datetime.now()
            
        try:
            if datetime.now() - request.session['last_touch'] > timedelta( 0, settings.AUTO_LOGOUT_DELAY * 60, 0):
                auth.logout(request)
                del request.session['last_touch']
                return
        except KeyError:
            pass
        
        request.session['last_touch'] = datetime.now()