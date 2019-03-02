from django.db import models
from datetime import date

class WeatherData(models.Model):
	location = models.CharField(max_length=50)
	metric = models.CharField(max_length=50)
	date_added = models.DateField(auto_now_add=True)
	value= models.FloatField(null=True,blank=True)
	year=models.IntegerField()
	month=models.IntegerField()
	class Meta:
		unique_together=(('location','metric','year','month'),) #To prevent duplicate records
	def __str__(self):
		return self.location

