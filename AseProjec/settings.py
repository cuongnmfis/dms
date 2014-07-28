# Django settings for AseProjec project.

import os

import mongoengine


# mongoengine.register_connection(alias, name, host, port, is_slave, read_preference, slaves, username, password)
mongoengine.connect('my_db',host="oceanic.mongohq.com",port=10043,username="admin",password="113322")
AUTHENTICATION_BACKENDS = (
    'mongoengine.django.auth.MongoEngineBackend',
    'social.backends.open_id.OpenIdAuth',
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOAuth',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.facebook.FacebookOAuth2',
)


SESSION_ENGINE = 'mongoengine.django.sessions'
DEBUG = True
TEMPLATE_DEBUG = DEBUG
TEMPLATE_DIRS = (
#                  os.path.join(os.path.dirname(__file__),'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)
#CSRF_COOKIE_SECURE = True
TEMPLATE_CONTEXT_PROCESSORS =(
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.csrf',
    'myapp.util.context_processors.user',
)

LOCALE_PATHS = ('/conf/locale/',)

ADMINS = (
    # ('CuongNM', 'cuongnm@ex-artisan.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy',
    },
}
SESSION_ENGINE = 'mongoengine.django.sessions'
AUTHENTICATION_BACKENDS = (
    'mongoengine.django.auth.MongoEngineBackend',
    'social.backends.open_id.OpenIdAuth',
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOAuth',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.facebook.FacebookOAuth2',
)
TEST_RUNNER = 'yourproject.tests.NoSQLTestRunner'
# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
# LANGUAGE_CODE = 'us'
LANGUAGE_CODE = 'en_US.utf8'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir))+"/upload/"

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/upload/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/'
#STATIC_IMAGE_URL = '/common/images'
# Additional locations of static files
STATICFILES_DIRS = (
                'D:/Projects/ASE/AseProjec/common',
                #("css", "D:/Projects/ASE/AseProjec/common/css"),
                #("fonts", "D:/Projects/ASE/AseProjec/common/fonts"),
                #("holder.js", "D:/Projects/ASE/AseProjec/common/holder.js"),
                #("images", "D:/Projects/ASE/AseProjec/common/images"),
                #("js", "D:/Projects/ASE/AseProjec/common/js"),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '3=2nhmoxo#ze5+bk6-m887_o6r$ytqd-eja90r%879!^oj+k0n'


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

AUTO_LOGOUT_DELAY = 5

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'myapp.views.middleware.AutoLogout',
    'myapp.views.middleware.ExceptionMiddleware',
    
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'AseProjec.urls'


# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'AseProjec.wsgi.application'



INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'mongoengine.django.mongo_auth',
    #'django.contrib.staticfiles',
    'myapp',
    'social.apps.django_app.me',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

LANGUAGES = (
    ('en', 'English'),
    ('en-us', 'English'),
    ('ja', 'Japan'),
)

AUTH_USER_MODEL = 'mongo_auth.MongoUser'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/signinsns'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/signupsns'

SOCIAL_AUTH_STORAGE = 'social.apps.django_app.me.models.DjangoStorage'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '86706008722-gtsfej37d74nhhvjlkblfllbj3j5qmiv.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'hUzpunyIJmBC2e_Xi7Vx2mzP'

SOCIAL_AUTH_TWITTER_KEY = 'EE3yel9URqDYyZl18eHscAYyO'
SOCIAL_AUTH_TWITTER_SECRET = 'kvvwhIYvrOpEmaqNN8Eh0gRn3LG6dprP93rCEaCq7ZcrSnwrXI'

SOCIAL_AUTH_FACEBOOK_KEY = '295316650624581'
SOCIAL_AUTH_FACEBOOK_SECRET = 'f814a4e83209881e9cc4ab81775963e4'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)

SOCIAL_AUTH_PIPELINE += (
    'myapp.util.pipelines.save_profile_picture',
)
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
