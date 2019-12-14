from django.db import models


# Create your models here.

"""TIME_CHOICES = (
	('MT','Matutino'),
	('VP','Vespertino'),
	('NT','Nocturno'),
)"""

#File: S051OT
class VehicleModel(models.Model):
	model = models.CharField(max_length=7, verbose_name='Codigo Modelo')
	description = models.CharField(max_length=30, verbose_name='Descripcion', blank=True)
	brand = models.CharField(max_length=2, verbose_name='Marca', blank=True)

	def __str__(self):
		return self.model

#File: S042OT
class Niv(models.Model):
	niv = models.CharField(max_length=8, verbose_name ='niv', blank=True, null=True)
	owner = models.CharField(max_length=40, verbose_name='Propietario', blank=True)
	address = models.CharField(max_length=40, verbose_name='Direccion', blank=True)
	city = models.CharField(max_length=40, verbose_name='Ciudad', blank=True)
	telephone = models.CharField(max_length=11, verbose_name='Telefono', blank=True)
	phone = models.CharField(max_length=7, verbose_name='Celular', blank=True)
	fax = models.CharField(max_length=7, verbose_name='Fax', blank=True)
	client_id = models.CharField(max_length=7, verbose_name='Codigo cliente', blank=True)
	email = models.CharField(max_length=40, verbose_name='Email', blank=True)
	birthdate = models.CharField(max_length=8, verbose_name='Fecha de nacimiento', blank=True)
	purchase_date = models.CharField(max_length=8, verbose_name='Fecha de compra', blank=True)
	invoice_number = models.CharField(max_length=6, verbose_name='Numero de factura', blank=True)
	niv_assignment = models.CharField(max_length=8, verbose_name='Fecha asignacion NIV', blank=True)
	job_queue = models.CharField(max_length=6, verbose_name='Ultimo Job trabajado o en proceso', blank=True)
	vin = models.CharField(max_length=20, verbose_name='Numero de chassis', blank=True)
	motor_number = models.CharField(max_length=20, verbose_name='Numero de motor', blank=True)
	brand = models.CharField(max_length=2, verbose_name='Marca', blank=True)
	model = models.ForeignKey(VehicleModel, null=True, on_delete=models.SET_NULL, blank=True)
	color = models.CharField(max_length=20, verbose_name='Color', blank=True)
	year = models.CharField(max_length=4, verbose_name='Ano', blank=True)
	plate_number = models.CharField(max_length=7, verbose_name='Numero de placa', blank=True)
	reference = models.CharField(max_length=8, verbose_name='Referencia', blank=True)
	sold_by = models.CharField(max_length=1, verbose_name='Vendido por', blank=True)
	identification = models.CharField(max_length=12, verbose_name='Cedula/RNC', blank=True)
	last_job = models.CharField(max_length=6, verbose_name='Ultimo Job', blank=True)
	zone = models.CharField(max_length=40, verbose_name='Zona/Barrio', blank=True)

	def __str__(self):
		return self.niv