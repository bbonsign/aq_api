import json
import datetime as dt
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
import django_filters.rest_framework
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from rest_framework import viewsets, generics
from rest_framework.response import Response
from .serializers import CitySerializer, ParameterSerializer, MeasurementSerializer, LocationSerializer
from .models import City, Measurement, Parameter, Location


def home(request):
    return redirect(to='api-root')


class ParameterViewSet(viewsets.ModelViewSet):
    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class LocationViewSet(generics.ListAPIView):
    queryset = Location.objects.all().select_related('city')
    serializer_class = LocationSerializer
    filterset_fields = ['city__name']


class MeasurementViews(generics.ListCreateAPIView):
    # queryset = Measurement.objects.all().prefetch_related('location')
    serializer_class = MeasurementSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['location__city__name', 'parameter__name']

    def get_queryset(self):
        queryset = Measurement.objects.all()
        # Set up eager loading to avoid N+1 selects
        queryset = MeasurementSerializer.setup_eager_loading(
            queryset)
        return queryset


@csrf_exempt
@require_POST
def add_measurement(request):
    json_string = request.body
    data = json.loads(json_string)
    print('()())(@()#@#()@#)(@)#(@#', data)
    city_name = data['city']
    city = City.objects.get(name=city_name)
    print('***************', city)
    location = city.locations.all()[0]
    date = dt.datetime.strptime(
        data['date'], '%Y-%m-%dT%H:%M:%SZ')
    parameter_name = data['parameter']
    parameter = Parameter.objects.get(name=parameter_name)
    value = data['value']
    measurement = Measurement.objects.create(
        date=date,
        location=location,
        value=value,
        parameter=parameter
    )
    measurement.save()
    return JsonResponse({"message": "Measurement saved to database", "data": data})
