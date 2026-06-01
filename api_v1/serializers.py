from rest_framework import serializers
from .models import Client, Car, ServiceRequest


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'id',
            'full_name',
            'phone',
            'email',
            'created_at',
        ]


class CarSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(
        source='client.full_name',
        read_only=True
    )

    class Meta:
        model = Car
        fields = [
            'id',
            'client',
            'client_name',
            'brand',
            'model',
            'year',
            'license_plate',
        ]


class ServiceRequestSerializer(serializers.ModelSerializer):
    car_info = serializers.CharField(
        source='car.__str__',
        read_only=True
    )

    class Meta:
        model = ServiceRequest
        fields = [
            'id',
            'car',
            'car_info',
            'description',
            'price',
            'status',
            'created_at',
        ]