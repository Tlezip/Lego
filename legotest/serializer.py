from rest_framework import serializers
from legotest.models import Test,Section,Question,Condition
from django.http import HttpResponse
from rest_framework import viewsets


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'name', 'is_display')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Section
        fields = ('num', 'name', 'pull', 'typequestion', 'full_score', 'pass_score', 'test', 'is_display', 'question')

class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = ('id', 'bank')

class TestDetailSerializer(serializers.ModelSerializer):
    section = SectionSerializer(many=True, read_only=True)
    print(section)
    # section = serializers.PrimaryKeyRelatedField(many=False, queryset=Section.objects.filter(is_display=True))
    # section = serializers.PrimaryKeyRelatedField(many=True, queryset=Section.objects.filter(is_display=True))
    class Meta:
        model = Test
        fields = ('id', 'name', 'is_display', 'section')



# class SectioninSerializer(serializers.ModelSerializer):
# 	section = SectionSerializer(many=True, read_only=True)
# 	class Meta:
# 		model = Test
# 		fields = ('id','name','section')