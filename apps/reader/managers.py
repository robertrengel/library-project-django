from django.db import models
from django.db.models import Q, Count, Avg
from django.db.models.functions import Lower, Trim

class LoanManager(models.Manager):

    def age_reader_loan(self):
        return self.filter(book__id= 1).aggregate(avg_age= Avg("reader__age"))

    def num_loan_books(self):
        return self.values("book").annotate(num_loan = Count("book"),  titulo = Trim("book__title"))
        # la funcion values hace que la funcion annotate devuelve un conjunto
        # de valores mas especificos al limitar la referencia de como ordena los datos
        # ademas de que ya no devuelve un query normal sino un query de diccionarios