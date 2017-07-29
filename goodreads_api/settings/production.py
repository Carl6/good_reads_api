from .base import *
import dj_database_url
import os


DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'good_db',
    'USER': 'good_admin',
    'PASSWORD':'good2017',
    'HOST':'localhost',
    'PORT':'5432'
  }
}

# DATABASES = dict()
# DATABASES['default'] = dj_database_url.config()

# STATIC_ROOT = os.path.join(os.getcwd(),'static')