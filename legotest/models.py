from django.db import models

class Test(models.Model):
	CATEGORY_CHOICE = (
		(0, 'AIS Products & Services'),
		(1, 'Handset & Device & Gadget'),
		(2, 'IT Development'),
		(3, 'Language Center'),
		(4, 'Customer Services'),
		(5, 'Corporate Culture'),
		(6, 'Leadership Management'),
		(7, 'Business Acumen'),
		(8, 'Compliance & Regulation'),
		(9, 'Ethics & Policy'),
		(10, 'Personal Development'),
		(11, 'Innovations'),
		(12, 'Office Productivity')
	)
	PROVIDER_CHOICE = (
		(0, 'AIS Center'),
		(1, 'AIS Academy'),
		(2, 'CSM (Service)'),
		(3, 'CMD (TWZ)'),
		(4, 'ACC (Call Center)'),
		(5, 'TKM (Technical)')
	)
	name = models.CharField(max_length=50) #Test Name
	image = models.ImageField(upload_to = 'image/', null=True, blank=True)
	# typetest = models.CharField(null = True , max_length=50)
	category = models.IntegerField(choices=CATEGORY_CHOICE, blank=True, null=True)
	overview = models.TextField(null=True, blank=True)
	provider = models.IntegerField(choices=PROVIDER_CHOICE , null=True, blank=True)
	condition = models.TextField(null=True, blank=True) # this is condition detail
	max_submit = models.IntegerField(default=0) #จำนวนครั้งที่ให้สอบ
	limit= models.IntegerField(default=0) #ระยะเวลาในการทำข้อสอบ
	limit_time = models.DurationField(null=True, blank=True)
	expired = models.IntegerField(null=True, blank=True) #ระยะเวลาที่ให้เข้าสอบ
	expired_time = models.DurationField(null=True, blank=True)
	descripe = models.TextField(null=True, blank=True)
	is_display = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
	timeupdate = models.DateTimeField(auto_now=True)
	# def __init__(self):
	# 	a = Section.objects.filter(test=self.id)
	# 	if a == None:
	# 		is_display=False

	def __str__(self):
		return 'Test: ' + self.name

class Section(models.Model):
	PULL_CHOICES = (
		(0, 'Basic'),
		(1, 'Bank')
	)
	QUESTION_CHOICE=(
		(0, 'Question'),
		(1, 'Fill Description'),
		(2, 'Information'),
		(3, 'Match')
	)
	test = models.ForeignKey('Test', blank=True, null=True, related_name='section')
	pull = models.IntegerField(choices=PULL_CHOICES , default=0)
	num = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	typequestion = models.IntegerField(choices=QUESTION_CHOICE, blank=True, null=True)
	full_score = models.IntegerField(default=0)
	pass_score = models.IntegerField(default=0)
	is_display = models.BooleanField(default=False)
	def __str__(self):
		return 'Section: ' + self.name

	# SectionID = models.AutoField(primary_key=True)
	# typequestion = models.CharField(max_length=50)

class Question(models.Model):
    questionid = models.ForeignKey('legotestquestion.Question', null=True, related_name='question')
    sectionid = models.ForeignKey('Section', null=True, related_name='question')
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
	section = models.ForeignKey('Section', null=True)
	bank = models.ForeignKey('legotestquestion.Bank')
	numquestion = models.IntegerField(default=0)
	typecondition = models.IntegerField(choices=CONDITION_CHOICE, default=2)
	# keepquestion = models.ManyToManyField('legotestquestion.Bank')