import os

from django.conf import settings
from django.conf.urls import patterns, url , include

from myapp.views import Home, AccountSetting, SignIn, \
	SignUp, SignOut , CreateDms,d_MainScreen,d_NewCus,d_CusDebitDetail,AuthenFail,errorpage\


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('',
						#Debit
						url(r'^mainscreen$', d_MainScreen.index, name='d_MainScreen'),
						url(r'^newcustomer$', d_NewCus.index, name='d_NewCus'),
						url(r'^custom-debit-detail$',d_CusDebitDetail.index),
						url(r'^newCusDebit$',d_CusDebitDetail.index,name='newCusDebit'),
						
						#ASE
						url(r'^error-authenticate$', AuthenFail.index),
						
						url('', include('social.apps.django_app.urls', namespace='social')),
                       url(r'^$', SignIn.index, name='signin'),
                       url(r'^home$', Home.index),
                       url(r'^index$', Home.index),
                       url(r'^account-setting$', AccountSetting.index),
                       
                       url(r'^signin$', SignIn.index, name='signin'),
                       url(r'^signup$', SignUp.index, name='signup'),
                       url(r'^signout$', SignOut.index, name='signout'),
                       
                       url(r'^CreateDms$', CreateDms.index, name='CreateDms'),
                       url(r'^error-page$',errorpage.index,name='error-page'),
                       url(regex  = r'^%s(?P<path>.*)$' % settings.STATIC_URL[1:], 
    view   = 'django.views.static.serve', 
    kwargs = {'document_root': os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir))+"/common",
              'show_indexes' : True})
    # Examples:
    # url(r'^$', 'DMS.views.home', name='home'),
    # url(r'^DMS/', include('DMS.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
