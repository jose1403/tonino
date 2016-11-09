
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse, Http404
from contabilidad.models import PrecioDeRubroPorCiclo, IMPUESTOS

from .models import Despacho, IngresoDespacho, TotalDespacho,CuentasXcobrarDespacho
from .forms import  FormDespacho, FormTotalDespacho, FormCuentasXcobrarDespacho
from .despacho_pdf import lista_despacho_pdf
import datetime
from gestion.views import get_query, desabilite_model
tiempo= datetime.datetime.now()
fecha=datetime.date(tiempo.year,tiempo.month,tiempo.day)

# Create your views here.
def ValorTotal( cantidad, precio, impuestos):
	total_neto = cantidad * precio
	calculo= []
	total = total_neto
	total_pago= 0
	retorno= {}
	for i, k in impuestos.items():
		total_pago= total_neto
		i = k
		total_pago+= total_neto*(float(k)/100)
		retorno.update({i:k})

	retorno.update({'total_pago':total_pago})

	#for i in impuestos:
	#	cal.append(total_neto*(float(i)/100))
	#	total += total_neto*(float(i)/100)

	return retorno
from django.views.generic.dates import ArchiveIndexView


class Mostrar_Despacho(ArchiveIndexView):
	#model=Despacho
	#context_object_name='form'
	date_field="fecha_salida"
	template_name='despacho/VerDespachos.html'
	paginate_by=25
	make_object_list = True
	allow_empty=True
	allow_future=True
	q=''
	def get(self, request, *args, **kwargs):
		queryset= Despacho.objects.filter(null=False)
		q= ''
		if 'q' in request.GET and request.GET['q'].strip():
			q= request.GET['q']
			query = get_query(q,['pk', 'producto__nombre', 'variedad__nombre',
								'tipo__nombre', 'ciclo_asociado__nombre', 'silo__nombre',
								'cliente__nombre_o_razon_social',
								'dirigido_a', 'cantidad_en_Kg'])
			#return HttpResponse(query)
			queryset = queryset.filter(query)
		
		self.object = queryset
		return super(Mostrar_Despacho, self).get(request, *args, **kwargs)
	def get_context_data(self, **kwargs):
		context = super(Mostrar_Despacho, self).get_context_data(**kwargs)
		context['form'] = self.object
		context['q']= self.q
		return context 
	def get_queryset(self):
		return self.object
	
	def post(self, request, *args, **kwargs):
		if request.POST['lista-pdf'] == 'lista-selected' and request.user.has_perm('auth.empleado'):

			a=request.POST.getlist('seleccion')
			return lista_despacho_pdf(request, a, Despacho.objects.filter(null=False))
	
		else:
			return HttpResponseRedirect('.')

class Mostrar_CuetasXcobrar(ArchiveIndexView):
	model=CuentasXcobrarDespacho
	context_object_name='form'
	date_field="fecha_agregado"
	template_name='despacho/cuentas/VerCuentasPorCobrar.html'
	paginate_by=25
	make_object_list = True
	allow_empty=True
	allow_future=True
	def post(self, request, *args, **kwargs):
		if request.POST['lista-pdf'] == 'lista-selected':

			a=request.POST.getlist('seleccion')
			return lista_recepcion_pdf(request, a, self.model.objects.all())
	
		else:
			return HttpResponseRedirect('.')

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Editar_CuentasXcobrar(request, pk):
	info=''
	print pk
	try:
		int(pk)
	except ValueError:
		raise Http404()
	info = ''
	try:
		model = CuentasXcobrarDespacho.objects.select_related().get(pk=pk, pagado=False)
	except ObjectDoesNotExist:
		return HttpResponseRedirect('/agregado/cuentasxcobrar/ver') 
	if request.method=='POST':
		form = FormCuentasXcobrarDespacho(request.POST, instance=model)
		if form.is_valid():
			deuda= form.cleaned_data['deuda']
			abono= form.cleaned_data['abono']
			saldo_deudor= form.cleaned_data['saldo_deudor']
			fecha_vencimiento= form.cleaned_data['fecha_vencimiento']
			pago=''
			saldo = deuda - abono
			if abono >=deuda:
				print 'funciona'
				pago = True
				pagado = model.despacho.ingreso
				pagado.pagado= True
				pagado.save()
				model.deuda = deuda
				model.abono= abono
				model.saldo_deudor= saldo
				model.fecha_vencimiento = fecha_vencimiento
				model.pagado = pago
				model.save()
				return HttpResponseRedirect('/agregado/cuentasxcobrar/ver')

						
			else:
				pago = False
				model.deuda = deuda
				model.abono= abono
				model.saldo_deudor= saldo
				model.fecha_vencimiento = fecha_vencimiento
				model.pagado = pago
				model.save()
			return HttpResponseRedirect('.')
		else:
			info='POR FAVOR CORRIJA LOS CAMPOS INVALIDOS'
			return render(request, 'despacho/cuentas/EditarCuentaXcobrar.html', {'info':info,
																			'form':form,
																			'model':model})


	else:
		
		form = FormCuentasXcobrarDespacho(instance=model)
		return render(request, 'despacho/cuentas/EditarCuentaXcobrar.html', {'info':info,
																			'form':form,
																			'model':model})
															
