from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from legotest.models import Test
from legotest.serializer import TestSerializer
from rest_framework import viewsets

# Create your views here.
# @csrf_exempt
# def request_detail(request):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     # try:
#     #     snippet = Snippet.objects.get(pk=pk)
#     # except Snippet.DoesNotExist:
#     #     return HttpResponse(status=404)

#     if request.method == 'GET':
#         return HttpResponse(status=200)

#     elif request.method == 'PUT':
#         return HttpResponse(status=404)

#     elif request.method == 'POST':
#         return HttpResponse(status=404)

#     elif request.method == 'PATCH':
#         return HttpResponse(status=404)

class TestViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer