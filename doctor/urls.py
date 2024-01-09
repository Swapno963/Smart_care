from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .  import views
router = DefaultRouter()

router.register(f'Doctors',views.DoctorViewSet)
router.register(f'review',views.ReviewViewSet)
router.register(f'avail_time',views.AvailableTimeViewSet)
router.register(f'designation',views.DesignationViewSet)
router.register(f'specialization',views.SpecializationViewSet)

urlpatterns = [
    path('',include(router.urls))
]
