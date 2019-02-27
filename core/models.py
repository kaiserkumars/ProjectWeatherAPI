from django.db import models

class WeatherData(models.Model):
	location = models.CharField(max_length=50)
	metric = models.CharField(max_length=50)
	date_added = models.DateTimeField(auto_now=True)
	value= models.FloatField(null=True,blank=True)
	year=models.IntegerField()
	month=models.IntegerField()

