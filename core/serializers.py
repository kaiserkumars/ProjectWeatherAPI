from rest_framework import serializers
from . import models

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WeatherData
        fields = ('location', 'metric', 'year','month','value')

