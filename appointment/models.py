from django.db import models

# Create your models here.
from patient.models import Patient
from doctor.models import Doctor,AvailableTime


APPOINTMENT_STATUS = [
    ('Completed','Completed'),
    ('Pending','Pending'),
    ('Running','Running'),
]
APPOINTMENT_TYPE = [
    ('Offline','Offline'),
    ('Online','Online'),
]


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_status = models.CharField(max_length=100, choices = APPOINTMENT_STATUS)
    appointment_type = models.CharField(max_length=100, choices = APPOINTMENT_TYPE)
    symptom = models.TextField()
    time = models.OneToOneField(AvailableTime,on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)