import datetime
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView, DetailView
from . models import Book, Category
# Create your views here.

class BooksInicio(ListView):
    template_name = "book/book_index.html"
    context_object_name = "books"

    def get_queryset(self):
        keyword = self.request.GET.get("kword", "")
        date1 = self.request.GET.get("date1", "")
        date2 = self.request.GET.get("date2", "")
        
        if date1 and date2:
            date1 = datetime.datetime.strptime(date1, "%Y-%m-%d").date()
            date2 = datetime.datetime.strptime(date2, "%Y-%m-%d").date()
            return Book.objects.buscar_libros_fecha(keyword, date1, date2)
        else:
            return Book.objects.buscar_libros(keyword)

class BooksTrigram(ListView):
    template_name = "book/book_index.html"
    context_object_name = "books"

    def get_queryset(self):
        keyword = self.request.GET.get("kword", "")
      
        return Book.objects.buscar_libros_trigram(keyword)

class BooksListCategory(ListView):
    template_name = "book/books_category.html"
    context_object_name = "category"

    def get_queryset(self):
        return Book.objects.books_category(1)


class BooksListByAutors(ListView):
    template_name = "book/book_list_autors.html"
    context_object_name = "list_books"

    def get_queryset(self):
        return Category.objects.listar_libros_autor(8)


class BookDetailView(DetailView):
    model = Book
    template_name = "book/books_detail.html"

