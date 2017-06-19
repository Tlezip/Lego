from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from legotest.models import Test
from legotest.serializer import TestSerializer
from rest_framework import viewsets

class TestViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Test.objects.filter(is_display=True)
    serializer_class = TestSerializer