import os

from django.db import connection

from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS = [os.environ.get('WEBSITE_HOSTNAME')]
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']]
DEBUG = False

os.environ["APPLICATIONINSIGHTS_CONNECTION_STRING"] = "InstrumentationKey=d714fe96-3d4b-4991-ab0b-8783e893b74d;IngestionEndpoint=https://northeurope-2.in.applicationinsights.azure.com/;LiveEndpoint=https://northeurope.livediagnostics.monitor.azure.com/"
configure_azure_monitor()


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

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "djangopremier-database",
        'USER': "Oliezhyk",
        'PASSWORD': "197346825Oleg",
        'HOST': "premierdjango-server.mysql.database.azure.com",
    }
}