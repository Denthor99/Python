from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer, ResourceSerializer, BookingSerializer
from rest_framework import viewsets
from .models import Resource, Booking
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.

# Autenticación por token
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# Los recursos solo serán accesibles si estás registrados
class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

# Todo el mundo puede consultar, pero no puede hacer reservas si no está registrado
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer