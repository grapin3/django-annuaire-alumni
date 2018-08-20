"""
Django settings for annuaire_alumni project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(BASE_DIR,'..')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o)oym9sa6wr(-(&x)_e0)r-z8f=#sy5y778p^n6l1ecc!a^7i)'

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
    'apps.annuaire',
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

ROOT_URLCONF = 'annuaire_alumni.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
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

WSGI_APPLICATION = 'annuaire_alumni.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# Define for used in local
INTERNAL_IPS = []

# Mess
LOGIN_REDIRECT_URL = 'display_profile'
LOGOUT_REDIRECT_URL = 'home'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

#Define the css class name to append depending on the type of messages
MESSAGE_TAGS = { messages.ERROR: 'danger', messages.DEBUG: 'secondary',}

#Logging setup
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    #Define two outputs format, a verbose one and a short one
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {asctime}:{message}',
            'style': '{',
        },
    },
    'filters': {
        # How to define a custom filter
        #  'special': {
            #  '()': 'annuaire_alumni.logging.SpecialFilter',
            #  'foo': 'bar',
        #  },
        # A filter that only passes if DEBUG == True. It won't work in
        # production environnement
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
            },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
            },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            #  'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
            },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false']
            }
        },
    'loggers': {
        # We don't setup the logging for the django logger as the default seems
        # to be just fine
        #  'django': {
            #  'handlers': ['console'],
            #  'propagate': True,
        #  },
        #  'django.request': {
            #  'handlers': ['mail_admins'],
            #  'level': 'ERROR',
            #  'propagate': False,
        #  },
        'apps.annuaire': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
            #  'filters': ['special']
        }
    }
}

