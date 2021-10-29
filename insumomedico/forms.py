from django import forms
from .models import InsumoMedico

# Create your forms here.

class InsumoMedicoForm(forms.ModelForm):
    class Meta:
        model = InsumoMedico
        fields = [
            'nombreEstablecimiento',
            'sitio'
        ]
        widgets = {
            'nombreEstablecimiento':forms.TextInput(attrs={'class':'form-control'}),
            'sitio':forms.TextInput(attrs={'class':'form-control'}),
        }