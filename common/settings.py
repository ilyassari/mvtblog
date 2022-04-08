"""
Django settings for mvtblog project.
"""

import os
import environ
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # project apps
    'account.apps.AccountConfig',
    'blog.apps.BlogConfig',
    'link.apps.LinkConfig',
    # ThirdPartyApps
    'ckeditor',
    'ckeditor_uploader',
    'crispy_forms',
    "crispy_bootstrap5",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'common.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'account.forms.injection',
            ],
        },
    },
]

WSGI_APPLICATION = 'common.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation

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

LANGUAGE_CODE = 'tr'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#####

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
    ]

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_ROOT = 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


CKEDITOR_UPLOAD_PATH = os.path.join(MEDIA_ROOT, 'ckeditor')


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


AUTH_USER_MODEL = 'account.CustomUserModel'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env('EMAIL_ADDRESS')
EMAIL_HOST_PASSWORD = env('EMAIL_PASSWORD')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'basic_log':{
            'format': '{asctime} | {levelname} | {name} | {message}',
            'style': '{'
        }
    },
    'handlers':{
        'console': {
            'class': 'logging.StreamHandler'
        },
        'file':{
            'class': 'logging.FileHandler',
            'filename': 'logs/log.log',
            'formatter': 'basic_log'
        }
    },
    'loggers': {
        'post_viewed': {
            'handlers': ['console', 'file'],
            'level': 'INFO'
        },
        'post_added': {
            'handlers': ['file'],
            'level': 'INFO'
        },
        'post_updated': {
            'handlers': ['file'],
            'level': 'INFO'
        },
        'post_deleted': {
            'handlers': ['file'],
            'level': 'INFO'
        },
        'comment_added': {
            'handlers': ['file'],
            'level': 'INFO'
        },
        'comment_deleted': {
            'handlers': ['file'],
            'level': 'INFO'
        }
    }
}
