from django.contrib import admin
from .models import Client, Car, ServiceRequest


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone', 'email', 'created_at']
    search_fields = ['full_name', 'phone', 'email']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'brand', 'model', 'year', 'license_plate']
    list_filter = ['brand', 'year']
    search_fields = ['brand', 'model', 'license_plate']


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'car', 'status', 'price', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['description']