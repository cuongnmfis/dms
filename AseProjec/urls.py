import os

from django.conf import settings
from django.conf.urls import patterns, url , include

from myapp.views import Home, AccountSetting, PostDetail, SignIn, MentorPost, \
	Profile, SignUp, SignOut, PeopleDirectory, Chat, PersonalHome , AuthenFail, \
	MentorView, Documents, StudentHome, MentorCourse, Test, SearchMentor, BecomeMentor, \
	StudentView, CourseDetail, AsStudentHome , StudyLog, CreateCurriculumn,EditMaterial ,\
	Community,Slide,EditAction,EditCurriculumn, errorpage, CreateDms,d_MainScreen,d_NewCus,d_CusDebitDetail


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
						url(r'^community$', Community.index, name='community'),
						url(r'^i18n/', include('django.conf.urls.i18n')),
						url(r'^signinsns$', SignIn.signinsns, name='signinsns'),
						url(r'^error-authenticate$', AuthenFail.index),
						url('', include('social.apps.django_app.urls', namespace='social')),
                       url(r'^$', Home.index),
                       url(r'^home$', Home.index),
                       url(r'^index$', Home.index),
                       url(r'^account-setting$', AccountSetting.index),
                        url(r'^blog-single$', PostDetail.index, name='blog-single'),
                        url(r'^mentorpost$', MentorPost.index),
						url(r'^mentorview$', MentorView.afterlogin,name='mentorview'),
						url(r'^studentview$', StudentView.index,name='studentview'),
						url(r'^studylog$', StudyLog.index,name='studylog'),
						url(r'^AsStudentHome$', AsStudentHome.index,name='studenthome'),
						url(r'^personalhome$', PersonalHome.index,name='personalhome'),
                        url(r'^mentorpost$', MentorPost.index),
                       url(r'^signin$', SignIn.index, name='signin'),
                       url(r'^profile$', Profile.index, name='profile'),
                       url(r'^signup$', SignUp.index, name='signup'),
                       url(r'^signupsns$', SignUp.signupsns, name='signupsns'),
                       url(r'^signout$', SignOut.index, name='signout'),
                       url(r'^create-profile$', Profile.createProfile),
                       url(r'^update-profile$', Profile.updateProfile),
                       url(r'^people-directory$',PeopleDirectory.index),
                       url(r'^chat$',Chat.index),
                       url(r'^post-detail$', PostDetail.index, name='post-detail'),
                       url(r'^lecture-detail$', PostDetail.index, name='lecture-detail'),
                       url(r'^course-detail$', CourseDetail.index, name='course-detail'),
                       url(r'^documents$', Documents.index),
                       url(r'^test$', Test.index),
                       url(r'^student-home$', StudentHome.index, name='student-home'),
#                        url(r'^add-course$', MentorCourse.index, name='add-course'),
                       url(r'^add-material$', MentorCourse.add_material, name='add-material'),
                       url(r'^add-action$', MentorCourse.add_action, name='add-action'),
                       url(r'^join-course$', CourseDetail.index, name='join-course'),
                       url(r'^search-mentor$', SearchMentor.index),
                       url(r'^become-mentor$', BecomeMentor.index),
                       url(r'^mentor-course$', MentorView.index,name='mentor-course'),
                       url(r'^mentor-view$', MentorView.afterlogin,name='mentor-view'),
                       url(r'^add-course$', CreateCurriculumn.index,name='add-course'),
                       url(r'^edit-material$', EditMaterial.index, name='edit-material'),
                       url(r'^edit-action$', EditAction.index, name='edit-action'),
                       url(r'^edit-curriculumn$', EditCurriculumn.index, name='edit-curriculumn'),
                       url(r'^CreateDms$', CreateDms.index, name='CreateDms'),
                       url(r'^slide$',Slide.index),
                       url(r'^error-page$',errorpage.index,name='error-page'),
                       url(regex  = r'^%s(?P<path>.*)$' % settings.STATIC_URL[1:], 
    view   = 'django.views.static.serve', 
    kwargs = {'document_root': os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir))+"/common",
              'show_indexes' : True})
    # Examples:
    # url(r'^$', 'AseProjec.views.home', name='home'),
    # url(r'^AseProjec/', include('AseProjec.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
