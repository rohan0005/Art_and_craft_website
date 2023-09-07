from django.db import models

#for using foreign key
from django.contrib.auth.models import User






#category choice 

CATEGORY_CHOICES = (
    ('paintings', 'Paintings'),
    ('sculptures', 'Sculptures'),
    ('crafts', 'Crafts'),

)


# Creating UserUploadedItem form

class UserUploadedItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to = "images/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Cart(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image= models.ImageField(upload_to = "cart/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title