#-*- encoding: utf-8 -*-
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse, Http404

from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from io import BytesIO

from .models import Recepcion, PagoRecepcion, TotalRecepcion,CuentasXpagarRecepcion
from .forms import FormRecepcion, FormTotalRecepcion, FormCuentasXpagarRecepcion,  FormRecepcionesEdit
from django.core.exceptions import ObjectDoesNotExist 

from nucleo.models import DATOS_DE_LA_EMPRESA
from contabilidad.models import PrecioDeRubroPorCiclo, IMPUESTOS
from .recepcion_pdf import lista_recepcion_pdf
import datetime
from django.db.models import Q
from gestion.views import delete_model, paginacion, get_query, desabilite_model
tiempo= datetime.datetime.now()
fecha=datetime.date(tiempo.year,tiempo.month,tiempo.day)

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def generar_pdf(request,pk):
    print "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    p= Recepcion.objects.get(pk=pk)
    empresa= DATOS_DE_LA_EMPRESA.objects.get(pk=1)
    pdf_name = "recepcion_generada%s.pdf"% p.pk  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,


                            )
    """ 
    DATOS DEL PROOVEDOR:
    NOMBRE O RAZON SOCIAL: {{recepcion.productor. 
    RIf : {{recepcion.productor.docum
    
    RECEPCION:"""
    cuerpo_recepcion = []
    styles = getSampleStyleSheet()
    header = Paragraph("Recepcion N° 0000%s"% p.pk, styles['Heading1'])
    encabesado = Paragraph("SENIAT \n %s \n RIF: %s \n %s \n TELEFONOS: %s/%s \n ZONA_POSTAL: %s"%(empresa.NOMBRE, empresa.RIF, empresa.DIRECCION, empresa.TELEFONO,empresa.CELULAR, empresa.CODIGO_POSTAL),styles['Heading1'])
    print encabesado
    cuerpo_recepcion.append(header)
    cuerpo_recepcion.append(encabesado)

    headings = ('Rubro','Variedad','Ciclo','Cantidad','Zona','Precio/kg','Precio Neto')
    tabla_rec = [(p.producto.nombre, p.variedad.nombre, p.ciclo_asociado.nombre, p.cantidad_en_Kg, 'La Toma', 12, 12.0*p.cantidad_en_Kg  )]

    t = Table([headings] + tabla_rec)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))
    cuerpo_recepcion.append(t)
    doc.build(cuerpo_recepcion)
    response.write(buff.getvalue())
    buff.close()
    return response

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

	retorno.update({'total_pago':total_pago, 'total_neto':total_neto})

	#for i in impuestos:
	#	cal.append(total_neto*(float(i)/100))
	#	total += total_neto*(float(i)/100)

	return retorno

def mermas(cantidad, HI, HF, Ii, If):
	mermahumedad= 0
	mermainpureza=0
	mermamanipuleo= 0
	MI= MermaPorImpuresa(cantidad, Ii, If)
	MIT= cantidad - MI['cantidadI']
	MH = MermaPorHumedad(MIT, HI, HF)
	MHT= MIT-MH['cantidadH']
	MP= MermaPorManipuleo(MHT)
	MPT = MHT - MP['cantidadM']

	cantidad_descuento= MI['cantidadI']+MH['cantidadH']+MP['cantidadM']
	merma_total=cantidad_descuento/float(cantidad)*100
	"""C= Cantidad M= Merma P= manipuleo"""
	dicc= {'CMI':MIT,'MI': MI['mermaI'], 'CI': MI['cantidadI'],
			'CMH': MHT,'MH':MH['mermaH'], 'CH':MH['cantidadH'],
			'CMP': MPT,'MP':MP['mermaM'], 'CP': MP['cantidadM'],
			'CantidadDescuento':cantidad_descuento, 'MermaTotal':merma_total }
	
	return dicc
def MermaPorImpuresa(cantidad, Iinicial, Ifinal):
	mermaI = {}
	formula= 'In-If/100-IF'
	Iinicial= float(Iinicial)
	Ifinal= float(Ifinal)
	merma = round(((Iinicial-Ifinal)/(100-Ifinal))*100, 2)
	cantidadMerma= round(cantidad * (merma/100),2)
	mermaI.update({'mermaI': merma, 'cantidadI':cantidadMerma})
	return mermaI


