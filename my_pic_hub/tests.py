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

    def test_update_image(self):
        self.image.save_images()
        self.image.update_image('vincent','new_description','new_image_url')
        self.image.save_images()
        updated_name = self.image.name
        update_description = self.image.image_description
        updated_url = self.image.image
        self.assertTrue(updated_name == 'vincent' and update_description== 'new_description' and updated_url == 'new_image_url')

    def test_get_image_by_id(self):
        self.image.save_images()
        gotten_image = Image.get_image_by_id(5)
        self.assertEqual(gotten_image.id == 5)


class LocationTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.location= Location(name = 'test_location')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_locations(self):
        self.location.save_locations()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_locations(self):
        self.location.save_locations()
        self.location.delete_locations()
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)
 
