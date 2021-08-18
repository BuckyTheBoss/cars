from django import forms
from .models import Person
class VehicleForm(forms.Form):
    manufacturer = forms.CharField(max_length=80)
    model_name = forms.CharField(max_length=80)
    color = forms.CharField(max_length=80)
    milage = forms.IntegerField()
    owner = forms.ModelChoiceField(queryset=Person.objects.all())