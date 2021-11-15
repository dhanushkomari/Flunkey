from .models import Bot_location
from rest_framework import serializers

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Bot_location
        fields = ('x', 'y', 'angle')

