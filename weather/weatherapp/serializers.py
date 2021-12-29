from rest_framework import serializers
from .models import Temperature, City
# from models import Temperature, City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('city', 'approve')


class TemperatureSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    class Meta:
        model = Temperature
        fields = ('city', 'date', 'temp')


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ('temp', 'date', 'city')
