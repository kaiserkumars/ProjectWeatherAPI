from django.core.management.base import BaseCommand
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
		metric = kwargs['metric']
		location = kwargs['location']
		url = "https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/Rainfall-UK.json"
		response  = requests.get(url)
		response = response.json()
		# print(response)