from .models import Vehicle, Person
from django.shortcuts import render

# Create your views here.

def index(request):
    cars = Vehicle.objects.all()
    return render(request, 'index.html', {'cars':cars})

def person_view(request,person_id):
    p = Person.objects.get(id=person_id)
    return render(request, 'person.html', {'person':p})
    