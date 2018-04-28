from django.conf import settings
from django.conf.urls import include, url
from rest_framework import routers

from . import views
from .views import AttendanceAPIView

app_name = 'attendance'


urlpatterns = [
    url(r'^attendance/?$', AttendanceAPIView.as_view())
]

