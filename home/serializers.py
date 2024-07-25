# serializers.py
from rest_framework import serializers
from .models import Product, ProductSpecification

class ProductSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecification
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    specifications = ProductSpecificationSerializer(many=True, read_only=True)
    descount = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'image_url', 'price', 'original_price', 'description',
            'stock_status', 'color', 'category', 'tags', 'rating', 'specifications',
            'video_url', 'descount', 'created_at', 'Bestseller'
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "descount": {"read_only": True}
        }
