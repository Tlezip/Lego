from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from legocourse.views import *
from legocourse.view_coursedetail import *
from legotest.views import *
from legotestquestion.views import *
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Pastebin API')

router = DefaultRouter()
router.register(r'course', CourseDisplayViewSet)
router.register(r'test', TestViewSet)
router.register(r'testquestion', TestQuestionViewSet)
router.register(r'condition', ConditionViewSet)

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]