from django.shortcuts import render
from .models import Autor
# Create your views hefromre.
from django.views.generic import TemplateView, ListView, FormView

class AutorInicio(ListView):
    template_name = "autor/autor_index.html"
    context_object_name = "autores"

    def get_queryset(self):
        keyword = self.request.GET.get("kword", None)
        return Autor.objects.buscar_autor4(keyword)
