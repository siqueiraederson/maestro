from .base import *

DEBUG = False
ALLOWED_HOSTS = ['192.168.99.49', 'localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'maestro',
        'USER': 'maestro',
        'PASSWORD': 'm@&$Tr025',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
