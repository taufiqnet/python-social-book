from django.db import models
import uuid
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from django.utils.html import mark_safe

class Category(models.Model):
    name = models.CharField(_('category name'),max_length=255)
    description = models.TextField(_('category description'),null=True, blank=True)
    photo = models.ImageField(max_length=255, upload_to="category_images", blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    category = models.ForeignKey(Category, verbose_name=_('category'), related_name='products', on_delete=models.CASCADE)
    name = models.CharField("Product", max_length=200)
    description = models.TextField(blank=True, null=True)
    purchase_price = models.FloatField(default=0)
    selling_price = models.FloatField(default=0)
    discount_price = models.FloatField(default=0)
    is_published= models.BooleanField(_('is product published'))
    
    brand = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='product_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def image_tag(self):        
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.image.url))
        image_tag.short_description = 'Image'
    
