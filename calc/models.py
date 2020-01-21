from django.db import models

# Create your models here.

class Destination(models.Model):
    
    img = models.ImageField(upload_to= "pics")
    place = models.CharField(max_length= 20)
    descrip = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default= False)