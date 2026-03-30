"""WSGI config for the Caesar Cipher UI project."""

import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ciphersite.settings")

application = get_wsgi_application()
