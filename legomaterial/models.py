from django.db import models


class WebLink(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='weblink/%Y/%m/', blank=True)
    url = models.URLField(max_length=256, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)


class Document(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='document/%Y/%m/', blank=True)
    document = models.FileField(upload_to='document/%Y/%m/')
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)


class FileUpload(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='fileupload/%Y/%m/', blank=True)
    file = models.FileField(upload_to='fileupload/%Y/%m/')
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    timeupdate = models.DateTimeField(auto_now=True)