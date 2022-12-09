from django.db import models
from apps.autor.models import Autor

# Create your models here.

class Category(models.Model):
    name = models.CharField( max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    autors = models.ManyToManyField(Autor)
    title = models.CharField(max_length=50)
    release_date = models.DateField("Realease date")
    cover = models.ImageField(upload_to="cover")
    views = models.PositiveIntegerField()

    def __str__(self):
        return self.title