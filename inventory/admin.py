from django.contrib import admin
from .models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'photo'
    ]
    list_filter = ['name', 'description']
    search_fields = ['name']
    

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'category',
        'image_tag',
        'selling_price',
        'purchase_price',
        'discount_price',
        'is_published',
        'brand',
        'created_at',
        'updated_at',
    ]
    list_filter = ['name','is_published','brand','category']
    search_fields = ['name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
