from django.db import models
from legocourse.models import Material



class Scorm(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='scorm/%Y/%m/', blank=True)
    scorm_url = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)