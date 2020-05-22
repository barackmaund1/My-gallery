from django.db import models

# Create your models here.
class Image(models.Model):
    id=models.AutoField
    image_name=models.CharField(max_length=50)
    image_description=models.CharField(max_length=250)
    image_location=models.ForeignKey(Location,on_delete=models.CASCADE)
    image_category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to= 'images/')

    def __str__(self):
        return self.image_name

class Location(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Category(models.Model) :
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


