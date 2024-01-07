from django.contrib import admin

# Register your models here.
from .models import Patient

class PatientAdminModel(admin.ModelAdmin):
    list_displa= ['first_name','last_name','phone_no']


    def first_name(self,obj):
        return obj.user.first_name

    def last_name(self,obj):
        return obj.user.last_name
    

admin.site.register(Patient,PatientAdminModel)