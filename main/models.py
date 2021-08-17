from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class ImageProfile (models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    image = models.URLField()

    def __str__(self):
        return f'ImageProfile of {self.person}'

class Vehicle(models.Model):
    manufacturer = models.CharField(max_length=80)
    model_name = models.CharField(max_length=80)
    color = models.CharField(max_length=80)
    milage = models.IntegerField()
    top_speed = models.IntegerField(default=50)
    owner = models.ForeignKey(Person, on_delete=models.PROTECT)


    def __str__(self):
        return f'{self.manufacturer} {self.model_name}'

