from django.db import models
from legocourse.models import Material



class Audio(models.Model):
    material = models.OneToOneField(Material, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to='weblink/%Y/%m/')
    duration = models.DurationField()