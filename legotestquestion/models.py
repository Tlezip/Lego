from django.db import models

# Create your models here.
class Bank(models.Model):
	questions = models.ManyToManyField(Question)

class Question(models.Model):
	question_text = models.TextField()
	question_type = models.IntegerField(choices=QUESTION_TYPE_CHOICES)
	question_answer = models.CharField(max_length=50)
	question_num_show = models.IntegerField()
	question_isrequire = models.IntegerField(default = 0)
	QUESTION_TYPE_CHOICES = (
    (0, 'Multiple Choice'),
    (1, 'Fill Description'),
    (2, 'Fill the Box'),
    (3, 'Match'),
	)

class Choice(models.Model):
	questionid = models.ForeignKey('Question')
	choice_text = models.CharField(max_length=50)
