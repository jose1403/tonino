from django.db import models
from django.core.urlresolvers import reverse
from rubro.models import Rubro, VariedadRubro,TipoRubro
from smart_selects.db_fields import ChainedForeignKey
from plantas.models import Silos, Plantas
from contabilidad.models import Ciclo, PrecioDeRubroPorCiclo, IMPUESTOS
from clientes.models import Cliente

pagos=(('Pagado', 'Pagado'),('Deuda', 'Deuda'))

# Create your models here.
class Despacho(models.Model):
	#datos del producto
	#=================================================
	producto = models.ForeignKey(Rubro)

	variedad=ChainedForeignKey(VariedadRubro, chained_field='producto',
											  chained_model_field='rubro',
											  show_all= False,
											  auto_choose=True)

	tipo = ChainedForeignKey(TipoRubro, chained_field='producto',
											  chained_model_field='rubro',
											  show_all= False,
											  auto_choose=True)

	ciclo_asociado=models.ForeignKey(Ciclo)
	planta= models.ForeignKey(Plantas, null=True)
	silo = ChainedForeignKey(Silos,null=True, chained_field='planta',chained_model_field='plantas',show_all= False, auto_choose=True)
	precio = models.FloatField()

	#datos de entrega
	fecha_salida = models.DateTimeField()
	tipo_vehiculo = models.CharField(max_length=100)
	placa= models.CharField(max_length=50)
	#datos del productor
	cliente= models.ForeignKey(Cliente)
	dirigido_a= models.CharField(max_length=300)
	#Orden_TEsa

	referencia_folder= models.CharField(max_length=20, default=0)
	#estado del rubro

	cantidad_en_Kg=models.FloatField()

	humedad = models.FloatField()
	impureza= models.FloatField()
	granos_danados_totales = models.FloatField()
	granos_partidos= models.FloatField()
	temperatura_promedio = models.FloatField()
	otros= models.FloatField()

	despachado_por = models.CharField(max_length=100)
	fecha_agregado = models.DateTimeField(auto_now=True)
	observacion= models.TextField()
	null = models.BooleanField(default=False)


	def get_absolute_url(self):
		return reverse('despacho.views.Ver_Factura_Despacho', args=[str(self.id)])
	
	def codigo_en_sistema(self):
		nominal= 'MD'
		subnominal= ''
		num= 5
		id_num= str(self.id)
		if len(id_num)< num:
			ceros= '0'*(num-len(id_num))
			subnominal= '%s%s'%(ceros, id_num)
		else:
			subnominal= '%s'%(id_num)
		codigo = nominal + '-'+ subnominal
		return codigo
	def __unicode__(self):
		return '%s - %s'%(self.codigo_en_sistema(), self.cliente)
	def producto_total(self):
		cadena='%s(%s-%s)' %(self.producto.nombre, self.variedad.nombre,self.tipo.nombre)
		return cadena
	def fecha_emision(self):
		cadena = '%s/%s/%s - %s:%s' % (self.fecha_agregado.year, self.fecha_agregado.month, self.fecha_agregado.day, self.fecha_agregado.hour, self.fecha_agregado.minute)
		return cadena
class IngresoDespacho(models.Model):
	
	despacho=models.OneToOneField(Despacho)
	precio = models.FloatField()
	#total_impuestos =models.CharField(Impuesto)
	pagado = models.BooleanField(default=False)
	null = models.BooleanField(default=False)

	#def get_absolute_url(self):
	#	return reverse('nucleo.views.Editar_Ingreso_Despacho', args=[str(self.id)])
	def __unicode__(self):
		return '%s %s a %s Bs.'%(self.despacho.codigo_en_sistema(),self.despacho.producto_total(), self.precio)

	
class TotalDespacho(models.Model):
	ingreso=models.OneToOneField(IngresoDespacho)
	total_neto= models.FloatField()
	total_Bs= models.FloatField()
	null = models.BooleanField(default=False)

	
	def __unicode__(self):
		return '%s %s'%(self.ingreso.despacho.codigo_en_sistema(),self.ingreso.despacho.producto_total())
	def impuestos(self):
		var = self.total_neto
		dicc={}
		for i, k in IMPUESTOS.items():
			v = var*(k/100)
			print 'pago: %s%%'%v
			dicc.update({'%s %s%%'%(i,k):v})
		return dicc
#Contabilidad  de recepcion
class CuentasXcobrarDespacho(models.Model):
	despacho= models.OneToOneField(TotalDespacho)
	deuda = models.FloatField()
	abono= models.FloatField(default=0)
	saldo_deudor= models.FloatField()
	pagado = models.BooleanField(default=False)
	fecha_agregado= models.DateField(auto_now_add=True)
	fecha_vencimiento = models.DateField()
	null = models.BooleanField(default=False)
	
	def __unicode__(self):
		return str(self.despacho)
	def get_absolute_url(self):
		return reverse('despacho.views.Editar_CuentasXcobrar', args=[str(self.id)])