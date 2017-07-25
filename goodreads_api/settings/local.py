from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'GR-Database',
    'USER': 'GR-Admin',
    'PASSWORD':'libros',
    'HOST':'localhost',
    'PORT':'5432'
  }
}