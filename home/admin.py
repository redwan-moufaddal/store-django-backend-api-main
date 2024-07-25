# admin.py
from django.contrib import admin
from .models import Product, ProductSpecification

class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification
    extra = 1  # Do not display any extra empty forms
    max_num = 1  # Do not allow adding any new ProductSpecifications
    can_delete = False  # Do not allow deleting ProductSpecifications

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'original_price', 'description', 'stock_status', 'color', 'category', 'tags', 'rating', 'video_url', 'created_at', 'descount')
    search_fields = ('name', 'category', 'tags')
    inlines = [ProductSpecificationInline]

admin.site.register(Product, ProductAdmin)
