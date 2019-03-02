from django.core.management.base import BaseCommand
from core.models import WeatherData
from itertools import product
import requests



class Command(BaseCommand):
	help = 'Fetches data'

	
	def add_arguments(self,parser):
		parser.add_argument(
            '--metric', dest='metric', required=False,
            help='The metric')
		parser.add_argument(
            '--loc', dest='location', required=False,
            help='The location')

	def handle(self, *args, **kwargs):
		mtList = ['Tmax','Tmin','Rainfall'] # Metric list
		locList=['UK','England','Scotland','Wales'] # Location list
		bulk_insert=[]
		defUrl = "https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/{met}-{loc}.json" # URL to fetch data
		if kwargs['metric'] and kwargs['location'] is not None: # Checking for --metric and --location arguments 
			response = requests.get(defUrl.format(met=kwargs['metric'],loc=kwargs['location'])).json()
			for x in response:
					data = WeatherData(location=kwargs['location'], metric=kwargs['metric'],value=x['value'],year=x['year'],month=x['month'])
					bulk_insert.append(data)
		else:
			for m,l in product(mtList,locList):
				bulk_insert=[]
				response = requests.get(defUrl.format(met=m,loc=l)).json()
				for x in response:
					data = WeatherData(location=l, metric=m,value=x['value'],year=x['year'],month=x['month'])
					bulk_insert.append(data)
				try:
					WeatherData.objects.bulk_create(bulk_insert)
					print("Success.")
				except Exception as e:
					print(str(e))

				
				

				
		
		
		