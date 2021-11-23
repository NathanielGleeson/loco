
import environ
import os
import pathlib
from pathlib import Path
import django_on_heroku
import dj_database_url
from decouple import Csv, config
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
env = environ.Env()
environ.Env.read_env()
BASE_DIR = Path(__file__).resolve().parent.parent.parent
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
TEMPLATE_DIR = pathlib.Path.joinpath(BASE_DIR, 'templates')
STATIC_DIR = pathlib.Path.joinpath(BASE_DIR, 'static')
MEDIA_DIR = pathlib.Path.joinpath(BASE_DIR, 'media')
print(BASE_DIR)
print(STATIC_DIR)
#print(STATICFILES_DIRS)
#print(MEDIA_ROOT)
import dj_database_url
from decouple import Config,Csv

MODE=env("MODE", default="dev")
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG', default=False, cast=bool)
# development
if env('MODE')=="dev":
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql_psycopg2',
           'NAME': env('DB_NAME'),
           'USER': env('DB_USER'),
           'PASSWORD': env('DB_PASSWORD'),
           'HOST': env('DB_HOST'),
           'PORT': '',
       }
       
   }
# production
else:
   DATABASES = {
       'default': dj_database_url.config(
           default=config('DATABASE_URL')
       )
   }

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

ALLOWED_HOSTS = env('ALLOWED_HOSTS', cast=Csv())
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'pi30famq-o(&=@zag-5@)f)vp$1)89^hdxb2dzwpboyyoghrgr'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True

#ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'main',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'My_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'My_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

#STATIC_ROOT = [BASE_DIR / 'static_root']
#STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_URL = '/static/'
#STATICFILES_DIRS = [STATIC_DIR,]

#MEDIA_DIR = [MEDIA_DIR,]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
django_on_heroku.settings(locals())

import environ
env = environ.Env()
environ.Env.read_env()

# Previous settings ...
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

# Custom setting. To email
RECIPIENT_ADDRESS = env('RECIPIENT_ADDRESS')