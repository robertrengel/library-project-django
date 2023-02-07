from datetime import date

from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from .models import Loan
from .forms import LoanForm
# Create your views here.

class RegisterLoan(FormView):
    template_name = "reader/add_register.html"
    form_class = LoanForm
    success_url = "."

    def form_valid(self, form):
        # Loan.objects.create(
        #     reader = form.cleaned_data["reader"],
        #     book = form.cleaned_data["book"],
        #     loan_date = date.today(),
        #     retuned = False
        # )

        # tambien se puede utilizar la forma de guardado usando save
        loan = Loan(
            reader=form.cleaned_data["reader"],
            book = form.cleaned_data["book"],
            loan_date = date.today(),
            retuned = False
            )
        loan.save()

        return super(RegisterLoan, self).form_valid(form)

class AddRegisterLoan(FormView):
    template_name = "reader/add_register.html"
    form_class = LoanForm
    success_url = "."

    def form_valid(self, form):
        
        obj, created = Loan.objects.get_or_create(
            reader=form.cleaned_data["reader"],
            book = form.cleaned_data["book"],
            retuned = False,
            defaults={
                "loan_date": date.today(),
            }
        )
        if created:
            return super(AddRegisterLoan, self).form_valid(form)
        else:
            return HttpResponseRedirect("/succes/")

class SuccesTemplete(TemplateView):
    template_name = "reader/loan.html"     