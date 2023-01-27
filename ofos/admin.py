from django.contrib import admin
from .models import FoodModel, ProductModel

# Register your models here.

admin.site.register(FoodModel)
admin.site.register(ProductModel)