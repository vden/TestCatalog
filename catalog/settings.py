# Django settings for Catalog project.

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Denis Voskvitsov', 'denis.voskvitsov@gmail.com'),
)

import os
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

MANAGERS = ADMINS

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-ru'

SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_ROOT = os.path.join(PROJECT_ROOT, '../media/')
MEDIA_URL = '/media/'

# static files on production will be here
STATIC_ROOT = os.path.join(PROJECT_ROOT, '../static/')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    # for development
    os.path.join(PROJECT_ROOT, 'static/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'i2h59kwas1c2ss7zhx8)mx+k4lkuecmbzkkg-$bvq@ne(oq@vh'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    "django.contrib.auth.context_processors.auth",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'catalog.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',

    # 3rd party
    "south",

    # local apps
    'core',
)

FIXTURE_DIRS = (
    os.path.join(PROJECT_ROOT, 'fixtures'),
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# Import deploy-specific settings, if present
try:
    from local_settings import *
except ImportError, e:
    pass
