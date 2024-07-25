from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email", "full_name", "phone_number", 
                  "address", "city", "country", "zip_code", "password"]
        extra_kwargs = {
            "password": {"write_only": True},  # Ensures password is write-only
            "id": {"read_only": True},  # Ensures id is read-only (auto-generated)
        }
        def create(self, validated_data):
            user = CustomUser.objects.create_user(**validated_data)
            return user
