"""ASGI config for the Caesar Cipher UI project."""

import os

from django.core.asgi import get_asgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ciphersite.settings")

application = get_asgi_application()
