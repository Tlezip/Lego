from django.conf.urls import url, include
from django.contrib import admin
from legotest import views
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from legotest.views import TestViewSet


router = routers.DefaultRouter()
router.register(r'test', views.TestViewSet)

urlpatterns = [
 	url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
