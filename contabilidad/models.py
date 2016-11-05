from django.db import models

# Create your models here.
from rubro.models import VariedadRubro,TipoRubro, Rubro
from smart_selects.db_fields import ChainedForeignKey
from django.core.urlresolvers import reverse

# Create your views here.
IMPUESTOS={'IVA':12.0}
import datetime
tiempo= datetime.datetime.now()
class Bancos(models.Model):
	nombre = models.CharField(max_length=100, unique=True)
	descripcion=models.TextField()
	null = models.BooleanField(default=False)

	def __unicode__(self):
		return self.nombre

class TipoCuenta(models.Model):
	nombre= models.CharField(max_length=50, unique=True)
	null = models.BooleanField(default=False)

	def __unicode__(self):
		return self.nombre.title()

#=== ======================ciclo de recepcion========

class Ciclo(models.Model):
	nombre= models.CharField(max_length=50, unique=True)
	fecha_de_inicio=models.DateField()
	fecha_de_cierre=models.DateField(null=True,blank=True )
	habilitado = models.BooleanField(default=True)
	null = models.BooleanField(default=False)

	

	def get_absolute_url(self):
		return reverse('contabilidad.views.Edit_Ciclos', args=[str(self.id)])
	
	def deshabilitar(self):
		ano,mes,dia= tiempo.year,tiempo.mes,tiempo.day
		fecha=datetime.date(ano,mes,dia)
		if self.fecha_de_cierre < self.fecha:
			return False
		else:
			return True
	def codigo_en_sistema(self):
		nominal= 'MCC'
		subnominal= str(self.id)
		if self.id < 10:
			subnominal = '0'+ subnominal
		codigo = nominal + '-'+ subnominal + str(self.fecha_de_inicio.year)
		return codigo
	
	def __unicode__(self):
		return '%s-%s'%(self.nombre, self.codigo_en_sistema())
#==============================Precio de Ciclo===============
class PrecioDeRubroPorCiclo(models.Model):
	
	producto= models.ForeignKey(Rubro)
	#variedad
	#Tipo
	variedad= ChainedForeignKey(VariedadRubro, chained_field='producto', chained_model_field='rubro',show_all= False,auto_choose=True)
	tipo= ChainedForeignKey(TipoRubro, chained_field='producto',chained_model_field='rubro',show_all= False, auto_choose=True)
	ciclo= models.ForeignKey(Ciclo)

	precio_por_Kg=models.FloatField()
	null = models.BooleanField(default=False)
	
	def get_absolute_url(self):
		return reverse('contabilidad.views.Edit_PresioXCiclo', args=[str(self.ciclo.pk), str(self.pk)])

	def __unicode__(self):
		return '%s ciclo %s a %s'% (self.producto, self.ciclo, self.precio_por_Kg)



