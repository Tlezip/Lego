from django.db import models



class Course(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='course/%Y/%m/')
    overview = models.TextField(max_length=250, null=True)
    condition = models.TextField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    is_display = models.BooleanField(default=True)
    term_info = models.TextField(blank=True, null=True)


class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    outline_name = models.CharField(max_length=200)
    sort = models.IntegerField(default=0)

    def create(self):
        self.sort = Section.object.count() + 1


class Material(models.Model):
    TYPE_CHOICES = (
        (4, 'Audio'),
        (0, 'Video'),
        (1, 'WebLink'),
        (2, 'Document'),
        (5, 'Scorm'),
        (3, 'Test')
    )

    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    type = models.IntegerField(choices=TYPE_CHOICES, default=0)