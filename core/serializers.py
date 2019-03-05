from rest_framework import serializers
from . import models
# Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types.

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WeatherData
        fields = ('location', 'metric', 'date','value')

