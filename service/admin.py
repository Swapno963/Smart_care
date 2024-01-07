from django.contrib import admin

# Register your models here.
from .models import Service

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name','description']


admin.site.register(Service,ContactModelAdmin)