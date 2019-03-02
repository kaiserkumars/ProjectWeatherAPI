from rest_framework import serializers
from . import models

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WeatherData
        fields = ('location', 'metric', 'year','month','value')

# class WeatherSerializer(serializers.ModelSerializer):
#     ingredients = IngredientSerializer(many=True, read_only=True)
#     class Meta:
#         model = models.WeatherData
#         fields = ('slug', 'name', 'description', 'cooking_instructions',
#             'cooking_time', 'preparation_time',
#             'created', 'modified')