from django.db import models
from django.core.urlresolvers import reverse
import csv
from django.http import HttpResponse

class ContarRubro(models.Manager):
    def contar_rubro(self, **keyword):
        rubro = self.get(pk=keyword['pk'])

        #recepcion= rubro.objects.get(pk=recepcion.producto.pk)
        
        rubros_asociados = rubro.recepcion_set.all()
        
        #pagos_asociados= PagoRecepcion.objects.get(recepcion=recepcion)

        #cantidad= rubros_asociados.count()

        #a =p.pagorecepcion_set.all()
        #b = a.total_recepcion_set.all()
        #zonas= a.count()
        #hect= 0
        #for i in a:
		#	hect+= i.hectareas
        return {'RenRecep':rubros_asociados,}

class Rubro(models.Model):
	nombre= models.CharField(max_length=50, unique=True)
	nombre_cientifico= models.CharField(max_length=100, unique=True)
	objects=  models.Manager()
	#variedad = models.CrarField(max_length=4, choices=variedad
	tolerancia_humedad= models.FloatField(default=0)
	diferencia_humedad = models.FloatField(default=0)
	tolerancia_impureza= models.FloatField(default=0)
	null = models.BooleanField(default=False)
	objects = models.Manager()
	cuenta= ContarRubro()
	
	
	foto= models.ImageField(upload_to='imagenes/rubro',blank=True, default='imagenes/icon_miau.gif')
	def codigo_en_sistema(self):
		nominal= 'MR'
		subnominal= str(self.id)
		if self.id < 10:
			subnominal = '0'+ subnominal
		codigo = nominal + '-'+ subnominal
		return codigo

	
	def get_absolute_url(self):
		return reverse('rubro.views.Editar_Rubro', args=[str(self.id)])
	def __unicode__(self):
		return '%s'%(self.nombre)


class VariedadRubro(models.Model):
	rubro= models.ForeignKey(Rubro)
	nombre=models.CharField(max_length=50, unique=True)
	descripcion=models.TextField()
	null = models.BooleanField(default=False)
	def get_absolute_url(self):
		return reverse('rubro.views.Rubro_Variedades_Edit', args=[str(self.rubro.id),str(self.id)])
	def __unicode__(self):
		return '%s - %s'%(self.rubro, self.nombre)

# Topo dentado o duro
class TipoRubro(models.Model):
	rubro=models.ForeignKey(Rubro)
	nombre= models.CharField(max_length=50, unique=True)
	descripcion=models.TextField()
	null = models.BooleanField(default=False)
	

	def get_absolute_url(self):
		return reverse('rubro.views.Rubro_Tipo_Edit', args=[str(self.rubro.id),str(self.id)])
	def __unicode__(self):
		return '%s - %s'%(self.rubro, self.nombre)


#busqueda de relacion para ajustar el precio