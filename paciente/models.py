from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Paciente(models.Model):

    nombre = models.CharField(max_length=100, blank=False, null=False)    
    tipoDeSangre = models.CharField(max_length=3, blank=False, null=False)
    hospital = models.CharField(max_length=100, blank=False, null=False)
    informacionAdicional = models.TextField(blank=True, null=True)
    cantidadReportado = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='paciente'
        verbose_name_plural='pacientes'

    def __str__(self):
        return '{0}'.format(self.nombre)