from django.shortcuts import render
from . import models
from . import serializers
# Create your views here.
from rest_framework import viewsets

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = models.ContactUs.objects.all()
    serializer_class = serializers.ContactUsSerializer

 