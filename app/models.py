from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, null=True, blank=True, default=None)
    bio = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return u'%s' % self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, null=True, blank=True, default=None)
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
