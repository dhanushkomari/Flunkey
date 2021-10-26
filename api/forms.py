from django import forms
from .models import Delivery

class Deliveryform(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ('speed_of_the_bot', 'food_type')