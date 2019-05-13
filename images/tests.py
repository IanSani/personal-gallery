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

    def test_update(self):
        self.drinks.save()
        self.drinks.name ="MoreDrinks"
        self.asserTrue(self.drinks.name == 'MoreDrinks')

    def test_all_images(self):
        self.drinks.save()
        images = Image.all_images()
        self.asserTrue(len(images) >0)

    def test_search_by_category(self):
        self.drinks.save()
        location = Image.view_location(self.nairobi)
        self.asserTrue(len(location) >0)

    def test_view_category(self):
        self.drinks.save()
        location =Image.view_category(self.music)
        self.asserTrue(len(Category) >0)

class LocationTest(Test)
    def setUp(self):
        self.nairobi = Location(name='nairobi')

    def test_instance(self):
        self.nairobi.save()
        self.asserTrue(isinstance(self.nairobi, Location))
