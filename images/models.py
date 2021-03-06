from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name =models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Image(models.Model):
    name =models.CharField(max_length=50)
    description = HTMLField()
    gallery_image = models.ImageField(upload_to='photos/', blank=True)
    Category = models.ManyToManyField(Category)
    location = models.ForeignKey(Location)

    @classmethod
    def all_images(self):

        return Image.objects.all()

    @classmethod
    def search_by_category(cls,search_images):
        images = Image.objects.filter(name__icontains=search_images)
        return images

    @classmethod
    def view_location(cls,name):
        location = cls.objects.filter(location=name)
        return location

    @classmethod
    def view_category(cls,cat):
        Category = cls.objects.filter(Category=cat)
        return Category
