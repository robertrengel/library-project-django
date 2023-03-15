from django.contrib import admin
from django.urls import path
from . import views

app_name = "reader_app"

urlpatterns = [
    path('add_register/', views.AddRegisterLoan.as_view(), name="add_register"),
    path('add_register_multiple/', views.AddMultipleRegisterLoan.as_view(), name="add_register_multiple"),
    path('succes/', views.SuccesTemplete.as_view(), name="add_register"),

    
]