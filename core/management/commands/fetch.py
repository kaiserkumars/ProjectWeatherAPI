from django.core.management.base import BaseCommand
import requests


class Command(BaseCommand):
	help = 'Displays current time'

	def handle(self, *args, **kwargs):
		
		url = "https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/Rainfall-UK.json"
		response  = requests.get(url)
		response = response.json()
		print(response)