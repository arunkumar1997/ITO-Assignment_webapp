from django.core import validators
from django import forms
from .models import Car

class CarRegistration(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['id','Company','Model','Color','Date','Price','Engine_capacity','Number_plate','Seating_capacity']
        widgets = {

            'Company':forms.TextInput(attrs={'class':'form-control'}),
            'Model':forms.TextInput(attrs={'class':'form-control'}),
            'Color':forms.TextInput(attrs={'class':'form-control'}),
            'Date':forms.TextInput(attrs={'class':'form-control'}),
            'Price':forms.TextInput(attrs={'class':'form-control'}),
            'Engine_capacity':forms.TextInput(attrs={'class':'form-control'}),
            'Number_plate':forms.TextInput(attrs={'class':'form-control'}),
            'Seating_capacity':forms.TextInput(attrs={'class':'form-control'}),
        }