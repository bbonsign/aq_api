import datetime as dt
from rest_framework import serializers
from .models import City, Location, Measurement, Parameter


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'country')

    def validate(self, data):
        return data


class CityListingField(serializers.ReadOnlyField):
    def to_representation(self, value):
        return value.name


class ParameterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parameter
        fields = ('name', 'description', 'preferred_unit')

    def validate(self, data):
        return data


class LocationSerializer(serializers.ModelSerializer):
    city = CityListingField()

    class Meta:
        model = Location
        fields = ('id', 'name', 'city', 'latitude', 'longitude')

    def validate(self, data):
        return data


class MeasurementSerializer(serializers.Serializer):
    parameter = ParameterSerializer(read_only=True)
    # location = LocationSerializer(read_only=True)
    value = serializers.FloatField(read_only=True)
    date = serializers.DateTimeField(read_only=True)

    def validate_content(self, data):
        return data

    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        # prefetch_related for "to-many" relationships
        queryset = queryset.select_related(
            'parameter',
            # 'location',
            'location__city')
        return queryset
