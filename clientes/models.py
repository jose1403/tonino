from django.db import models
from contabilidad.models import Bancos, TipoCuenta
tipo_de_cuenta= (('Aho', 'Ahorro'), ('Cor', 'Corriente'))
from django.core.urlresolvers import reverse
# Create your models here.
class Cliente(models.Model):
	#Datos Personales
	nombre_o_razon_social = models.CharField(max_length =100)
	#apellido =models.CharField(max_length=50)
	documentoId= models.CharField(max_length=20, unique=True)
	#informacion de Contactos
	domicilio_fiscal=models.TextField()
	#profecion=models.CharField(max_length=100)
	telefono= models.CharField(max_length=12, blank=True)
	celular= models.CharField(max_length=12, blank=True)
	e_mail= models.EmailField(default='moliven@moliven.com', blank=True)

	referencia_folder= models.CharField(max_length= 50, default='0')
	# Datos bancarios
	cuenta_bancaria= models.CharField(max_length=100, blank=True)
	banco=models.ForeignKey(Bancos)
	tipo_cuenta= models.ForeignKey(TipoCuenta)
	
	fecha_agregado =models.DateTimeField(auto_now=True)
	habilitado = models.BooleanField(default=True)
	observacion=models.TextField(blank=True)
	null = models.BooleanField(default=False)
	


	#zona= models.ForeignKey('Zona')
	#def get_absolute_url(self):
	#	return reverse('nucleo.views.Editar_Productor', args=[str(self.id)])
	def __unicode__(self):
		return '%s %s'%(self.nombre_o_razon_social, self.documentoId)

	def codigo_en_sistema(self):
		nominal= 'MC'
		subnominal= str(self.id)
		if self.id < 10:
			subnominal = '0'+ subnominal
		codigo = nominal + '-'+ subnominal
		return codigo

	#zona= models.ForeignKey('Zona')
	def get_absolute_url(self):
		return reverse('clientes.views.Edit_Cliente', args=[str(self.id)])
	