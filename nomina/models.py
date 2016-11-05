from django.db import models
from django.core.urlresolvers import reverse
GENERO=(('M', 'Hombre'),('F', 'Mujer'))
# Create your models here.


class Puesto(models.Model):
	nombre= models.CharField(max_length=100)
	descripcion= models.TextField()
	null=models.BooleanField(default=False)

	def __unicode__(self):
		return self.nombre
	def get_absolute_url(self):
		return reverse('edit-puestos', kwargs={'pk':self.pk})

class FechaPagosAsignados(models.Model):
	fecha_inicio=models.DateField()
	fecha_cierre=models.DateField()
	semana= models.IntegerField(default=0)
	null=models.BooleanField(default=False)

	def __unicode__(self):
		return '%s-%s'%(self.fecha_inicio, self.fecha_cierre)
	def get_absolute_url(self):
		return reverse('edit-fechas-asignadas', kwargs={'pk':self.pk})

class Empleado(models.Model):
	nombre= models.CharField(max_length=50)
	apellido=models.CharField(max_length=50)
	documentoID= models.CharField(max_length=50, unique=False)
	fecha_de_nacimiento=models.DateField()
	domicilio= models.TextField()
	genero = models.CharField(max_length=1, choices=GENERO)
	fecha_ingreso=models.DateField()
	contrato= models.CharField(max_length=50)
	referecia_contrato= models.CharField(max_length=50)
	puesto = models.ForeignKey(Puesto)
	sueldo_mensual = models.FloatField()
	habilitado= models.BooleanField(default=True)
	null=models.BooleanField(default=False)

	def __unicode__(self):
		return '%s %s'% (self.nombre, self.apellido)
	def get_absolute_url(self):
		return reverse('edit-empleado', kwargs={'pk':self.pk}) 
class Obrero(models.Model):
	nombre= models.CharField(max_length=50)
	apellido=models.CharField(max_length=50)
	documentoID= models.CharField(max_length=50)
	fecha_de_nacimiento=models.DateField()
	domicilio= models.TextField()
	genero = models.CharField(max_length=1, choices=GENERO)
	fecha_ingreso=models.DateField()
	referencia_folder=models.CharField(max_length=30)
	contrato= models.CharField(max_length=50)
	referecia_contrato= models.CharField(max_length=50)
	puesto = models.ForeignKey(Puesto)
	sueldo_mensual = models.FloatField()
	habilitado= models.BooleanField(default=True)
	null=models.BooleanField(default=False)

	def __unicode__(self):
		return '%s %s'% (self.nombre, self.apellido)

	def get_absolute_url(self):
		return reverse('edit-obrero', kwargs={'pk':self.pk})

class CobroSemanalObrero(models.Model):
	fecha = models.ForeignKey(FechaPagosAsignados)
	obrero= models.ForeignKey(Obrero)
	sueldo_diario=models.FloatField()
	dias_trabajados=models.IntegerField()
	bono_nocturno= models.FloatField()
	total_asignacion=models.FloatField()
	descuento_ivss=models.FloatField(default=0)
	descuento_faov=models.FloatField(default=0)

	total_deducciones=models.FloatField()
	total_a_cobrar=models.FloatField()
	generado=models.DateTimeField(auto_now=True)
	null=models.BooleanField(default=False)

	def __unicode__(self):
		return '%s (%s)'% (self.obrero, self.fecha)
	def get_absolute_url(self):
		return reverse('edit-pagos-semanales-obreros', kwargs={'pk':self.pk})

class BonoDeAlimentacionSemanalObreros(models.Model):
	fecha = models.ForeignKey(FechaPagosAsignados)
	obreros=models.ManyToManyField(Obrero)
	bono_mensual= models.FloatField()
	bono_diario=models.FloatField()
	dias_trabajados=models.IntegerField()
	total_a_cobrar= models.FloatField()
	
	null=models.BooleanField(default=False)

	def __unicode__(self):
		return 'Bonos del %s'% (self.fecha)
	def get_absolute_url(self):
		return reverse('edit-bono-alimentacion-obrero', kwargs={'pk':self.pk})
"""class BonoDeAlimentacionMensualObreros(models.Model):
	fecha=models.DateField()
	obreros=models.ManyToManyField(Obreros)
	bono_mensual= models.FloatField(max_digit=2)
	bono_diario=models.FloatField(max_digit=2)
	dias_trabajados=models.IntegerField()
	total_a_cobrar= models.FloatField(max_digit=2)"""

class BonoDeAlimentacionSemanalEmpleados(models.Model):
	fecha = models.OneToOneField(FechaPagosAsignados)
	empleados=models.ManyToManyField(Empleado)
	bono_mensual= models.FloatField()
	bono_diario=models.FloatField()
	dias_trabajados=models.IntegerField()
	total_a_cobrar= models.FloatField()
	null=models.BooleanField(default=False)

	def __unicode__(self):
		return 'Bonos del %s'% (self.fecha)

	def get_absolute_url(self):
		return reverse('edit-bono-alimentacion-empleado', kwargs={'pk':self.pk})


c="""lass BonoDeAlimentacionMensualEmpleados(models.Model):
	fecha=models.DateField()
	obreros=models.ManyToManyField(Obreros)
	bono_mensual= models.FloatField(max_digit=2)
	bono_diario=models.FloatField(max_digit=2)
	dias_trabajados=models.IntegerField()
	total_a_cobrar= models.FloatField(max_digit=2)"""

	#	BONO ALIMENTACION MENSUAL 	DIARIO	DIAS TRABAJADOS 	TOTAL A COBRAR 	DIAS TRABAJADOS 		DIARIO	TOTAL SEMANAL




class CobroSemanalEmpleado(models.Model):
	fecha = models.ForeignKey(FechaPagosAsignados)
	empleado= models.ForeignKey(Empleado)
	sueldo_diario=models.FloatField()
	dias_trabajados=models.IntegerField()
	bono_nocturno= models.FloatField()
	total_asignacion=models.FloatField()

	descuento_ivss=models.FloatField(default=0)
	descuento_faov=models.FloatField(default=0)
	total_deducciones=models.FloatField()
	total_a_cobrar=models.FloatField()
	null=models.BooleanField(default=False)

	def __unicode__(self):
		return ' %s (%s)'% (self.empleado, self.fecha)
	def get_absolute_url(self):
		return reverse('edit-pagos-semanales-empleados', kwargs={'pk':self.pk})


class NominaTotalObreros(models.Model):
	obreros = models.ManyToManyField(CobroSemanalObrero)
	fecha = models.OneToOneField(FechaPagosAsignados)
	total_obreros= models.IntegerField()
	total_nomina =  models.FloatField()
	fecha_generado=models.DateField()

	null=models.BooleanField(default=False)

	def __unicode__(self):
		return 'Nomina del %s'% (self.fecha)

class NominaTotalEmpleados(models.Model):
	empleados = models.ManyToManyField(CobroSemanalEmpleado)
	fecha = models.OneToOneField(FechaPagosAsignados)
	total_empleados= models.IntegerField()
	total_nomina =  models.FloatField()
	fecha_generado=models.DateField(auto_now=True)
	null=models.BooleanField(default=False)

	def __unicode__(self):
		return 'Nomina del %s'% (self.fecha)




#. IVSS 	DESC. FAOV	TOTAL  DEDUCCIONES 	TOTAL A COBRAR 
