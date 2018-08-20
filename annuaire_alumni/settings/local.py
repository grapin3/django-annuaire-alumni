from .base import *
from django.conf import settings

DEBUG==True

"""
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
"""

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
