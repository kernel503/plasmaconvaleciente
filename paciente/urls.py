from django.urls import path
from paciente import views

urlpatterns = [
    path('', views.pacientes, name="Paciente"),
]