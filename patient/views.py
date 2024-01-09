from django.shortcuts import render

# Create your views here.
from . import models
from . import serializer
from rest_framework import viewsets

class PatientViewSet(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializer.PatientSerializer