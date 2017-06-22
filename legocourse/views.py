from rest_framework import viewsets
from rest_framework.response import Response
from legocourse.serializers import *
from legocourse.models import *


class CourseDisplayViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.filter(is_display=True)
    serializer_class = CourseSerializer

    def retrieve(self, request, pk=None):
        detail = Course.objects.filter(id=pk)
        serializer = CourseDetailSerializer(detail, many=True)
        return Response(serializer.data)

