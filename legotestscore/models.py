from django.db import models

# Create your models here.
class score(models.Model):

class scoresection(models.Model):
	userid = models.IntegerField()
	testid = models.IntegerField()
	sectionid = models.IntegerField()
	score_section = models.IntegerField()
