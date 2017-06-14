from django.db import models

import datetime


class Audio(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='audio/%Y/%m/', null=True, blank=True)
    duration = models.DurationField(default=datetime.timedelta(0))
    audio_url = models.CharField(max_length=200, default='')
