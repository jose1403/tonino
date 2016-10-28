from django.db import models
from contabilidad.models import Bancos, TipoCuenta
estado=(('Por', 'Portuguesa'),
	    ('Bar', 'Barinas'),
	    ('Coj', 'Cojedes'),
	    ('Gua', 'Guarico'))

tipo_de_cuenta= (('Aho', 'Ahorro'), ('Cor', 'Corriente'))

# Create your models here.
from django.core.urlresolvers import reverse

 
class ContarZonas(models.Manager):
	def cantidad_almacenada(self, **keyword):
		p= self.get(pk=keyword['pk']) 
		r = p.recepcion_set.all()
		a = r.filter(producto__nombre= keyword['nombre'])

		cont=0
		for i in a:
			cont+= i.cantidad_en_Kg

		cantidad=cont
		return {'cantidad':cantidad}
	def contar_zonas(self, **keyword):
		p= self.get(pk=keyword['pk']) 
		a =p.zonaproductor_set.all()
		zonas= a.count()
		hect= 0
		for i in a:

			hect+= i.hectareas

		return {'zonas':a, 'CantZonas':zonas, 'CantHectareas': hect}
        	




class Productor(models.Model):
	#Datos Personales
	nombre_o_razon_social = models.CharField(max_length =100)
	documentoId= models.CharField(max_length=20, unique=True)

	#informacion de Contactos
	domicilio_fiscal=models.TextField()
	#fecha_de_nacimiento= models.DateField()
	#profecion=models.CharField(max_length=100)
	telefono= models.CharField(max_length=12, blank=True)
	celular= models.CharField(max_length=12, blank=True)

	#Datos Fisicos
	referencia_folder= models.CharField(max_length= 50, default='0')
	# Datos bancarios
	cuenta_bancaria= models.CharField(max_length=100, blank=True)
	banco=models.ForeignKey(Bancos)
	tipo_cuenta= models.ForeignKey(TipoCuenta)
	
	objects = models.Manager()
	zona= ContarZonas()
	fecha_agregado =models.DateTimeField(auto_now=True)
	habilitado = models.BooleanField(default=True)
	observacion=models.TextField(blank=True)
	null = models.BooleanField(default=False)

	def codigo_en_sistema(self):
		nominal= 'MP'
		subnominal= str(self.id)
		if self.id < 10:
			subnominal = '0'+ subnominal
		codigo = nominal + '-'+ subnominal
		return codigo
	def get_absolute_url(self):
		return reverse('proovedores.views.Rubro_Productor_Edit', args=[str(self.id)])
	def __unicode__(self):
		return '%s %s'%(self.nombre_o_razon_social, self.documentoId)



class ZonaProductor(models.Model):
	estado =models.CharField(max_length=3, choices=estado, default=estado[0][0])
	municipio= models.CharField(max_length=50)
	productor =models.ForeignKey(Productor)
	zona= models.CharField(max_length=50, unique=True)
	hectareas= models.FloatField()
	null = models.BooleanField(default=False)
	
	def get_absolute_url(self):
		return reverse('proovedores.views.Edit_Zona_Productor', args=[str(self.productor.id),str(self.id)])
	def __unicode__(self):
		return'%s' %(self.zona)