from django.db import models
from django.contrib.postgres.fields import ArrayField

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
	bank = models.ForeignKey('Bank', null=True, blank=True)
	text = models.TextField()
	type = models.IntegerField(choices=TYPE_CHOICES, default=0)
	answer = models.CharField(max_length=50)
	num_show = models.IntegerField()
	# in_bank = models.BoolenField(dafault=False)
	is_require = models.IntegerField(default=0)
	def __str__(self):
		return 'Question: ' + self.text
	

class Choice(models.Model):
	questionid = models.ForeignKey('Question')
	choice_text = models.CharField(max_length=50)
