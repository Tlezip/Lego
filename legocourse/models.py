from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Course(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='course/%Y/%m/', blank=True, null=True)
    overview = models.TextField(max_length=250, blank=True, null=True)
    condition = models.TextField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    is_display = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)


class Section(models.Model):
    course = models.ForeignKey(Course, related_name='section')
    name = models.CharField(max_length=200)
    sort = models.IntegerField(db_index=True, default=1)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.sort = Section.objects.filter(course=self.course).count() + 1
        super(Section, self).save(*args, **kwargs)


class Material(models.Model):
    TYPE_CHOICES = {
        (0, 'Video'),
        (1, 'WebLink'),
        (2, 'Document'),
        (3, 'Test'),
        (4, 'Audio'),
        (5, 'Scorm'),
        (6, 'FileUpload')
    }

    section = models.ForeignKey(Section, related_name='material')
    types = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, default=0)
    sort = models.IntegerField(db_index=True, default=1)

    limit = models.Q(app_label='legovideo', model='video') | models.Q(app_label='legomaterial', model='weblink') | \
            models.Q(app_label='legomaterial', model='document') | models.Q(app_label='legotest', model='test') | \
            models.Q(app_label='legoaudio', model='audio') | models.Q(app_label='legoscorm', model='scorm') | \
            models.Q(app_label='legomaterial', model='fileupload')

    content_type = models.ForeignKey(ContentType, limit_choices_to=limit)
    object_id = models.PositiveSmallIntegerField(default=1)
    content_object = GenericForeignKey('content_type', 'object_id')

    def create(self):
        self.sort = Material.object.count() + 1
        self.save()