def MermaPorHumedad(cantidad, HI, HF):
	mermaH={}
	VHF= float(HF)-1  
	HI= float(HI)
	formula = 'M= (HI-HF)/(100-HF)*100'
	merma = round(((HI-HF)/(100-HF))*100, 2)
	cantidadMerma= round(cantidad* (merma/100))
	mermaH.update({'mermaH':merma, 'cantidadH': cantidadMerma})
	return mermaH

def MermaPorManipuleo(cantidad, manipuleo=0.25):
	mermaM= {}
	formula ='cantidad * manipuleo/100 '
	merma= manipuleo
	cantidadMerma= round(cantidad * (manipuleo/100))
	mermaM.update({'mermaM':merma, 'cantidadM':cantidadMerma})
	return mermaM

from django.views.generic.dates import ArchiveIndexView  
 

class Mostrar_Recepcion(ArchiveIndexView):
	#model=Recepcion
	##context_object_name='form'
	date_field="fecha_llegada"
	template_name='recepcion/VerRecepcion.html'
	paginate_by=25
	make_object_list = True
	allow_empty=True
	allow_future=True
	q=''
	def get(self, request, *args, **kwargs):
		queryset= Recepcion.objects.filter(null=False)
		q= ''
		if 'q' in request.GET and request.GET['q'].strip():
			q= request.GET['q']
			query = get_query(q,['pk', 'producto__nombre', 'variedad__nombre',
								'tipo__nombre', 'ciclo_asociado__nombre', 'silo__nombre',
								'proovedor__nombre_o_razon_social',
								'zona_de_cosecha__zona', 'cantidad_en_Kg'])
			#return HttpResponse(query)
			queryset = queryset.filter(query)
		
		self.object = queryset
		return super(Mostrar_Recepcion, self).get(request, *args, **kwargs)
	def get_context_data(self, **kwargs):
		context = super(Mostrar_Recepcion, self).get_context_data(**kwargs)
		context['form'] = self.object
		context['q']= self.q
		context['date_field']='fecha_llegada'
		return context 
	def get_queryset(self):
		print self.object
		return self.object
	
	def post(self, request, *args, **kwargs):
		if request.POST['lista-pdf'] == 'lista-selected':

			a=request.POST.getlist('seleccion')
			return lista_recepcion_pdf(request, a, Recepcion.objects.filter(null=False))
	
		else:
			return HttpResponseRedirect('.')
 

class Mostrar_CuetasXpagar(ArchiveIndexView):
	#model=CuentasXpagarRecepcion
	#context_object_name='form'
	date_field="fecha_agregado"
	template_name='recepcion/cuentas/VerCuentasPorPagar.html'
	paginate_by=25
	make_object_list = True
	allow_empty=True
	allow_future=True
	q=""
	def get(self, request, *args, **kwargs):
		queryset= CuentasXpagarRecepcion.objects.filter(null=False)
		q= ''
		if 'q' in request.GET and request.GET['q'].strip():
			q= request.GET['q']
			query = get_query(q,['pk', 'fecha_agregado', 'fecha_vencimiento','recepcion__ingreso__recepcion__producto__nombre', 'recepcion__ingreso__recepcion__ciclo_asociado__nombre',
								'recepcion__ingreso__recepcion__proovedor__nombre_o_razon_social','recepcion__ingreso__recepcion__proovedor__documentoId',

								'recepcion__ingreso__recepcion__zona_de_cosecha__zona', 'recepcion__total_neto'])
			#return HttpResponse(query)
			queryset = queryset.filter(query)
		self.object = queryset
		return super(Mostrar_CuetasXpagar, self).get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(Mostrar_CuetasXpagar, self).get_context_data(**kwargs)
		context['form'] = self.object
		context['q']= self.q
		return context 
	def get_queryset(self):
		return self.object
	def post(self, request, *args, **kwargs):
		if request.POST['lista-pdf'] == 'lista-selected':

			a=request.POST.getlist('seleccion')
			return lista_recepcion_pdf(request, a, self.model.objects.all())
	
		else:
			return HttpResponseRedirect('.')

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Editar_CuentasXpagar(request, pk):
	info=''
	print pk
	try:
		int(pk)
	except ValueError:
		raise Http404()
	info = ''
	try:
		model = CuentasXpagarRecepcion.objects.select_related().get(pk=pk, pagado=False)
	except ObjectDoesNotExist:
		return HttpResponseRedirect('/agregado/cuentas/ver') 
	if request.method=='POST':
		form = FormCuentasXpagarRecepcion(request.POST, instance=model)
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
				pagado = model.recepcion.ingreso
				pagado.p= True
				pagado.save()
				model.deuda = deuda
				model.abono= abono
				model.saldo_deudor= saldo
				model.fecha_vencimiento = fecha_vencimiento
				model.pagado = pago
				model.save()
				return HttpResponseRedirect('/agregado/cuentas/ver')


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
			return render(request, 'recepcion/cuentas/EditarCuentaXpagar.html', {'info':info,
																			'form':form,
																			'model':model})


	else:
		
		form = FormCuentasXpagarRecepcion(instance=model)
		return render(request, 'recepcion/cuentas/EditarCuentaXpagar.html', {'info':info,
																			'form':form,
																			'model':model})


