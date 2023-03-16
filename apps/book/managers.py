from django.db import models
from django.db.models import Q, Count
from django.contrib.postgres.search import TrigramSimilarity

class BooksManager(models.Manager):
    #manager para el modelo autor

    def listar_libros(self, kword):
        return self.all()

    def buscar_libros(self, kword):
        return self.filter(title__icontains=kword)

    def buscar_libros_fecha(self, kword,date1,date2):
        return self.filter(title__icontains=kword, release_date__range=(date1,date2))
    
    def buscar_libros_trigram(self, kword):
        return self.filter(title__trigram_similar=kword) if kword else self.all()[:10]
    
    def books_category(self, kword):
        return self.filter(category__id=kword)
    
    def add_book_autor(self, id_book, id_autor):
        return self.get(id = id_book).autors.add(id_autor)
    #--------------------------------------------------------------------
    def num_loan_book(self):
        return self.aggregate(num_loan = Count("book_loan"))
        #usar aggregate devuelve un diccionario python con un resultado entero
    #--------------------------------------------------------------------


class CategoryManager(models.Manager):
    def listar_libros_autor(self, kword):
        return self.filter(category_book__autors__id=kword).distinct()
#--------------------------------------------------------------------
    def category_amount(self):
        resultado = self.annotate(num_books= Count("category_book"))
        for r in resultado:
            print(r, r.num_books)
        return resultado
        #usar annotate devuelve una consuta query o sea una columna adicional llena con la consulta que estamos realizando
#--------------------------------------------------------------------