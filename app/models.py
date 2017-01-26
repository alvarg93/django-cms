from __future__ import unicode_literals

import os

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from janyga import settings


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.owner.id, filename)

class Author(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, null=True, blank=True, default=None)
    bio = models.TextField()
    facebook_url = models.CharField(max_length=200, default="", blank=True)
    twitter_url = models.CharField(max_length=200, default="", blank=True)
    short_desc = models.CharField(max_length=80, default="")
    created_at = models.DateTimeField(default=timezone.now)
    profile_photo = models.ImageField(upload_to=user_directory_path,
                                      default=os.path.join(settings.STATIC_URL, 'media', 'default.jpeg'))
    background_photo = models.ImageField(upload_to=user_directory_path,
                                         default=os.path.join(settings.STATIC_URL, 'media', 'default.jpeg'))

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return u'%s' % self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, null=True, blank=True, default=None, on_delete=models.SET_NULL)
    content = models.TextField()
    exerpt = models.TextField(default="")
    created_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)


class Comment(models.Model):
    comment = models.TextField(max_length=200, default="")
    post = models.ForeignKey(Post, null=True, blank=True, default=None)
    author = models.ForeignKey(User, null=True, blank=True, default=None, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=timezone.now)

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
