from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.

def all_wd(request):
	result=[]
	for rec in models.WeatherData.objects.all():
		result.append({'Location':rec.location,'Metric':rec.metric,'Year':rec.year,'Month':rec.month,'Value':rec.value})
	return JsonResponse(result)


class WeatherViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.WeatherSerializer
    queryset = models.WeatherData.objects.all()