from django.test import TestCase
from .models import *

# Create your tests here.
class ImageTest(TestCase):
    def setUp(self):
        self.nairobi =Location.objects.create(name ='nairobi')
        self.fun = Category.objects.create(name='fun')
        self.music = Category.objects.create(name='music')

        self.drinks = Image.objects.create(name='drinks',location=self.nairobi, description='picture of a drinks')
        self.drinks.Category.add(self.fun)
        self.drinks.Category.add(self.music)

    def test_instance(self):
        self.drinks.save()
        self.assertTrue(isinstance(self.drinks, Image))

    def test_delete_image(self):
        self.drinks.save()
        self.drinks.delete()
        self.assertTrue(len(Image.objects.all())== 0)

    def test_update(self):
        self.drinks.save()
        self.drinks.name ="MoreDrinks"
        self.assertTrue(self.drinks.name == 'MoreDrinks')

    def test_all_images(self):
        self.drinks.save()
        images = Image.all_images()
        self.assertTrue(len(images) >0)

    def test_search_by_category(self):
        self.drinks.save()
        Category = Image.view_location(self.nairobi)
        self.assertTrue(len(Category) >0)

    def test_view_category(self):
        self.drinks.save()
        location =Image.view_category(self.music)
        self.assertTrue(len(location) >0)

class CategoryTest(TestCase):
    def setUp(self):
        self.nature = Category(name='nature')

    def test_instance(self):
        self.nature.save()
        self.assertTrue(isinstance(self.nature, Category))

class LocationTest(TestCase):
    def setUp(self):
        self.nairobi = Location(name='nairobi')

    def test_instance(self):
        self.nairobi.save()
        self.assertTrue(isinstance(self.nairobi, Location))
