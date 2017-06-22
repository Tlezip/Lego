from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from legotest.models import *
from legotestquestion.models import Question as Question_eog
from legotest.serializer import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
# import random

class TestDetailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Test.objects.filter(is_display=True)
    serializer_class = TestDetailSerializer

class TestViewSet(viewsets.ReadOnlyModelViewSet):
    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return serializers.TestSerializer
    #     if self.action == 'retrieve':
    #         return serializers.TestDetailSerializer
    #     return serializers.Default
    queryset = Test.objects.filter(is_display=True)
    serializer_class = TestSerializer

    def retrieve(self, request, pk=None):
        detail = Test.objects.filter(is_display=True)
        serializer = TestDetailSerializer(detail, many=True, read_only=True)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = self.queryset
        for i in queryset:
            a = Section.objects.filter(test=i.id)
            if len(a)==0 and i.is_display==True:
                i.is_display=False
                i.save(update_fields=['is_display'])
        sectionset = Section.objects.filter(is_display=True)
        for i in sectionset:
            b = Question.objects.filter(sectionid=i.num)
            if len(b)==0 and i.is_display==True:
                i.is_display=False
                i.save(update_fields=['is_display'])

        # queryset = Test.objects.filter(is_display=True , section__in = Section.objects.filter(is_display=True))
        queryset = Test.objects.filter(is_display=True)
        return queryset



class ConditionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer

    @detail_route(methods=['get'])
    def question(self, request, pk=None):
        condition = self.get_object()
        queryset = condition.bank.question_set.all()
        # queryset = Question_eog.objecs.filter(condition.bank)
        if condition.typecondition == 0:
            queryset = queryset.order_by('?')[:condition.numquestion]

        # Gen response
        serializer = ConditionSerializer(queryset, many=True, read_only=True)
        return Response(serializer.data)

    # for i in self.queryset:
        #     lenbank = len(Question_eog.objects.filter(bank=i.bank))
        #     if i.typecondition == 0: #random
        #         obj = random.sample(range(1, lenbank), i.numquestion)
        #         realquestion = Question_eog.objects.filter(bank=i.bank, id__in = o




# class SectiontestViewSet(viewsets.ReadOnlyModelViewSet):
#   for x in Test.objects.all():
#       if x.section is None and x.is_display==True:
#           x.is_display=False
#           x.save()
#   queryset = Test.objects.exclude(section=None).filter(is_display=True)
#   # queryset = Test.objects.filter(is_display=True)

#   serializer_class = SectioninSerializer