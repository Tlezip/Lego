from django.db import models
import datetime


class Video(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='video/%Y/%m/')
    duration = models.DurationField(default=datetime.timedelta(0))
    video_url = models.CharField(max_length=200)
    status = models.IntegerField(default=0)
    type = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)