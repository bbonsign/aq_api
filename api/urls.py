from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'cities', views.CityViewSet)
router.register(r'parameters', views.ParameterViewSet)
# router.register(r'measurements', views.MeasurementViewSet)
# router.register(r'locations', views.LocationViewSet)

urlpatterns = [
    path('measurements/add/', views.add_measurement),
    path('measurements/', views.MeasurementViews.as_view()),
    path('locations/', views.LocationViewSet.as_view()),
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
