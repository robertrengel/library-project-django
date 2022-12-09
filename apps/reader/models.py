from django.db import models
from apps.book.models import Book

# Create your models here.

class Reader(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=20)
    age = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Loan(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    retuned = models.BooleanField()

    def __str__(self):
        return  self.book.title