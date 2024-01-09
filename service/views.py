from django.shortcuts import render

# Create your views here.
from . import models 
from . import serializer
from rest_framework import viewsets


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializer.ServiceSerializer