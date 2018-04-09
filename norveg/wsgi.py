"""
WSGI config for norveg project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "norveg.settings")

application = get_wsgi_application()

# Use whitenoise package to serv static files on heroku
# from whitenoise.django import DjangoWhiteNoise
# Application = DjangoWhiteNoise(application)