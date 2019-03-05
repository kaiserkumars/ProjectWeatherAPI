from django.db import models
from datetime import date

class WeatherData(models.Model):
	location = models.CharField(max_length=50)
	metric = models.CharField(max_length=50)
	date = models.DateField()
	value= models.FloatField(null=True,blank=True)
	class Meta:
		unique_together=(('location','metric','date'),) #To prevent duplicate records
	def __str__(self):
		return self.location

