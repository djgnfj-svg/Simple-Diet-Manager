"""
Django settings for Simple_Diet_Manager project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import json
import os
from pathlib import Path

import pymysql
from django.core.exceptions import ImproperlyConfigured

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_BASE_FILE = os.path.join(BASE_DIR, '.secrets.json')

with open(SECRET_BASE_FILE, encoding="UTF-8") as f:
    secrets = json.loads(f.read())
def get_secret(setting):
    """비밀 변수를 가져오거나 명시적 예외를 반환한다."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)
# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = get_secret("SECRET_KEY")

if get_secret("ENV") == "DEV":
    DEV = True
    
else :
    DEV = False

if DEV:
    ALLOWED_HOSTS = ["*"]
    DEBUG = True
    DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: DEBUG,
    }
else:
    DEBUG = False
    ALLOWED_HOSTS = ["simple-diet-manager.link"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar', # debug tool bar

    # library
	'rest_framework',
	'corsheaders',

    'foods',
    'meals',
    'diets',
    'accounts',
    
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'Simple_Diet_Manager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'Simple_Diet_Manager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if get_secret("ENV") == "DEV":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else :
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', # engine: mysql
            'NAME' : get_secret("DB_NAME"), # DB Nameget_secret("ENV")
            'USER' : get_secret("DB_USER"), # DB User
            'PASSWORD' : get_secret("DB_PASSWORD"), # Password
            'HOST': get_secret("DB_HOST"), # 생성한 데이터베이스 엔드포인트
            'PORT': get_secret("DB_PORT"), # 데이터베이스 포트
            'OPTIONS':{
                'init_command' : "SET sql_mode='STRICT_TRANS_TABLES'"
            }
        }
    }
    

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static') #개발자가 관리하는 파일들 

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') #사용자가 업로드한 파일 관리

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# throttle
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS' : 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,

    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '500/day',
        'user': '500/day'
    },
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}


#CORS setting
if DEV:
    CORS_ORIGIN_WHITELIST = [
        'http://localhost:3000',
        'http://127.0.0.1:8000',
    ]
    CORS_ALLOW_CREDENTIALS = True
else :
    CORS_ORIGIN_WHITELIST = [
        'http://simple-diet-manager.link',
        'http://simple-diet-manager.link:8000',
    ]

