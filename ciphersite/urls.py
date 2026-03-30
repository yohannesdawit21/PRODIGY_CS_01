"""URL configuration for the Caesar Cipher UI project."""

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("cipherweb.urls")),
]
