from django.conf import settings
from django.conf.urls import include, url
from rest_framework import routers

from . import views
from .views import ClassroomViewSet

app_name = 'classrooms'

router = routers.DefaultRouter()
router.register(r'classrooms', ClassroomViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]