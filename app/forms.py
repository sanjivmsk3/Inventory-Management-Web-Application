from django import forms
from app.models import *


class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class LocationAddForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

class ProductMovementForm(forms.ModelForm):
    class Meta:
        model = ProductMovement
        fields = '__all__'