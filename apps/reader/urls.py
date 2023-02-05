from django.contrib import admin
from django.urls import path
from . import views

app_name = "reader_app"

urlpatterns = [
    path('add_register/', views.RegisterLoan.as_view(), name="add_register"),
    
]