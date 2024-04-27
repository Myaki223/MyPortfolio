from operator import mod
from unittest.util import _MAX_LENGTH
from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe

class Product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.FloatField()
    description = models.CharField(max_length = 100)


class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=30, prefix="cat", alphabet="abcdefgh12345")
    title = models.CharField(max_length=100, default="Graphic Design")
    description = models.TextField(default="desciption")
    image = models.ImageField(upload_to="category", default="category.jpg")
    
    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50">' % (self.image.url))
    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50">' % (self.image.url))
    def __str__(self):
        return self.title

class GraphicDesign(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to='img')
    def __str__(self):
        return self.caption
