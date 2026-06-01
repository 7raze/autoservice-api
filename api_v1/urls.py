from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ClientViewSet, CarViewSet, ServiceRequestViewSet

router = DefaultRouter()

router.register('clients', ClientViewSet, basename='client')
router.register('cars', CarViewSet, basename='car')
router.register('service-requests', ServiceRequestViewSet, basename='service-request')

urlpatterns = [
    path('', include(router.urls)),
]