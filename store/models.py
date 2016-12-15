from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
from django.db import models

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    publish_date = models.DateField(default=timezone.now)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=0)
    year = models.IntegerField(default=1970)

class Boot(models.Model):
    brand = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    size = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
