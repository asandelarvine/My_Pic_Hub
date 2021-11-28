from django.test import TestCase
from .models import Category, Image , Location

# Create your tests here.
class ImageTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.image= Image(image = 'imageurl', name ='test_image', image_description ='image test description')
