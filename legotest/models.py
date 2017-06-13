from django.db import models

# Create your models here.
class Test(models.Model): 
	sectionID = models.ForeignKey('Section')
	name = models.CharField(max_length=50) #Test Name
	Img_name = models.ImageField(upload_to = 'image/')
	typetest = models.CharField(null = True , max_length=50)
	category = models.CharField(max_length=50)
	overview = models.TextField()
	provider = models.CharField(max_length=50)
	condition = models.TextField()
	max_submit = models.IntegerField()
	limit= models.IntegerField()
	expired = models.DateTimeField(null=True)
	descripe = models.TextField()

class Section(models.Model):
	# SectionID = models.AutoField(primary_key=True)
	sectionNum = models.AutoField(primary_key=True)
	typequestion = models.CharField(max_length=50)
	fullscore = models.IntegerField(default = 0)
	pass_score = models.IntegerField()

class Question(models.Model):
	sectionNum = models.ForeignKey(Section)
	# typequestion = models.CharField(default = "Section.Type << how to do" , max_length=50)
	# name = models.CharField(max_length=50)
	# answer = models.CharField(max_length=50)
	# numshow = models.IntegerField()