@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Ver_Despacho(request):
	form= Despacho.objects.all()
	return render(request,'despacho/VerDespachos.html', {'form':form})

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Add_Despacho(request):
	info=''
	if request.method=='POST':
		form = FormDespacho(request.POST)
		if form.is_valid():
			producto =  form.cleaned_data['producto']
			variedad =  form.cleaned_data['variedad']
			tipo = form.cleaned_data['tipo']
			precio = form.cleaned_data['precio']
			ciclo_asociado=  form.cleaned_data['ciclo_asociado']
			silo=  form.cleaned_data['silo']
			planta=form.cleaned_data['planta']
			fecha_salida=form.cleaned_data['fecha_salida']
			tipo_vehiculo= form.cleaned_data['tipo_vehiculo']
			placa = form.cleaned_data['placa']
			cliente=  form.cleaned_data['cliente']
			dirigido_a=  form.cleaned_data['dirigido_a']
			cantidad_en_Kg=  form.cleaned_data['cantidad_en_Kg']
			humedad=  form.cleaned_data['humedad']
			impuresa=  form.cleaned_data['impureza']
			granos_danados_totales =  form.cleaned_data['granos_danados_totales']
			granos_partidos = form.cleaned_data['granos_partidos']
			temperatura_promedio= form.cleaned_data['temperatura_promedio']
			otros=  form.cleaned_data['otros']
			despachado_por= form.cleaned_data['despachado_por']
			observacion =form.cleaned_data['observacion']
			pagado= True
			if 'pagado' in request.POST.keys():
				pagado=True
			else:
				pagado=False
			pagado= pagado
			model= Despacho()
			model.producto= producto
			model.variedad= variedad
			model.tipo=tipo
			model.ciclo_asociado= ciclo_asociado
			model.planta= planta

			model.silo = silo 
			model.precio= precio
			model.fecha_salida= fecha_salida
			model.tipo_vehiculo= tipo_vehiculo
			model.placa = placa
			model.cliente= cliente
			model.dirigido_a= dirigido_a

			model.cantidad_en_Kg =cantidad_en_Kg
			model.humedad =humedad
			model.impureza =impuresa

			model.granos_danados_totales =granos_danados_totales
			model.granos_partidos= granos_partidos
			model.temperatura_promedio= temperatura_promedio
			model.otros = otros
			model.despachado_por= despachado_por
			model.observacion= observacion

			

			if cantidad_en_Kg > silo.en_inventario:return render(request,'despacho/AddDespachos.html', {'form':form,'info':'la cantidad ingresada supera la cantidad disponible en el silo'.upper()})
			model.save()

			model_pago= IngresoDespacho()
			model_pago.despacho= model
			model_pago.precio= precio
			model_pago.pagado= pagado
			model_pago.save()
			
			# ajustar de acuerdo al pago generado
			valorespago = ValorTotal(model.cantidad_en_Kg, model_pago.precio, IMPUESTOS)
			model_total = TotalDespacho()
			model_total.ingreso= model_pago
			model_total.total_neto= model.cantidad_en_Kg * float(precio)
			model_total.total_Bs= valorespago['total_pago']

			model_total.save()
			if pagado == False:
				CXP = CuentasXcobrarDespacho()
				CXP.despacho = model_total
				CXP.deuda= valorespago['total_pago']
				CXP.saldo_deudor= valorespago['total_pago']
				CXP.fecha_vencimiento= datetime.date(fecha.year,fecha.month,fecha.day )

				CXP.save()
			else:
				pass
			
			silo.en_inventario -= cantidad_en_Kg
			silo.resto += cantidad_en_Kg
			silo.save() 
			
			
			return HttpResponseRedirect('/agregado/despacho/ver/')

	else: 
		form= FormDespacho()
	return render(request, 'despacho/AddDespachos.html', {'form':form})


