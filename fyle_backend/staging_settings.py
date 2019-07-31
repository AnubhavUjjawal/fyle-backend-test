import dj_database_url

from .settings import *

ALLOWED_HOSTS = [
    'limitless-springs-53595.herokuapp.com'
]

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
