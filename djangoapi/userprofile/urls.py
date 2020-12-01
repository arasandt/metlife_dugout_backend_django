from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from .views import get_userprofile

urlpatterns = [
    url('^', get_userprofile),
]