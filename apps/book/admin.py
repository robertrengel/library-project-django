from django.contrib import admin
from .models import Book, Category

class BooksAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "category",
        "release_date",
        "id"
    ]


admin.site.register(Book, BooksAdmin)
admin.site.register(Category)