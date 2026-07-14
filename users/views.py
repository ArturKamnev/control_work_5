
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.permissions import AllowAny

class RegistrationApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]


