from django import forms
from .models import Donante

# Create your forms here.

class donanteFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=50, widget=forms.TextInput({'class':'form-control', 'placeholder':'Nombre Completo'}))
    telefonoContacto = forms.CharField(min_length=8, max_length=8, widget=forms.TextInput({'class':'form-control', 'placeholder':'Ej. 70809065'}))    
    
    tipoSangre=[
        ('A+','A RH+'),
        ('A-','A RH-'),
        ('B+','B RH+'),
        ('B-','B RH-'),
        ('AB+','AB RH+'),
        ('AB-','AB RH-'),
        ('O+','O RH+'),
        ('O-','O RH-'),
    ]
    tipoDeSangre = forms.ChoiceField(choices=tipoSangre, widget=forms.Select(attrs={'class':'form-control'}))    
    
    transporte=[
        ('Si','Si'),
        ('No','No'),
    ]
    poseeTransporte = forms.ChoiceField(choices=transporte, widget=forms.Select(attrs={'class':'form-control'}))    
    
    informacionAdicional = forms.CharField(widget=forms.Textarea({'class':'form-control','placeholder':'Por favor ingresa tu contacto y otra información necesaria para que se comuniquen contigo.'}), required=True)