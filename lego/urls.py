from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from legocourse.views import CourseViewSet
from legotest.views import TestViewSet


router = DefaultRouter()
router.register(r'course', CourseViewSet)
router.register(r'test', TestViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]