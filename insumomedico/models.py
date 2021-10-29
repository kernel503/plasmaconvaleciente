from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class InsumoMedico(models.Model):
    nombreEstablecimiento = models.CharField(max_length=100, blank=False, null=False)
    sitio = models.TextField(blank=True, null=True)
    informacionAdicional = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Insumo Médico'
        verbose_name_plural='Insumos Médicos'

    def __str__(self):
        return self.nombreEstablecimiento