from django.contrib import admin
from django.urls import path
from . import views

app_name = "book_app"

urlpatterns = [
    path('books_index/', views.BooksInicio.as_view(), name="books_index"),
    path('books_category/', views.BooksListCategory.as_view(), name="books_category"),
    path('books_autors/', views.BooksListByAutors.as_view(), name="books_autors"),
    path('books_detail/<pk>', views.BookDetailView.as_view(), name="books_detail"),
    path('books_triagram/', views.BooksTrigram.as_view(), name="books_triagram"),
]