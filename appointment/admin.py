from django.contrib import admin

from .models import Appointment
# Register your models here.

class AppointmentAdminModel(admin.ModelAdmin):
    list_display = ['doc_name','doc_name','appointment_status','appointment_type','symptom','time','cancel']

    def doc_name(self, obj):
        return obj.doctor.user.first_name
    
    def doc_name(self, obj):
        return obj.patient.user.first_name
    
admin.site.register(Appointment)