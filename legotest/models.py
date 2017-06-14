from django.db import models

class Test(models.Model): 
	name = models.CharField(max_length=50) #Test Name
	image = models.ImageField(upload_to = 'image/')
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
	PULL_CHOICES = (
		(0, 'Basic'),
		(1, 'Bank')
	)
	test = models.ForeignKey('Test', default=0)
	pull = models.IntegerField(choices=PULL_CHOICES , default=0)
	num = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50, default='')
	full_score = models.IntegerField(default=0)
	pass_score = models.IntegerField()

	# SectionID = models.AutoField(primary_key=True)
	# typequestion = models.CharField(max_length=50)

class Question(models.Model):
    questionid = models.IntegerField(null=True)
	# sectionNum = models.ForeignKey(Section)
	# typequestion = models.CharField(default = "Section.Type << how to do" , max_length=50)
	# name = models.CharField(max_length=50)
	# answer = models.CharField(max_length=50)
	# numshow = models.IntegerField()

class Condition(models.Model):
	CONDITION_CHOICE = (
        (0, 'random'),
        (1, 'choose')
	)
	section = models.ForeignKey('Section')
	bank = models.ForeignKey('legotestquestion.Bank')
	typecondition = models.IntegerField(choices=CONDITION_CHOICE)
	pass