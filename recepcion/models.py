from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from rubro.models import VariedadRubro, Rubro, TipoRubro
from contabilidad.models import Ciclo, PrecioDeRubroPorCiclo, IMPUESTOS
from proovedores.models import Productor, ZonaProductor
from plantas.models import Silos, Plantas
from django.core.urlresolvers import reverse
pagos=(('Pagado', 'Pagado'),('Deuda', 'Deuda'))
# Create your models here.

class ContarRubro(models.Manager):
    def contar_rubro(self, **keyword):
        recepcion = self.get(pk=keyword['pk'])
        pagos = TotalRecepcion.objects.filter(ingreso__recepcion__producto__pk=recepcion.producto.pk)
        rubro= Rubro.objects.get(pk=recepcion.producto.pk)
        
        rubros_asociados = rubro.recepcion_set.all()
        pagos_asociados= PagoRecepcion.objects.get(recepcion=recepcion)
        
        cantidad= rubros_asociados.count()

        #a =p.pagorecepcion_set.all()
        #b = a.total_recepcion_set.all()
        #zonas= a.count()
        #hect= 0
        #for i in a:
		#	hect+= i.hectareas
        return {'pago':pagos,'RenRecep':cantidad, 'productos':rubros_asociados, 'pagos':pagos_asociados}
        #return {'zonas':a}#, 'CantZonas':zonas, 'CantHectareas': hect}



class Recepcion(models.Model):
	#datos del producto
	producto = models.ForeignKey(Rubro)
	variedad=ChainedForeignKey(VariedadRubro, chained_field='producto',chained_model_field='rubro',show_all= False,auto_choose=True)
	tipo = ChainedForeignKey(TipoRubro, chained_field='producto',chained_model_field='rubro',show_all= False,auto_choose=True)
	ciclo_asociado=models.ForeignKey(Ciclo)#.objects.filter(habilitado=True))
	planta= models.ForeignKey(Plantas, null=True)
	silo = ChainedForeignKey(Silos,null=True, chained_field='planta',chained_model_field='plantas',show_all= False, auto_choose=True)
	#datos de entrega
	fecha_llegada = models.DateTimeField()
	tipo_vehiculo = models.CharField(max_length=100)
	placa= models.CharField(max_length=50)
	#datos del productor
	proovedor= models.ForeignKey(Productor)
	zona_de_cosecha=ChainedForeignKey(ZonaProductor, chained_field='proovedor',chained_model_field='productor', show_all= False, auto_choose=True)
	#Orden_TEsa
	numero_romana= models.CharField(max_length=20, default=0)
	referencia_folder= models.CharField(max_length=20, default=0)
	cantidad_en_Kg=models.FloatField()
	humedad = models.FloatField()
	impureza= models.FloatField()
	granos_danados_totales = models.FloatField()
	granos_partidos= models.FloatField()
	temperatura_promedio = models.FloatField()
	otros= models.FloatField()
	recibido_por = models.CharField(max_length=100)
	fecha_agregado = models.DateTimeField(auto_now=True)
	objects = models.Manager()
	cuenta= ContarRubro()
	observacion= models.TextField(default='Recepcion Satisfactoria')
	null = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse('recepcion.views.Ver_Factura_Recepcion', args=[str(self.id)])
	def __unicode__(self):
		return 'N %s --%s - cilo %s -  %s'%(self.pk,self.producto, self.ciclo_asociado, self.proovedor )

	def codigo_en_sistema(self):
		nominal= 'MR'
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
	def producto_total(self):
		cadena='%s(%s-%s)' %(self.producto.nombre, self.variedad.nombre,self.tipo.nombre)
		return cadena.upper()
#Contabilidad  de recepcion


