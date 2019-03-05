from rest_framework import viewsets
from rest_framework.response import Response
from . import models
from . import serializers
from datetime import datetime


class WeatherViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.WeatherSerializer
	
	def list(self, request, *args, **kwargs):  # overriding list to format the json output
		output={}
		queryset=self.get_queryset()
		for record in queryset.iterator(): 
			output[str(record.date)[:-3]]=record.value
		return Response(output)

	def get_queryset(self):
		location = self.request.query_params.get('location') # location parameter for GET request
		metric= self.request.query_params.get('metric') # metric parameter for GET request
		start = self.request.query_params.get('start') # start date parameter for GET request
		startd ='{0}'.format(start[:5]+'{:0>2}'.format(start[5:]))
		end = self.request.query_params.get('end') # edn date parameter for GET request
		endd = end[:5]+'{:0>2}'.format(end[5:])
		queryset = models.WeatherData.objects.filter(location=location,metric=metric,date__gte=datetime.strptime(startd+'-01', '%Y-%m-%d'), date__lte=datetime.strptime(endd+'-01','%Y-%m-%d')) # queryset to retrieve data from the database
		return queryset