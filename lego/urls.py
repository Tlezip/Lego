from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from legocourse import views


router = DefaultRouter()
router.register(r'course', views.CourseViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^lego/', include('legocourse.urls')),
    url(r'^api/', include(router.urls)),
]