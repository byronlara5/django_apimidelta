from django.db import models
from niv.models import Niv

# Create your models here.

class Asesor(models.Model):
	id_adviser = models.CharField(max_length=3, verbose_name='ID Asesor', blank=True)
	nombre = models.CharField(max_length=30, verbose_name='Nombre')

	def __str__(self):
		return self.nombre

#File: S013OT.NEW
class Operation(models.Model):
	niv = models.ForeignKey(Niv, null=True, on_delete=models.SET_NULL, blank=True)
	job = models.CharField(max_length=6, verbose_name='Jobs', blank=True)
	date = models.CharField(max_length=8, verbose_name='Fecha de recepcion', blank=True)
	description = models.CharField(max_length=40, verbose_name='Descripcion', blank=True)

	def __str__(self):
		return self.job

class PreCita(models.Model):
	niv = models.ForeignKey(Niv, null=True, on_delete=models.SET_NULL, blank=True)
	created = models.DateField(verbose_name='Fecha Creada')
	preferred_date = models.DateField(verbose_name='Fecha Preferida')
	preferred_time = models.CharField(max_length=10, verbose_name='Horario Preferido')
	mileage = models.CharField(max_length=9, verbose_name='Kilometraje')

	def __str__(self):
		return self.niv.niv

class Cita(models.Model):
	niv = models.ForeignKey(Niv, null=True, on_delete=models.SET_NULL, blank=True)
	date = models.DateField(verbose_name='Fecha')
	time = models.TimeField(verbose_name='Hora')
	adviser = models.ForeignKey(Asesor, null=True, on_delete=models.SET_NULL, blank=True)
	seen = models.BooleanField(default=False, verbose_name='Visto')

	def __str__(self):
		return self.niv