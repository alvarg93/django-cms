from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()
    exerpt = models.TextField(default="")
    created_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)


def duplicate(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        if hasattr(object, 'created_at'):
            object.created_at = timezone.now()
        object.save()


duplicate.short_description = "Duplicate selected record"


def publish(modeladmin, request, queryset):
    for object in queryset:
        object.is_published = True
        object.save()


publish.short_description = "Publish selected posts"


def unpublish(modeladmin, request, queryset):
    for object in queryset:
        object.is_published = False
        object.save()


unpublish.short_description = "Unpublish selected posts"
