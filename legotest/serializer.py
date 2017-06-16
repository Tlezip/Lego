from rest_framework import serializers
from legotest.models import Test,Section,Question,Condition
from django.http import HttpResponse
from rest_framework import viewsets

class TestSerializer(serializers.Serializer):
    name = serializers.IntegerField()
    # title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # code = serializers.CharField(style={'base_template': 'textarea.html'})
    # linenos = serializers.BooleanField(required=False)
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    # style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')