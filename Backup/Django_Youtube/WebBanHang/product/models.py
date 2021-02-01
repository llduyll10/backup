from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255, default='')
    slug = models.CharField(max_length=255, default= '')
    description = models.TextField(default='')
    active = models.BooleanField(default=True)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='')
    product_img = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    active = models.BooleanField(default=True)
    price = models.IntegerField(default=0)

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='')
    price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    inventory = models.BooleanField(default=0)
