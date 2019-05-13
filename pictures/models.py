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
    gallery-image = models.ImageField(upload_to='photos/', blank=True)
    Category = models.ManyToManyField(Category)
    location = models.ForeignKey(Location)

    @classmethod
    def all_images(self):

        return Image.objects.all()

    @classmethod
    def search_by_category(cls,search_images):
        images = Image.objects.filter(Category_name_icontains=search_images)
        return images
