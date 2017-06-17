from rest_framework import serializers
from legotest.models import Test,Section,Question,Condition
from django.http import HttpResponse
from rest_framework import viewsets

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'