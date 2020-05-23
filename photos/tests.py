from django.test import TestCase
from .models import Image,Category,Location
# Create your tests here.
class LocationTestClass(TestCase):
    # 'Set up method to run before every test'

    def setUp(self):
        self.location=Location(name='Nairobi')
        self.location.save()
    def tearDown(self):
        self.location.delete()    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))
    def test_save_location(self):
        self.location.save_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)>0)
    def test_get_location(self):
        location=Location.objects.get(id=1)
        self.assertEquals(location.name,'Nairobi')
      