@permission_required('auth.acceso_analista',login_url="/accounts/login/")
def Ver_Recepcion(request):
	form= Recepcion.objects.filter(null=False).order_by('fecha_llegada')
	if request.method=='POST':
		if request.POST['lista-pdf'] == 'lista-selected' and request.user.has_perm('auth.acceso_empleado'):
			a=request.POST.getlist('seleccion')
			return lista_recepcion_pdf(request, a, form)
	
		else:
			pass
	else:
		info=''
	return render(request,'recepcion/VerRecepcion.html', {'form':form})

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Add_Recepcion(request):
	info=''
	if request.method=='POST':
		from django.db.models import Q
		form = FormRecepcion(Q(habilitado=True),request.POST)
		
		if form.is_valid():
			producto =  form.cleaned_data['producto']
			variedad =  form.cleaned_data['variedad']
			tipo = form.cleaned_data['tipo']

			ciclo_asociado=  form.cleaned_data['ciclo_asociado']
			fecha_llegada=form.cleaned_data['fecha_llegada']
			tipo_vehiculo= form.cleaned_data['tipo_vehiculo']
			placa = form.cleaned_data['placa']
			productor=  form.cleaned_data['proovedor']
			zona_de_cosecha=  form.cleaned_data['zona_de_cosecha']
			cantidad_en_Kg=  form.cleaned_data['cantidad_en_Kg']
			numero_romana = form.cleaned_data['numero_romana']
			referencia_folder = form.cleaned_data['referencia_folder']


			humedad=  form.cleaned_data['humedad']
			impureza=  form.cleaned_data['impureza']

			silos=  form.cleaned_data['silo']
			planta=form.cleaned_data['planta']

			granos_danados_totales =  form.cleaned_data['granos_danados_totales']
			granos_partidos = form.cleaned_data['granos_partidos']
			temperatura_promedio= form.cleaned_data['temperatura_promedio']
			otros=  form.cleaned_data['otros']
			recibido_por= form.cleaned_data['recibido_por']
			


			con= PrecioDeRubroPorCiclo.objects.filter(producto=producto, variedad=variedad,tipo=tipo,ciclo=ciclo_asociado ) 
			if con.count()==0:return render(request, 'recepcion/AddRecepcion.html', {'form':form,'info':'ESTe Producto No tiene precio asignado'})
			
			model= Recepcion()
			model.producto= producto
			model.variedad= variedad
			model.tipo=tipo
			model.ciclo_asociado= ciclo_asociado
			model.referencia_folder= referencia_folder
			model.numero_romana=numero_romana
			model.planta= planta
			model.silo = silos
			model.fecha_llegada= fecha_llegada
			model.tipo_vehiculo= tipo_vehiculo
			model.placa = placa
			model.proovedor =productor
			model.zona_de_cosecha =zona_de_cosecha
			model.cantidad_en_Kg =cantidad_en_Kg
			model.humedad =humedad
			model.impureza =impureza

			model.granos_danados_totales =granos_danados_totales
			model.granos_partidos= granos_partidos
			model.temperatura_promedio= temperatura_promedio
			model.otros = otros
			model.recibido_por= recibido_por
			Hf = model.producto.tolerancia_humedad - model.producto.diferencia_humedad
			If = model.producto.tolerancia_impureza
			merma_total = mermas(cantidad_en_Kg, humedad,Hf, impureza, If)
			
			if silos.resto > merma_total['CMP']:return render(request, 'recepcion/AddRecepcion.html', {'form':form,'info':'la cantidad ingresada supera la capacidad del silo'.upper()})
			model.save()

			model_pago= PagoRecepcion()
			model_pago.recepcion= model
			model_pago.precio= PrecioDeRubroPorCiclo.objects.get(producto=producto, variedad=variedad,tipo=tipo,ciclo=ciclo_asociado )
			pago = ''
			if 'pagado' in request.POST.keys(): 
				pago= True
			else:
				pago= False


			model_pago.p= pago
			model_pago.save()
			
			model_total = TotalRecepcion()
			model_total.ingreso= model_pago

			

			silos.en_inventario += merma_total['CMP']
			silos.resto = silos.capacidad - silos.en_inventario
			silos.save() 
			
			# ajustar de acuerdo al pago generado
			model_total.descuentoI= merma_total['MI']
			model_total.descuentoH= merma_total['MH']
			model_total.descuentoM= merma_total['MP']
	 		model_total.descuentoTotal= merma_total['MermaTotal']
	 		model_total.cantidad_descuento= merma_total['CantidadDescuento']
	 		model_total.cantidad_real= merma_total['CMP']
	 		
	 		valorespago = ValorTotal(merma_total['CMP'], model_pago.precio.precio_por_Kg, IMPUESTOS)
			model_total.total_neto= valorespago['total_neto']

			model_total.total_Bs= valorespago['total_pago']
			model_total.save()
			if pago == False:
				CXP = CuentasXpagarRecepcion()
				CXP.recepcion = model_total
				CXP.deuda= valorespago['total_pago']
				CXP.saldo_deudor= valorespago['total_pago']
				CXP.fecha_vencimiento= datetime.date(fecha.year,fecha.month,fecha.day )

				CXP.save()
			else:
				pass
	
			return HttpResponseRedirect('/agregado/recepcion/ver/')

	else:
		from django.db.models import Q
		form= FormRecepcion(Q(habilitado=True))
	return render(request, 'recepcion/AddRecepcion.html', {'form':form,
															'info':info})
