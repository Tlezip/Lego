from rest_framework import viewsets
from legocourse.serializers import CourseDetailSerializer
from legocourse.models import *


class CourseDetailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.filter(is_display=True)
    serializer_class = CourseDetailSerializer