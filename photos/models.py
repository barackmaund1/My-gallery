from django.db import models

# Create your models here.
class Location(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    def save_location(self):
        self.save()
    def delete_location(self) :
        self.delete() 
    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(location=value)    
      
    def display_locations()
class Category(models.Model) :
    name=models.CharField(max_length=50)

    def save_category(self):
        self.save()
    def delete_category(self):
        self.delete()   

    def __str__(self):
        return self.name        
class Image(models.Model):
    image_name=models.CharField(max_length=50)
    image_description=models.CharField(max_length=250)
    image_location=models.ForeignKey(Location,on_delete=models.CASCADE)
    image_category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to= 'images/')
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)
    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image
    @classmethod
    def search_by_category(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return images    
    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()        
        
class Meta:
    ordering = ['date']




