from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('weather', views.WeatherViewSet)

urlpatterns =[
    path('1/',views.all_wd, name='home'),
    path('2/',include(router.urls)),
]