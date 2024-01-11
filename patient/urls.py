from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(f'patient', views.PatientViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('/register',views.UserRegistration.as_view(),name='register'),
    path('/login',views.UserLoginApiView.as_view(),name='login'),
    path('/logout',views.UserLogoutView.as_view(),name='logout'),
    path('/active/<uid64>/<token>/',views.activat,name='acive'),
]
