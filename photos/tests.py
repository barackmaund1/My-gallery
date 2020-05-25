from django.test import TestCase
from .models import Image,Category,Location
# Create your tests here.
class LocationTestClass(TestCase):
    # 'Set up method to run before every test'

    def setUp(self):
        self.location=Location(id=1,name='Nairobi')
        self.location.save()
    def tearDown(self):
        self.location.delete()    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))
    def test_save_location(self):
        self.location.save_location()
        locations=Location.objects.all()
        self.assertEqual(len(locations),1)
    def test_get_location(self):
        location=Location.objects.get(id=1)
        self.assertEquals(location.name,'Nairobi')
    def test_delete_location(self) :
        self.location.delete()
        locations=Location.objects.all()
        self.assertTrue(len(locations)==0)
    def test_update_location(self):
        # new_location='makueni'
        # self.location.update_location(self.location.id,new_location)
        # new_location=Location.objects.filter(name='makueni')
        # self.assertTrue(len(new_location)>0)
        pass

class CategoryTestClass(TestCase):
    def setUp(self) :
        self.category=Category(id=1,name='food') 
        self.category.save() 
    def tearDown(self):

        self.category.delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))
    def test_save_category(self):
        self.category.save_category()
        category=Category.objects.all()
        self.assertTrue(len(category)>0)
    def test_delete_category(self):
        self.category.delete() 
        category=Category.objects.all(id=1)
        self.assertTrue(len(category)==0)
    def test_update_category(self):
        pass
class TestImage(TestCase):
    def setUp(self):
        self.location = Location(name='Moringa')
        self.location.save_location()

        self.category = Category(name='home')
        self.category.save_category()

        self.image_test = Image(id=1, name='image', description='this is a test image', location=self.location,
                                category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_image(self):
        self.image_test.save_image()
        after = Image.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id, 'photos/test.jpg')
        changed_img = Image.objects.filter(image='photos/test.jpg')
        self.assertTrue(len(changed_img) > 0)

    def test_get_image_by_id(self):
        found_image = self.image_test.get_image_by_id(self.image_test.id)
        image = Image.objects.filter(id=self.image_test.id)
        self.assertTrue(found_image, image)

    def test_search_image_by_location(self):
        self.image_test.save_image()
        found_images = self.image_test.filter_by_location(location='moringa')
        self.assertTrue(len(found_images) == 1)

    def test_search_image_by_category(self):
        category = 'home'
        found_img = self.image_test.search_by_category(category)
        self.assertTrue(len(found_img) > 1)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
