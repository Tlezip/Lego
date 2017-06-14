from django.db import models


class Bank(models.Model):
	# questions = models.ManyToManyField('legotestquestion.Question')
	name = models.CharField(max_length=50, default='')

class Question(models.Model):
	TYPE_CHOICES = (
        (0, 'Multiple Choice'),
        (1, 'Fill Description'),
        (2, 'Fill the Box'),
        (3, 'Match'),
	)
	bank = models.ForeignKey('Bank',null=True)
	text = models.TextField()
	type = models.IntegerField(choices=TYPE_CHOICES, default=0)
	answer = models.CharField(max_length=50)
	num_show = models.IntegerField()
	is_require = models.IntegerField(default=0)
	

class Choice(models.Model):
	questionid = models.ForeignKey('Question')
	choice_text = models.CharField(max_length=50)
