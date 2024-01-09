
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact_us', include('contact_us.urls')),
    path('services', include('service.urls')),
    path('patient', include('patient.urls')),
    path('doctors', include('doctor.urls')),

]

urlpatterns += static(settings.MEDIA_URL, docunment_root = settings.MEDIA_ROOT)