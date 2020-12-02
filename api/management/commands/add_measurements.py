from django.core.management.base import BaseCommand

import json
import datetime as dt
from api.models import City, Measurement, Parameter, Location


def add_parameters():
    with open('parameters.json', 'r') as f:
        params = json.load(f)['results']

    for param in params:
        name = param['id']
        description = param['description']
        preferred_unit = param['preferredUnit']
        Parameter.objects.get_or_create(
            name=name, description=description, preferred_unit=preferred_unit)


class Command(BaseCommand):
    help = 'Add Measurements form OpenAQ to local database, along with any needed Locations and Cities'

    def handle(self, *args, **kwargs):
        add_parameters()
        with open('measurementsUS.json', 'r') as f:
            results = json.load(f)['results']

        for result in results:
            city_name = result['city']
            city, _ = City.objects.get_or_create(name=city_name)

            location_name = result['location']
            coors = result['coordinates']
            location, _ = Location.objects.get_or_create(
                name=location_name,
                latitude=coors['latitude'],
                longitude=coors['longitude'],
                city=city
            )

            date = dt.datetime.strptime(
                result['date']['utc'], '%Y-%m-%dT%H:%M:%SZ')

            parameter_name = result['parameter']
            parameter = Parameter.objects.get(name=parameter_name)

            # Change a bit from the real API value
            value = result['value'] + 1

            Measurement.objects.get_or_create(
                date=date,
                location=location,
                value=value,
                parameter=parameter
            )
