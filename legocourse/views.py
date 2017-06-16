from rest_framework import viewsets
from legocourse.serializers import CourseSerializer
from legocourse.models import Course


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    #permission_classes = [IsAccountAdminOrReadOnly]
