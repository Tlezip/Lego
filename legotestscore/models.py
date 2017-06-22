from django.db import models

<<<<<<< HEAD
=======
# Create your models here.
# class score(models.Model):

>>>>>>> 6b21d74a9c21f2309a437d20deaa60350a537d6b
class scoresection(models.Model):
	# userid = models.ForeignKey() Get from user table
	testid = models.ForeignKey('legotest.Test')
	sectionid = models.ForeignKey('legotest.Section')
	score_section = models.IntegerField()
