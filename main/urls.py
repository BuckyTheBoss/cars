from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index' ),
    path('person/<int:person_id>', views.person_view, name='person' ),
    path('add_vehicle', views.add_vehicle, name='add_vehicle'),
    path('add_passenger', views.add_person_to_car, name='add_passenger'),
    path('add_vehicle_new', views.add_vehicle_modelform, name='add_vehicle_new'),
    path('update_vehicle/<int:vehicle_id>', views.update_vehicle, name='update_vehicle'),
    path('update_color', views.set_color, name='update_color'),
]