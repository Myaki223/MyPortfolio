from django.contrib import admin
from .models import Product
from .models import GraphicDesign
from .models import Category

# Register your models here.


class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']

admin.site.register(Product)
admin.site.register(GraphicDesign, ImageAdmin)
admin.site.register(Category, CategoryAdmin)
