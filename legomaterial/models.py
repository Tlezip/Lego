from django.db import models


class WebLink(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='weblink/%Y/%m/')
    url = models.URLField(max_length=256, blank=True)


class Document(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='document/%Y/%m/')
    document = models.FileField(upload_to='document/%Y/%m/')


class FileUpload(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='fileupload/%Y/%m/')
    file = models.FileField(upload_to='fileupload/%Y/%m/')