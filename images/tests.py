from django.test import TestCase
from .models import *

# Create your tests here.
class ImageTest(TestCase):
    def setUp(self):
        self.nairobi =Location.objects.create(name ='nairobi')
        self.fun = Category.objects.create(name='fun')
        self.music = Category.objects.create(name='music')

        self.drinks = Image.objects.create(name='drinks',location=self.nairobi, description='picture of a drinks')
        self.drink.Category.add(self.fun)
        self.drinks.Category.add(self.music)

    def test_instance(self):
        self.drink.save()
        self.assertTrue(isinstance(self.drinks, Image))

    def test_delete_image(self):
        self.drinks.save()
        self.drinks.delete()
        self.asserTrue(len(Image.objects.all())== 0)
