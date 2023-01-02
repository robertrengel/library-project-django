from django.db import models
from .managers import AutorManager

# Create your models here.
class Autor(models.Model):
    firts_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    nationality = models.CharField( max_length=50)
    age = models.PositiveIntegerField()
    objects = AutorManager()

    def __str__(self):
        return self.firts_name + ' ' + self.last_name