from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashbaord, name ='dashboard'),
    path('bot/<str:bot_name>', views.bot_dashboard, name = 'bot-dashboard'),
    path('update-location/<str:bot_name>', views.updateLocation, name = 'update-location'),

    path('map/', views.mapView, name = 'map'),
    path('map-update', views.updateMap.as_view(), name = 'Map-update'),


]

