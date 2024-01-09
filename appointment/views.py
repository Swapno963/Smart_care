from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializer
# Create your views here.
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializer.AppointmentSerializer


    def get_queryset(self):
        return super().get_queryset()
    
        patient_id = self.request.query_params.get('patient_id')
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset