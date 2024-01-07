from django.contrib import admin

# Register your models here.
from .models import Specialization,Designation,AvailableTime,Doctor,Review


admin.site.register(Specialization)
admin.site.register(Designation)
admin.site.register(AvailableTime)
admin.site.register(Doctor)
admin.site.register(Review)