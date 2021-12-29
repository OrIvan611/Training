import datetime
from django.http import HttpResponse
from .models import City, Temperature
# from models import City, Temperature
from datetime import datetime
import time

from rest_framework import viewsets, status
from .serializers import TemperatureSerializer, CitySerializer, WeatherSerializer
# from serializers import TemperatureSerializer, CitySerializer, WeatherSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class CityView(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class WeatherView(APIView):
    serializer_class = WeatherSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            temp = serializer.data.temp
            city = serializer.data.city
            date = serializer.data.date



class TemperatureView(viewsets.ModelViewSet):
    serializer_class = TemperatureSerializer
    queryset = Temperature.objects.all()


def search(request):
    city, date = request.GET['city'], request.GET['date']
    cities = City.objects.filter(city=city)
    if not cities:
        return HttpResponse('The city you chose is not in the DataBase. Please pick another one.')
    city = cities[0]
    temperatures = Temperature.objects.filter(city=city, date=date)
    if not temperatures:
        return HttpResponse('The date you chose for this city is not in the DataBase. Please change it or pick another city.')
    temperature = temperatures[0]
    if city.approve == True:
        return HttpResponse('the temperature:' + str(temperature.temp))
    else:
        return HttpResponse('City not allowed')