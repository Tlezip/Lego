from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from legotest.models import *
from legotest.serializer import *
from rest_framework import viewsets

class TestViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Test.objects.filter(is_display=True)
    serializer_class = TestSerializer


# class SectiontestViewSet(viewsets.ReadOnlyModelViewSet):
# 	for x in Test.objects.all():
# 		if x.section is None and x.is_display==True:
# 			x.is_display=False
# 			x.save()
# 	queryset = Test.objects.exclude(section=None).filter(is_display=True)
# 	# queryset = Test.objects.filter(is_display=True)

# 	serializer_class = SectioninSerializer