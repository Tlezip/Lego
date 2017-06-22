from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import *
from legovideo.models import Video
from legoaudio.models import Audio
from legoscorm.models import Scorm
from legomaterial.models import  *


# class VideoInline(GenericTabularInline):
#     model = Video
#
# class AudioInline(GenericTabularInline):
#     model = Audio
#
# class ScormInline(GenericTabularInline):
#     model = Scorm
#
# class WebLinkInline(GenericTabularInline):
#     model = WebLink
#
# class DocumentInline(GenericTabularInline):
#     model = Document
#
# class FileDownloadInline(GenericTabularInline):
#     model = FileDownload
#
# class MaterialAdmin(admin.ModelAdmin):
#     inlines = [
#         VideoInline,
#         AudioInline,
#         ScormInline,
#         WebLinkInline,
#         DocumentInline,
#         FileDownloadInline
#     ]


admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Material)