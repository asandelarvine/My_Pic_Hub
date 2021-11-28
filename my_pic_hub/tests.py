from django.test import TestCase
from .models import Category, Image , Location

# Create your tests here.
class ImageTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.image= Image(image = 'imageurl', name ='test_image', image_description ='image test description')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_images(self):
        self.image.save_images()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_images(self):
        self.image.save_images()
        self.image.delete_images()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)

    def test_all_images(self):
        self.image.save_images()
        retrieved_images = Image.get_images()
        saved_images = Image.objects.all()
        self.assertTrue(len(retrieved_images)==len(saved_images))

