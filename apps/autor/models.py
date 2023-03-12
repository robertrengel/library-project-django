from django.db import models
from .managers import AutorManager

# Create your models here.

class Person(models.Model):
    firts_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    nationality = models.CharField( max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.firts_name} {self.last_name}'

    class Meta:
        abstract = True

class Autor(Person):
    
    objects = AutorManager()

    