from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('weather', views.WeatherViewSet, base_name='core-weather')

urlpatterns =[
    path('2/',include(router.urls)),
]