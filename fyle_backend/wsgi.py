"""
WSGI config for fyle_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fyle_backend.local_settings')

if os.getenv('mode') == 'STAGING':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'fyle_backend.staging_settings'
elif os.getenv('mode') == 'PRODUCTION':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'fyle_backend.prod_settings'


application = get_wsgi_application()
