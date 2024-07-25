# views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import status
from .models import *
from .serializers import ProductSerializer
from datetime import timedelta
from django.utils import timezone
from django.shortcuts import get_object_or_404
@api_view(["GET"])
@permission_classes([AllowAny])
def home_page_data(request):
    data = {}

    # Get the current time and subtract one day
    one_day_ago = timezone.now() - timedelta(minutes=5)
    
    # Filter products that were created more than one day ago and get the latest 3
    tree_products = Product.objects.filter(created_at__lte=one_day_ago).order_by("-id")[:3]
    serializer_tree_products = ProductSerializer(tree_products, many=True)
    data['latest_products'] = serializer_tree_products.data

    # Get the next 8 new products
    new_8_product = Product.objects.all().order_by("-id")[3:11]
    serializer_new_8_product = ProductSerializer(new_8_product, many=True)
    data['new_products'] = serializer_new_8_product.data
    best_selling_products = Product.objects.all().order_by('-Bestseller')[:4]
    # Serialize the queryset
    serializer_best_selling_products = ProductSerializer(best_selling_products, many=True)
    data['bestsellers'] = serializer_best_selling_products.data
    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def shop_page_data(request):
    data = {}
    get_products = Product.objects.all().order_by("-id")
    serializer_get_products = ProductSerializer(get_products, many=True)
    data['all products'] = serializer_get_products.data
    return Response(data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def contact_page_data(request):
    if request.method == "POST":
        # Extract form data from the request
        name = request.data.get("name")
        email = request.data.get("email")
        message = request.data.get("message")

        # Save the data to the database
        submission = FormSubmission(name=name, email=email, message=message)
        submission.save()

        # Create a response message
        data = {
            "message": "Form data received and saved successfully",
            "received_data": {
                "name": name,
                "email": email,
                "message": message
            }
        }
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
@permission_classes([AllowAny])
def one_product_data(request, pk):
    # Retrieve the product by primary key
    product = get_object_or_404(Product, pk=pk)
    # Serialize the product data
    serializer = ProductSerializer(product)
    # Return the serialized data in the response
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([AllowAny])
def products_by_category(request, category):
    products = Product.objects.filter(category=category)
    # Serialize the products
    serializer = ProductSerializer(products, many=True)
    # Return the serialized data in the response
    return Response(serializer.data, status=status.HTTP_200_OK)