pagos=(('Pagado', 'Pagado'),('Deuda', 'Deuda'))
class PagoRecepcion(models.Model):

	recepcion=models.OneToOneField(Recepcion)
	precio = models.ForeignKey(PrecioDeRubroPorCiclo)
	#impuestos =models.ManyToManyField(Impuesto)
	p = models.BooleanField()
	null = models.BooleanField(default=False)

	#def get_absolute_url(self):yo no soy yo soy alan from misisipi
	#	return reverse('nucleo.views.Editar_Pago_Recepcion', args=[str(self.id)])

	def __unicode__(self):
		return '%s %s a %s Bs.'%(self.recepcion.codigo_en_sistema(),self.recepcion.producto_total(), self.precio.precio_por_Kg)



class CantidadIngresadaRubro(models.Manager):
    def contar_rubros(self, **keyword):

        recepcion = self.filter(ingreso__recepcion__producto__pk=keyword['pk'])
       	cantidad_total= 0
       	dinero_invertido= 0
       	for rubro in recepcion:
       		cantidad_total += rubro.cantidad_real
       	for rubro in recepcion:
       		dinero_invertido += rubro.total_Bs 

       	pro= []
       	num_proovedores= 0
       	listado=[['proovedores', cantidad_total]]
       	for proovedor in recepcion:
       		proovedores= proovedor.ingreso.recepcion.proovedor
       		pro.append(proovedores)
       		num_proovedores+=1

       		print num_proovedores
       		a=0
       		while a <num_proovedores:
       			a+=1
       			print 'lista: %s'%listado
  		        for i in listado:
  		        	print 'listado: %s' %i
		       		if proovedores not in i:
		       			print i
		       			print '*'*50
		       			print 'provedores: %s'%proovedores
		       			j= proovedores.recepcion_set.all()
		        		b = j.filter(producto__pk=keyword['pk'])
		        		cont=0
		        		for c in b:
		        			cont +=c.cantidad_en_Kg
		        		listado.append([proovedores, cont])


        #a =p.pagorecepcion_set.all()
        #b = a.total_recepcion_set.all()
        #zonas= a.count()
        #hect= 0
        #for i in a:
		#	hect+= i.hectareas
        return {'Resepcion':recepcion, 'cantidad_total':cantidad_total,
        		'dinero_invertido': dinero_invertido, 'proovedores':pro,'listado': listado}
    
    def contar_clientes(self, **keyword):

        recepcion = self.filter(ingreso__recepcion__cliente__pk=keyword['pk'])
        cantidad_total=0
        rubros_almascenado=0
        total_envios=0
        numero_de_clientes= recepcion.count()





class TotalRecepcion(models.Model):
	ingreso=models.OneToOneField(PagoRecepcion)
	descuentoH= models.FloatField(default=0)
	descuentoI= models.FloatField(default=1)
	descuentoM= models.FloatField(default=0.25)
	descuentoTotal= models.FloatField(default=0)
	cantidad_descuento= models.FloatField(default=0)
	cantidad_real = models.FloatField(default=0)
	total_neto=models.FloatField(default=0.0)
	total_Bs=models.FloatField()
	objects = models.Manager()
	cuenta= CantidadIngresadaRubro()
	null = models.BooleanField(default=False)


	def __unicode__(self):
		return '%s %s'%(self.ingreso.recepcion.codigo_en_sistema(),self.ingreso.recepcion.producto_total())
	def impuestos(self):
		var = self.total_neto
		dicc={}
		for i, k in IMPUESTOS.items():
			v = var*(k/100)
			print 'pago: %s%%'%v
			dicc.update({'%s %s%%'%(i,k):v})
		return dicc


class CuentasXpagarRecepcion(models.Model):
	recepcion= models.OneToOneField(TotalRecepcion)
	deuda = models.FloatField()
	abono= models.FloatField(default=0)
	saldo_deudor= models.FloatField()
	pagado = models.BooleanField(default=False)
	fecha_agregado= models.DateField(auto_now_add=True)
	fecha_vencimiento = models.DateField()
	null = models.BooleanField(default=False)
	

	def __unicode__(self):
		return str(self.recepcion)

	def get_absolute_url(self):
		return reverse('recepcion.views.Editar_CuentasXpagar', args=[str(self.id)])