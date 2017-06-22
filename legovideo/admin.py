from django.contrib import admin
from .models import *
from django.contrib.contenttypes.admin import GenericTabularInline
from legocourse.models import Material


# class MaterialInline(GenericTabularInline):
#     model = Material
#
# class VideoAdmin(admin.ModelAdmin):
#     inlines = [
#         MaterialInline,
#     ]

admin.site.register(Video)
