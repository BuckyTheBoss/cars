from .models import Vehicle, Person
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .forms import VehicleForm
# Create your views here.

def index(request):
    # cars = get_list_or_404(Vehicle, color='red')
    cars = Vehicle.objects.all()
    return render(request, 'index.html', {'cars':cars})

def person_view(request,person_id):

    # p = Person.objects.get(id=person_id)
    p = get_object_or_404(Person, id=person_id)

    return render(request, 'person.html', {'person':p})
    
def add_vehicle(request):
    if request.method == 'GET':
        form = VehicleForm()
        return render(request, 'add_vehicle.html', {'form':form})
    elif request.method == 'POST':
        form = VehicleForm(request.POST)
        print(form.data)

        if form.is_valid():
            print(form.cleaned_data)
            Vehicle.objects.create(**form.cleaned_data) 

        return redirect('index')