from django.shortcuts import render
from rest_framework import viewsets
from legotestquestion.serializers import *

# Create your views here.
class TestQuestionViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Question.objects.all()
	serializer_class = TestQuestionSerializer
	