from django.db import models
from datetime import datetime
import uuid
CATEGORY_CHOICES = [
        ('imprimante', 'Imprimante'),
        ('ancre', 'Ancre'),
        ('ruban', 'Ruban'),
        ('bac', 'Bac de dechet'),
    ]


class Product(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    stock_status = models.CharField(max_length=50, choices=(('in_stock', 'In Stock'), ('out_of_stock', 'Out of Stock')))
    color = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    tags = models.CharField(max_length=255, help_text="Create up to three tags about your product")
    rating = models.FloatField(default=3)
    video_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    Bestseller = models.IntegerField(default=0)
    @property
    def descount(self):
        if self.original_price and self.original_price > self.price:
            if self.original_price > self.price :
                descount = ((self.original_price - self.price) / self.original_price) * 100
                return descount

    def __str__(self):
        return str(f"{self.name} : {self.created_at}")

class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specifications')
    gtin = models.CharField(max_length=50, null=True, blank=True)
    marque = models.CharField(max_length=100, null=True, blank=True)
    fonctions = models.CharField(max_length=100, null=True, blank=True)
    technology = models.CharField(max_length=255, null=True, blank=True)
    print_speed = models.CharField(max_length=255)
    first_print_out_time = models.CharField(max_length=255)
    max_monthly_duty_cycle = models.CharField(max_length=255)
    recommended_monthly_volume = models.CharField(max_length=255)
    printer_language_duplex_mode = models.CharField(max_length=255)
    printer = models.CharField(max_length=255)
    glass = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.product.name} Specifications"

class FormSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"FormSubmission from {self.name} on {self.submitted_at}"