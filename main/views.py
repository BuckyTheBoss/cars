from .models import Vehicle, Person
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

# Create your views here.

def index(request):
    cars = get_list_or_404(Vehicle, color='red')
    return render(request, 'index.html', {'cars':cars})

def person_view(request,person_id):

    # p = Person.objects.get(id=person_id)
    p = get_object_or_404(Person, id=person_id)

    return render(request, 'person.html', {'person':p})
    