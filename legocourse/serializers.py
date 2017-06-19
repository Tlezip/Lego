from rest_framework import serializers
from legocourse.models import Course
from legocourse.models import Section
from legocourse.models import Material


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'image', 'overview', 'condition', 'desc', 'is_display')


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('id', 'section', 'content_type', 'content', 'sort')

class SectionSerializer(serializers.ModelSerializer):
    material = MaterialSerializer(many=True, read_only=True)
    class Meta:
        model = Section
        fields = ('id', 'course', 'name', 'sort', 'material')


class CourseDetailSerializer(serializers.ModelSerializer):
    section = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'image', 'overview', 'condition', 'desc', 'is_display', 'section')