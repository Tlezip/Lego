from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='course/%Y/%m/')
    overview = models.TextField(max_length=250, null=True)
    condition = models.TextField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    is_display = models.BooleanField(default=True)
    # term_info = models.TextField(blank=True, null=True)


class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    sort = models.IntegerField(default=0)

    def create(self):
        self.sort = Section.object.count() + 1


class Material(models.Model):
    TYPE_CHOICES = (
        (0, 'Video'),
        (1, 'WebLink'),
        (2, 'Document'),
        (3, 'Test'),
        (4, 'Audio'),
        (5, 'Scorm'),
        (6, 'FileUpload')
    )

    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    type = models.IntegerField(choices=TYPE_CHOICES, default=0)

    content_type = models.ForeignKey('contenttypes.ContentType')
    content = models.IntegerField()

    sort = models.IntegerField(db_index=True, default=1)

    def create(self):
        self.sort = Material.object.count() + 1
        self.save()
