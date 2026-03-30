"""Application URLs for the Caesar Cipher UI."""

from django.urls import path

from .views import home


urlpatterns = [
    path("", home, name="home"),
]