@permission_required('auth.acceso_analista',login_url="/accounts/login/")
def Edit_Recepcion(request, pk):
	info=''
	try:
		int(pk)
	except ValueError:
		raise Http404()
	info =""
	model = Recepcion.objects.get(pk=pk, null=False)
	model_pago= PagoRecepcion.objects.get(recepcion=model)
	model_total = TotalRecepcion.objects.get(ingreso=model_pago)

	
	if request.method=='POST':

		if 'eliminar' in request.POST.keys() and  request.POST['eliminar']== 'delete-selected' and request.user.has_perm('auth.acceso_empleado'):
			
			model.null= True
			model.save()
			return HttpResponseRedirect(raiz)
		from django.db.models import Q

		form =  FormRecepcionesEdit(Q(habilitado=True),request.POST, instance=model)

		if form.is_valid():
			producto =  form.cleaned_data['producto']
			variedad =  form.cleaned_data['variedad']
			tipo = form.cleaned_data['tipo']
			ciclo_asociado=  form.cleaned_data['ciclo_asociado']
			fecha_llegada=form.cleaned_data['fecha_llegada']
			tipo_vehiculo= form.cleaned_data['tipo_vehiculo']
			placa = form.cleaned_data['placa']
			productor=  form.cleaned_data['proovedor']
			zona_de_cosecha=  form.cleaned_data['zona_de_cosecha']
			cantidad_en_Kg=  form.cleaned_data['cantidad_en_Kg']

			romana=  form.cleaned_data['numero_romana']
			referencia_folder=  form.cleaned_data['referencia_folder']


			humedad=  form.cleaned_data['humedad']
			impureza=  form.cleaned_data['impureza']
			granos_danados_totales =  form.cleaned_data['granos_danados_totales']
			granos_partidos = form.cleaned_data['granos_partidos']
			temperatura_promedio= form.cleaned_data['temperatura_promedio']
			otros=  form.cleaned_data['otros']
			recibido_por= form.cleaned_data['recibido_por']
			observacion= form.cleaned_data['observacion']

			Hf = model.producto.tolerancia_humedad - model.producto.diferencia_humedad
			If = model.producto.tolerancia_impureza
			merma_total = mermas(cantidad_en_Kg, humedad,Hf, impureza, If)

			en_inventario = merma_total['CMP'] - model_total.cantidad_real
			silo = model.silo
			silo.en_inventario = silo.en_inventario + en_inventario
			silo.resto = silo.capacidad - silo.en_inventario
			if silo.resto < 0:return render(request, 'recepcion/EditRecepcion.html', {'form':form,'info':'la cantidad ingresada supera la capacidad del silo'.upper()})

			silo.save() 

			con= PrecioDeRubroPorCiclo.objects.filter(producto=producto, variedad=variedad,tipo=tipo,ciclo=ciclo_asociado ) 
			if con.count()==0:return render(request, 'recepcion/AddRecepcion.html', {'form':form,'info':'ESTe Producto No tiene precio asignado'})

			model.producto= producto
			model.variedad= variedad
			model.tipo=tipo
			model.ciclo_asociado= ciclo_asociado
			model.fecha_llegada= fecha_llegada
			model.tipo_vehiculo= tipo_vehiculo
			model.placa = placa
			model.numero_romana= romana
			model.referencia_folder=referencia_folder
			model.proovedor =productor
			model.zona_de_cosecha =zona_de_cosecha
			model.cantidad_en_Kg =cantidad_en_Kg
			model.humedad =humedad
			model.impureza =impureza
			model.granos_danados_totales =granos_danados_totales
			model.granos_partidos= granos_partidos
			model.temperatura_promedio= temperatura_promedio
			model.otros = otros
			model.recibido_por= recibido_por
			model.observacion= observacion
			model.save()
			model_pago.precio = PrecioDeRubroPorCiclo.objects.get(producto=producto,
																variedad=variedad,
																tipo=tipo,
																ciclo=ciclo_asociado )
			
			model_pago.save()

			
			 

			

			# ajustar de acuerdo al pago generado
			model_total.descuentoI= merma_total['MI']
			model_total.descuentoH= merma_total['MH']
			model_total.descuentoM= merma_total['MP']
	 		model_total.descuentoTotal= merma_total['MermaTotal']
	 		model_total.cantidad_descuento= merma_total['CantidadDescuento']
	 		model_total.cantidad_real= merma_total['CMP']
	 		
	 		valorespago = ValorTotal(merma_total['CMP'], model_pago.precio.precio_por_Kg, IMPUESTOS)
			model_total.total_neto= valorespago['total_neto']

			model_total.total_Bs= valorespago['total_pago']
			model_total.save()
			
			if model_pago.p == False:
				CXP = CuentasXpagarRecepcion.objects.get(recepcion=model_total)
				CXP.deuda= valorespago['total_pago']
				CXP.saldo_deudor= valorespago['total_pago'] - CXP.abono
				CXP.save()
			else:
				pass
			info= 'Se ha Editado Satisfactoriamente'
			
			return render(request, 'recepcion/EditRecepcion.html', {'form':form,
															'model':model,
															'model_pago':model_pago,
															'model_total':model_total,
															'info':info})

	else:
		from django.db.models import Q
		form=  FormRecepcionesEdit(Q(habilitado=True), instance=model)
	return render(request, 'recepcion/EditRecepcion.html', {'form':form,
															'model':model,
															'model_pago':model_pago,
															'model_total':model_total,
															'info':info})

