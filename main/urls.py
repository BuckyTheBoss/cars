from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index' ),
    path('person/<int:person_id>', views.person_view, name='person' ),
    path('add_vehicle', views.add_vehicle, name='add_vehicle'),
    path('add_passenger', views.add_person_to_car, name='add_passenger')
]