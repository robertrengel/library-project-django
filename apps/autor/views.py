from django.shortcuts import render
from .models import Autor
# Create your views hefromre.
from django.views.generic import TemplateView, ListView, FormView

class AutorInicio(ListView):
    model = Autor
    template_name = "autor/autor_index.html"
