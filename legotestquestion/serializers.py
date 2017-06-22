from rest_framework import serializers
from legotestquestion.models import *

class TestQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'