from django.db import models


class Scorm(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='scorm/%Y/%m/', blank=True)
    url = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)