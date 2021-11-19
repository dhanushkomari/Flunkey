from .models import Bot_location, Map
from rest_framework import serializers

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Bot_location
        fields = ('x', 'y', 'angle')


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ('image',)