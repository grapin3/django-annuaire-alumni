from .base import *
from django.conf import settings

DEBUG==True

LOGGING['loggers']['apps.annuaire']['level'] = 'DEBUG'
LOGGING['handlers']['console']['level'] = 'DEBUG'

INSTALLED_APPS += [
        'debug_toolbar',
        'django_extensions',
        ]

MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        ]

INTERNAL_IPS += [
        '127.0.0.1',
        ]

# During development only
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  

MEDIA_URL = 'media/'
