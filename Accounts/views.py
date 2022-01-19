from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import GsUser
from .serializers import UserSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = GsUser.objects.all()