@permission_required('auth.acceso_analista',login_url="/accounts/login/")
def Ver_Factura_Despacho(request, pk):
	try:
		int(pk)
	except ValueError:
		raise Http404()
	info =""

	despacho= Despacho.objects.get(pk= pk)
	pago = IngresoDespacho.objects.get(despacho= despacho)
	total_pago= TotalDespacho.objects.get(ingreso=pago)
	#for i,k in IMPUESTOS.items():


	#IVA= total_pago.total_neto * (12.0/100)
	#TRASPORTE = total_pago.total_neto *(1.8/100) 

	return render(request,'despacho/factura_despacho.html', { 'despacho':despacho,
																'pago': pago,
																'total_pago':total_pago,
																'impuestos':IMPUESTOS,})

@permission_required('auth.acceso_analista',login_url="/accounts/login/")
def Edit_Despacho(request, pk):
	info=''
	print pk
	try:
		int(pk)
	except ValueError:
		raise Http404()
	info =""
	model = Despacho.objects.get(pk=pk)
	model_pago= IngresoDespacho.objects.get(despacho=model)
	model_total = TotalDespacho.objects.get(ingreso=model_pago)

	if request.method=='POST':
	
		if 'eliminar' in request.POST.keys() and  request.POST['eliminar']== 'delete-selected' and request.user.has_perm('auth.empleado'):
			
			model.delete()
			return HttpResponseRedirect(raiz)

	
		form = FormDespacho(request.POST, instance=model)
		if form.is_valid():
			producto =  form.cleaned_data['producto']
			variedad =  form.cleaned_data['variedad']
			tipo = form.cleaned_data['tipo']
			precio = form.cleaned_data['precio']
			ciclo_asociado=  form.cleaned_data['ciclo_asociado']
			fecha_salida=form.cleaned_data['fecha_salida']
			tipo_vehiculo= form.cleaned_data['tipo_vehiculo']
			placa = form.cleaned_data['placa']
			cliente=  form.cleaned_data['cliente']
			dirigido_a=  form.cleaned_data['dirigido_a']
			cantidad_en_Kg=  form.cleaned_data['cantidad_en_Kg']
			humedad=  form.cleaned_data['humedad']
			impuresa=  form.cleaned_data['impureza']
			granos_danados_totales =  form.cleaned_data['granos_danados_totales']
			granos_partidos = form.cleaned_data['granos_partidos']
			temperatura_promedio= form.cleaned_data['temperatura_promedio']
			otros=  form.cleaned_data['otros']
			despachado_por= form.cleaned_data['despachado_por']
			observacion =form.cleaned_data['observacion']
			model.producto= producto
			model.variedad= variedad
			model.tipo=tipo
			model.ciclo_asociado= ciclo_asociado
			model.precio= precio
			model.fecha_salida= fecha_salida
			model.tipo_vehiculo= tipo_vehiculo
			model.placa = placa
			model.cliente= cliente
			model.dirigido_a= dirigido_a

			model.cantidad_en_Kg =cantidad_en_Kg
			model.humedad =humedad
			model.impureza =impuresa

			model.granos_danados_totales =granos_danados_totales
			model.granos_partidos= granos_partidos
			model.temperatura_promedio= temperatura_promedio
			model.otros = otros
			model.despachado_por= despachado_por
			model.observacion= observacion
			model.save()


			model_pago.precio= precio
			model_pago.save()
			valorespago = ValorTotal(model.cantidad_en_Kg, model_pago.precio, IMPUESTOS)
			# ajustar de acuerdo al pago generado
			model_total.total_neto= model.cantidad_en_Kg * float(precio)
			model_total.total_Bs= valorespago['total_pago']
			model_total.save()
			if model_pago.pagado == False:
				CXP = CuentasXcobrarDespacho.objects.get(despacho=model_total)
				CXP.deuda= valorespago['total_pago']
				CXP.saldo_deudor= valorespago['total_pago'] - CXP.abono
				CXP.save()
			else:
				pass
			info = 'se ha editado Satisfactoriamente'
			return render(request, 'despacho/EditDespacho.html', {'form':form,
															'model':model,
															'model_pago':model_pago,
															'model_total':model_total,
															'info':info})

	else:

		form= FormDespacho(instance=model)
	return render(request, 'despacho/EditDespacho.html', {'form':form,
															'model':model,
															'model_pago':model_pago,
															'model_total':model_total,
															'info':info})


@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Ver_Ingreso_Despacho(request):
	form= IngresoDespacho.objects.all()
	return render(request, 'despacho/VerIngresoDespacho.html')


@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Add_Total_Despacho(request):
	form= FormTotalRecepcion()
	return render(request, 'despacho/AddTotalDespacho.html', {'form':form})
