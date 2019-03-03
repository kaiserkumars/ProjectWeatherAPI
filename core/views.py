from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Q
from . import models
from . import serializers


class WeatherViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.WeatherSerializer
	# def retrieve(self, request, *args, **kwargs):
	#     return Response({'something': 'djbftom JSON'})
	
	def list(self, request, *args, **kwargs):  # override list
		output={}
		queryset=self.get_queryset()
		for record in queryset.iterator(): 
			output[str(record.year)+'-'+str(record.month)]=record.value
		return Response(output)

	def get_queryset(self):
		location = self.request.query_params.get('location')
		metric= self.request.query_params.get('metric')
		start = self.request.query_params.get('start')
		end = self.request.query_params.get('end')
		starty = start[:4]
		startm = start[5:]
		endy=end[:4]
		endm=end[5:]
		queryset = models.WeatherData.objects.filter(location=location,metric=metric,year__gte=starty, year__lte=endy,month__gte=startm,month__lte=endm) 
		return queryset