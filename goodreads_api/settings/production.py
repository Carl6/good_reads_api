from .base import *
import dj_database_url
import os


DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = dict()
DATABASES['default'] = dj_database_url.config()

STATIC_ROOT = os.path.join(os.getcwd(),'static')