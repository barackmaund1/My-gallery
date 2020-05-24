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
        new_location='makueni'
        self.location.update_location(self.location.id,new_location)
        new_location=Location.objects.filter(name='makueni')
        self.assertTrue(len(new_location)>0)

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
        self.category.save_category()
