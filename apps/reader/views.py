from django.shortcuts import render
from django.views.generic.edit import FormView
from .models import Loan
from .forms import LoanForm
# Create your views here.

class RegisterLoan(FormView):
    template_name = "reader/add_register.html"
    form_class = LoanForm
    success_url = "."

    def form_valid(self, form):
        return super(RegisterLoan).form_valid(form)