from django import forms
from .models import Paciente
from paciente.listado import *
# Create your forms here.

class PacienteForm(forms.Form):
    nombre = forms.CharField(required=True, max_length=50, widget=forms.TextInput({'class':'form-control', 'placeholder':'Nombre Completo'}))
    tipoDeSangre = forms.ChoiceField(choices=getSangre(), widget=forms.Select(attrs={'class':'form-control'}))
    #hospital = forms.ChoiceField(choices=getHospitales(), widget=forms.Select(attrs={'class':'form-control'}))
    hospital = forms.CharField(required=True, max_length=100, widget=forms.TextInput({'class':'form-control', 'placeholder':'Ingresa el hospital donde se encuentra el paciente.'}))
    informacionAdicional = forms.CharField(widget=forms.Textarea({'class':'form-control','placeholder':'Por favor ingresa tu contacto y otra información necesaria para que se comuniquen contigo.'}), required=True)