from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from weatherapp import views

router = routers.DefaultRouter()
router.register(r'temperature', views.TemperatureView, 'temperature')
router.register(r'city', views.CityView, 'city')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weatherapp/', include('weatherapp.urls')),
    path('api/', include(router.urls)),
]
