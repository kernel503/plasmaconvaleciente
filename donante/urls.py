from django.urls import path
from donante import views

urlpatterns = [
    path('', views.donantes, name="Donante"),
]