from django.db import models
from apps.book.models import Book
from .managers import LoanManager
from apps.autor.models import Person

# Create your models here.

class Reader(Person):
    class Meta:
        verbose_name = "Reader"


class Loan(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_loan")
    loan_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    retuned = models.BooleanField()
    objects = LoanManager()

    def save(self, *args, **kwargs):
        self.book.stock = self.book.stock - 1
        self.book.save()
        super(Loan, self).save(*args, **kwargs)

    def __str__(self):
        return  self.book.title