from django.contrib import admin
from .models import City, Parameter, Measurement, Location

# Register your models here.

admin.site.register(City)
admin.site.register(Parameter)
admin.site.register(Measurement)
admin.site.register(Location)
