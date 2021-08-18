from .models import Vehicle, Person
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .forms import VehicleForm, SelectPassenger
# Create your views here.

def index(request):
    # cars = get_list_or_404(Vehicle, color='red')
    cars = Vehicle.objects.all()
    return render(request, 'main/index.html', {'cars':cars})

def person_view(request,person_id):

    # p = Person.objects.get(id=person_id)
    p = get_object_or_404(Person, id=person_id)

    return render(request, 'main/person.html', {'person':p})
    
def add_vehicle(request):
    cars = Vehicle.objects.all()
    if request.method == 'GET':
        form = VehicleForm()
        
    elif request.method == 'POST':
        form = VehicleForm(request.POST)
        print(form.data)

        if form.is_valid():
            print(form.cleaned_data)
            Vehicle.objects.create(**form.cleaned_data) 

            # return redirect('index')
    return render(request, 'main/add_vehicle.html', {'form':form, 'cars':cars})

 
def add_person_to_car(request):
    if request.method == "GET":
        form = SelectPassenger()
    elif request.method == 'POST':
        form = SelectPassenger(request.POST)
        if form.is_valid():
            person = form.cleaned_data['passenger']
            vehicle = form.cleaned_data['vehicle']
            vehicle.passengers.add(person)
            return redirect('person', person.id)
    return render(request, 'main/add_person_to_vehicle.html', {'form':form})
