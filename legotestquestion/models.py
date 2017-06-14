from django.db import models

# Create your models here.
class Question(models.Model):
	QUESTION_TYPE_CHOICES = (
    (0, 'Multiple Choice'),
    (1, 'Fill Description'),
    (2, 'Fill the Box'),
    (3, 'Match'),
	)
	question_text = models.TextField()
	question_type = models.IntegerField(choices=QUESTION_TYPE_CHOICES , default=0)
	question_answer = models.CharField(max_length=50)
	question_num_show = models.IntegerField()
	question_isrequire = models.IntegerField(default = 0)
	pass

class Bank(models.Model):
	questions = models.ManyToManyField(Question)



class Choice(models.Model):
	questionid = models.ForeignKey('Question')
	choice_text = models.CharField(max_length=50)
