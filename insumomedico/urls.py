from django.urls import path
from insumomedico import views

urlpatterns = [
    path('', views.insumosmedicos, name="InsumoMedico"),
]