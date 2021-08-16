from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    

class Vehicle(models.Model):
    manufacturer = models.CharField(max_length=80)
    model_name = models.CharField(max_length=80)
    color = models.CharField(max_length=80)
    milage = models.IntegerField()
    top_speed = models.IntegerField(default=50)
    owner = models.ForeignKey(Person, on_delete=models.PROTECT)