a= """model_pago.precio = PrecioDeRubroPorCiclo.objects.get(producto=producto,
																									variedad=variedad,
																									tipo=tipo,
																									ciclo=ciclo_asociado )
		model_pago.pago= 'Pagado'
		model_pago.save()
		valorespago = ValorTotal(model.cantidad_en_Kg, model_pago.precio.precio_por_Kg, IMPUESTOS)
		# ajustar de acuerdo al pago generado

		model_total.total_neto= model.cantidad_en_Kg * float(model_pago.precio.precio_por_Kg)

		model_total.total_Bs= valorespago['total_pago']
		model_total.save()"""


@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Ver_Pago_Recepcion(request):
	form= PagoRecepcion.objects.all()
	return render(request,'recepcion/VerPagoRecepcion.html', {'form':form})


@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Add_Pago_Recepcion(request):
	info=''
	if request.method=='POST':
		form = FormPagoRecepcion(request.POST)
		if form.is_valid():
			#return HttpResponse(form)
			recepcion = form.cleaned_data['recepcion']
			precio = form.cleaned_data['precio']

			pago = form.cleaned_data['pago']
			
			model= PagoRecepcion()
			model.recepcion = recepcion
			model.precio = precio
			model.pago = pago

			model.save()
			#return HttpResponse(precio)
			return HttpResponseRedirect('/agregado/recepcion/ver/')

	else:

		form= FormPagoRecepcion()
	
	return render(request, 'recepcion/AddPagoRecepcion.html', {'form':form})

