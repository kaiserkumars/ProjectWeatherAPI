from django.core.management.base import BaseCommand
from core.models import WeatherData
import requests


class Command(BaseCommand):
	help = 'Fetches data'

	
	def add_arguments(self,parser):
		parser.add_argument(
            '--metric', dest='metric', required=False,
            help='The metric',)
		parser.add_argument(
            '--loc', dest='location', required=False,
            help='The location',
        )

	def handle(self, *args, **kwargs):
		#TODO: 1. Take argument from user.  2. Implement Cache/ Avoid duplicate records
		metric = kwargs['metric']
		location = kwargs['location']
		url = "https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/Rainfall-UK.json"
		response  = requests.get(url).json()
		loc = "UK"
		metric = "Rainfall"
		bulk_insert=[]
		for x in response:
			data = WeatherData(location=loc, metric=metric,value=x['value'],year=x['year'],month=x['month'])	
			bulk_insert.append(data)

		print(len(bulk_insert))
		try:
			WeatherData.objects.bulk_create(bulk_insert)
			print("Success.")
		except Exception as e:
			return str(e)

		# print(response)