from django import forms
from .models import Person, Vehicle

def validate_name(name):
    # check if they are numbers in the name
    if not name.isalpha():
        print("Invalid name")  
        raise forms.ValidationError(f'The name {name} is invalid, it contains non-alphabetic characters')



class VehicleForm(forms.Form):
    manufacturer = forms.CharField(
        min_length=5,
        max_length=80, 
        label='Made By', 
        help_text='this is the manufacturer of the car, min 54 chars max 80', 
        error_messages= 
            {
                'required':'hello hacker', 
                'max_length':'youve exceeded the allowed char limit'
                },
        widget= forms.TextInput(attrs={'placeholder':'Kia'}),
        validators=[validate_name]
        )
    model_name = forms.CharField(max_length=80)
    color = forms.CharField(max_length=80, validators=[validate_name])
    milage = forms.IntegerField()
    owner = forms.ModelChoiceField(queryset=Person.objects.all())
    field_order = ['owner','manufacturer','model_name', 'milage', 'color' ]


class SelectPassenger(forms.Form):
    passenger = forms.ModelChoiceField(queryset=Person.objects.all())
    vehicle = forms.ModelChoiceField(queryset=Vehicle.objects.exclude(model_name='world'))

class NewVehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ['passengers', 'top_speed', 'owner']

class SetVehiclesColor(forms.Form):
    vehicles = forms.ModelMultipleChoiceField(queryset=Vehicle.objects.all())
    color = forms.CharField()