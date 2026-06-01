from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Client, Car, ServiceRequest
from .serializers import ClientSerializer, CarSerializer, ServiceRequestSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        full_name = self.request.query_params.get('full_name')
        phone = self.request.query_params.get('phone')

        if full_name:
            queryset = queryset.filter(full_name__icontains=full_name)
        if phone:
            queryset = queryset.filter(phone__icontains=phone)

        return queryset

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['patch'])
    def batch_update(self, request):
        updated = []

        for item in request.data:
            obj = Client.objects.get(id=item['id'])
            serializer = self.get_serializer(obj, data=item, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            updated.append(serializer.data)

        return Response(updated)

    @action(detail=False, methods=['delete'])
    def batch_delete(self, request):
        ids = request.query_params.get('ids')

        if not ids:
            return Response({'error': 'Передайте ids через запятую'}, status=400)

        ids_list = ids.split(',')
        deleted_count, _ = Client.objects.filter(id__in=ids_list).delete()

        return Response({'deleted': deleted_count})


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        brand = self.request.query_params.get('brand')
        model = self.request.query_params.get('model')
        year = self.request.query_params.get('year')
        client = self.request.query_params.get('client')

        if brand:
            queryset = queryset.filter(brand__icontains=brand)
        if model:
            queryset = queryset.filter(model__icontains=model)
        if year:
            queryset = queryset.filter(year=year)
        if client:
            queryset = queryset.filter(client_id=client)

        return queryset

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['patch'])
    def batch_update(self, request):
        updated = []

        for item in request.data:
            obj = Car.objects.get(id=item['id'])
            serializer = self.get_serializer(obj, data=item, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            updated.append(serializer.data)

        return Response(updated)

    @action(detail=False, methods=['delete'])
    def batch_delete(self, request):
        ids = request.query_params.get('ids')

        if not ids:
            return Response({'error': 'Передайте ids через запятую'}, status=400)

        ids_list = ids.split(',')
        deleted_count, _ = Car.objects.filter(id__in=ids_list).delete()

        return Response({'deleted': deleted_count})


class ServiceRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        car = self.request.query_params.get('car')
        status_value = self.request.query_params.get('status')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        if car:
            queryset = queryset.filter(car_id=car)
        if status_value:
            queryset = queryset.filter(status=status_value)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['patch'])
    def batch_update(self, request):
        updated = []

        for item in request.data:
            obj = ServiceRequest.objects.get(id=item['id'])
            serializer = self.get_serializer(obj, data=item, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            updated.append(serializer.data)

        return Response(updated)

    @action(detail=False, methods=['delete'])
    def batch_delete(self, request):
        ids = request.query_params.get('ids')

        if not ids:
            return Response({'error': 'Передайте ids через запятую'}, status=400)

        ids_list = ids.split(',')
        deleted_count, _ = ServiceRequest.objects.filter(id__in=ids_list).delete()

        return Response({'deleted': deleted_count})