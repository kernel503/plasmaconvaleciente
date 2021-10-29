from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Donante(models.Model):

    nombre = models.CharField("Nombre", max_length=50)    
    telefonoContacto = models.IntegerField("Teléfono", blank=False, null=False)
    
    TIPOS_SANGRE=[
        ('A+','A RH+'),
        ('A-','A RH-'),
        ('B+','B RH+'),
        ('B-','B RH-'),
        ('AB+','AB RH+'),
        ('AB-','AB RH-'),
        ('O+','O RH+'),
        ('O-','O RH-'),
    ]
    tipoDeSangre = models.CharField("Tipo de Sangre", max_length=25, choices=TIPOS_SANGRE, blank=False, null=False)

    POSEE_TRANSPORTE=[
        ('Si','Si'),
        ('No','No'),
    ]
    poseeTransporte = models.CharField("Posee transporte", max_length=2, choices=POSEE_TRANSPORTE, blank=False, null=False)
    
    informacionAdicional = models.TextField("Información adicional", null=True, blank=True)
    
    cantidadReportado = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
     
    class Meta:
        verbose_name='donante'
        verbose_name_plural='donantes'

    def __str__(self):
        return '{0}'.format(self.nombre)