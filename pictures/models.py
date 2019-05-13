from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class Category(models.Model):
    name =models.CharField(max-length=30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name =models.CharField(max-length=30)

    def __str__(self):
        return self.name

class Image(models.Model):
    name =models.CharField(max-length=50)
    description = HTMLField()
    gallery-image = models.ImageField(upload_to='', blank=True)
    Category = models.ManyToManyField(Category)
    location = models.ForeignKey(Location)
