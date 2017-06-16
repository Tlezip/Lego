from django.db import models

# Create your models here.
class score(models.Model):

class scoresection(models.Model):
	# userid = models.ForeignKey() Get from user table
	testid = models.ForeignKey('legotest.Test')
	sectionid = models.ForeignKey('legotest.Section')
	score_section = models.IntegerField()
