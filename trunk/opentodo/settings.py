# -*- coding: utf-8 -*-

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'mysql'        # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_NAME = 'opentodo'       # Or path to database file if using sqlite3.
DATABASE_USER = ''               # Not used with sqlite3.
DATABASE_PASSWORD = ''           # Not used with sqlite3.
DATABASE_HOST = ''               # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''               # Set to empty string for default. Not used with sqlite3.

# BASE_URL = http://myhost.com/opentodo/
BASE_URL = ''

# Absolute path to the directory that holds media.
# MEDIA_ROOT = '/var/www/opentodo_media'
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT.
# Note that this should have a trailing slash if it has a path component
# MEDIA_URL = 'http://static.myhost.ru' or MEDIA_URL = 'http://myhost.ru/static/'
MEDIA_URL = ''

EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ih^s_r3qgx!8-7aj%7^tqg#mj&zpdmchbbc=+*9=y#cm&v(ga)'


#############################################################################
# You should not edit these settings
#############################################################################

ADMIN_MEDIA_PREFIX = '/admin_media/'

LOGIN_URL = '/opentodo/accounts/login/'
LOGIN_REDIRECT_URL= '/opentodo/'

import sys, os
PROJECT_DIR = os.path.dirname(__file__)
sys.path.append(PROJECT_DIR)
sys.path.append(PROJECT_DIR + '/apps')

TEMPLATE_DIRS = (
    PROJECT_DIR + '/templates'
)

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru'

SITE_ID = 1
USE_I18N = True

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'todo.middleware.StripWhitespaceMiddleware',
)
FILE_CHARSET = 'utf-8'

SESSION_SAVE_EVERY_REQUEST = False

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'context_processors.site_media_url'
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'todo',
)