from rest_framework import serializers
from legocourse.models import *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'image', 'is_display')


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('id', 'content_type', 'content_object', 'sort')


class SectionSerializer(serializers.ModelSerializer):
    material = MaterialSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ('id', 'name', 'sort', 'material')


class CourseDetailSerializer(serializers.ModelSerializer):
    section = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'image', 'is_display', 'section')