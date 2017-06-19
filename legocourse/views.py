from rest_framework import viewsets
from legocourse.serializers import CourseSerializer
from legocourse.models import Course


class CourseDisplayViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.filter(is_display=True)
    serializer_class = CourseSerializer