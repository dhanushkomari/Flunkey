from rest_framework import serializers
from .models import Delivery, FinalDelivery, Bot  

class FinalDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = FinalDelivery
        fields = '__all__'

class deliveryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinalDeliverySerializer
        fields = ('food_delivered',)

class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = ('avialable', )