from django.contrib import admin
from .models import Product, Category

from import_export import resources
from import_export.admin import ExportActionMixin


# Export in PDF, EXCEL, CSV etc
class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('id', 'category', 'name', 'description', 'purchase_price', 'selling_price', 'discount_price', 'is_published', 'brand', 'image')


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'photo'
    ]
    list_filter = ['name', 'description']
    search_fields = ['name']
    

class ProductAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = ProductResource

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