from django.http import JsonResponse

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")

def prueva_ajax(request):
	return JsonResponse({"saluso":"hola mundo"})
	
@permission_required('auth.acceso_empleado',login_url="/accounts/login/")

def Ver_Total_Recepcion(request):
	form= TotalRecepcion.objects.all()
	return render(request,'recepcion/VerTotalRecepcion.html', {'form':form})

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")

def Add_Total_Recepcion(request):
	form= FormTotalRecepcion()
	return render(request, 'recepcion/AddTotalRecepcion.html', {'form':form})

@permission_required('auth.acceso_analista',login_url="/accounts/login/")

def Ver_Factura_Recepcion(request, pk):
	try:
		int(pk)
	except ValueError:
		raise Http404()
	info =""

	recepcion= Recepcion.objects.get(pk= pk)
	pago = PagoRecepcion.objects.get(recepcion= recepcion)
	total_pago= TotalRecepcion.objects.get(ingreso=pago)
	cuenta = Recepcion.cuenta.contar_rubro(pk=pk)
	total= TotalRecepcion.cuenta.contar_rubros(pk=recepcion.producto.pk)
	#for i,k in IMPUESTOS.items():


	#IVA= total_pago.total_neto * (12.0/100)
	#TRASPORTE = total_pago.total_neto *(1.8/100) 

	return render(request,'recepcion/factura_recepcion.html', { 'recepcion':recepcion,
																'pago': pago,
																'total_pago':total_pago,
																'impuestos':IMPUESTOS,
																'cuenta':cuenta,
																'total':total

																})

def cantidad_ingresada_a_silo(request,nombre, pk):
	print pk
	try:
		int(pk)
	except ValueError:
		raise Http404()
	model = TotalRecepcion.cuenta.contar_rubros(pk=pk)
	#proovedor = Productor.zona.cantidad_almacenada(pk= )
	return render(request, 'recepcion/cuentas/CantidadIngresada.html', {'model':model,'nombre':nombre})


def cantidad_ingresada_x_ciclo(request,nombre, pk):
	print pk
	try:
		int(pk)
	except ValueError:
		raise Http404()	
	model = TotalRecepcion.cuenta.contar_rubros( pk=pk)
	#proovedor = Productor.zona.cantidad_almacenada(pk= )
	return render(request, 'recepcion/cuentas/CantidadIngresada.html', {'model':model,'nombre':nombre})
