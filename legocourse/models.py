from django.db import models


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
    section = models.ForeignKey(Section, related_name='material')

    content_type = models.ForeignKey('contenttypes.ContentType')
    content = models.IntegerField()

    sort = models.IntegerField(db_index=True, default=1)

    def create(self):
        self.sort = Material.object.count() + 1
        self.save()
