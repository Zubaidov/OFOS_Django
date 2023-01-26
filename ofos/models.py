from django.db import models

class FoodModel(models.Model):
    #offer : bool
    #id : int
    #name : str
    #img : str
    #desc : str
    #price : int
    img = models.ImageField(upload_to='images')
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

# Create your models here.
