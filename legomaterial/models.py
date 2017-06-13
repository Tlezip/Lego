from django.db import models
from legocourse.models import Material



class WebLink(models.Model):
    material = models.OneToOneField(Material, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to='weblink/%Y/%m/')
    data = models.URLField(max_length=256)


class Document(models.Model):
    material = models.OneToOneField(Material, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to='document/%Y/%m/')
    document = models.FileField(upload_to='document/%Y/%m/')


class FileUpload(models.Model):
    material = models.OneToOneField(Material, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to='fileupload/%Y/%m/')
    file = models.FileField(upload_to='fileupload/%Y/%m/')