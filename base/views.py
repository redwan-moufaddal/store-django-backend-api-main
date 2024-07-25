from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import CustomUser
from .serializers import UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def create_user_view(request):
    # Validate password format
    email = request.data.get('email')
    if CustomUser.objects.filter(email=email).exists():
        return Response({'error': 'Email address already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    password = request.data.get('password')
    if len(password) < 8:
        return Response({'error': 'Password must contain at least one special character and be 8 characters long.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


