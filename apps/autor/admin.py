from django.contrib import admin
from .models import Autor
# Register your models here.

class AutorAdmin(admin.ModelAdmin):
    list_display = [
        "firts_name",
        "last_name",
        "age",
        "id"
    ]
admin.site.register(Autor,AutorAdmin)
