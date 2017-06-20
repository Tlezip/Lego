from rest_framework import serializers
from legotest.models import Test,Section,Question,Condition
from django.http import HttpResponse
from rest_framework import viewsets


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    section = SectionSerializer(many=True, read_only=True)
    class Meta:
        model = Test
        fields = ('id','name','is_display','section')

# class SectioninSerializer(serializers.ModelSerializer):
# 	section = SectionSerializer(many=True, read_only=True)
# 	class Meta:
# 		model = Test
# 		fields = ('id','name','section')