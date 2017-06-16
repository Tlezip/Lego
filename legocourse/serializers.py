from rest_framework import serializers
from legocourse.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'image', 'overview', 'condition', 'desc', 'is_display')