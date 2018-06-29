from .base import *
import os

DEBUG=False

SECRET_KEY=os.environ['SECRET_KEY']

ALLOWED_HOSTS=['annuaire.salletalumni.fr','164.132.97.33']

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME':os.environ['MYSQLNAME'],
            'USER':os.environ['MYSQLUSER'],
            'PASSWORD':os.environ['MYSQLPASSWORD'],
            'HOST':'127.0.0.1',
            'PORT':'3306',
            'OPTION':{
                'default-character-set':'utf8',
                },
        }}
