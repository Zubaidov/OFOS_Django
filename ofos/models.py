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
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.FloatField(default=0)

    def __str__(self):
        return self.name

class ProductModel(models.Model):
    img = models.ImageField(upload_to='product_img')
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.FloatField()
    offer = models.FloatField(default=0)

    def __str__(self):
        return self.name

# Create your models here.
