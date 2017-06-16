from django.conf.urls import url
from legocourse.views import CourseViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers


course_list = CourseViewSet.as_view(
    {
        'get': 'list',
        'post': 'create'
})
course_detail = CourseViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
course_highlight = CourseViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])



urlpatterns = format_suffix_patterns([
    url(r'^course/$', course_list, name='course-list'),
    url(r'^course/(?P<pk>[0-9]+)/$', course_detail, name='course-detail'),
    url(r'^course/(?P<pk>[0-9]+)/highlight/$', course_highlight, name='course-highlight'),
])