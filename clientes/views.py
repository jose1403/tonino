from django.shortcuts import render
#==========================
from django.contrib.auth.decorators import login_required, permission_required

from django.http import HttpResponseRedirect, HttpResponse, Http404
#============================
from .models import Cliente
from .forms import FormCliente
from nucleo.models import DATOS_DE_LA_EMPRESA
import csv
from gestion.views import delete_model, paginacion,get_query,desabilite_model

import datetime
raiz = '/agregado/cliente/ver/'
tiempo= datetime.datetime.now()
# Create your views here.

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Ver_Cliente(request):
	form= Cliente.objects.filter(habilitado=True, null=False)
	if request.method=='POST':
		if request.POST['eliminar'] == 'delete-selected':
			a=request.POST.getlist('seleccion')
			return desabilite_model(a, form, '')

		else:
			pass

	else:
		q= ''

		if 'q' in request.GET and request.GET['q'].strip():
			q= request.GET['q']
			query = get_query(q,['nombre_o_razon_social','pk', 'documentoId', 'domicilio_fiscal',
								'banco__nombre', 'tipo_cuenta__nombre'])
			#return HttpResponse(query)
			form = form.filter(query)
		info =''
		paginator = paginacion(request, form, 3)
		contacts = paginator['modelo']
		lista = paginator['paginas']
		cantidad= paginator['cantidad']
	return render(request,'clientes/VerClientes.html', {'form':contacts,
		                                                    'info':info,
															'lista':lista,
															'cantidad':cantidad, 'q':q})
@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def lista_clientes_csv(request): 
    # Crea un objeto HttpResponse con las cabeceras del CVS correctas. 
    cvs_name='LISTADO-CLIENTES'
    response = HttpResponse(content_type='application/csv')
    response['Content-Disposition'] = 'attachment; filename=%s-%s/%s/%s.pdf'%(cvs_name,
    																		 tiempo.day,
    																		 tiempo.month,
    																		 tiempo.year)
 
    # Crea el escritor CSV usando un HttpResponse como "archivo." 
    model= Cliente.objects.filter(habilitado=True, null=False)

    datos = DATOS_DE_LA_EMPRESA.objects.get(pk=1)
    writer = csv.writer(response)
    writer.writerow([''])

    writer.writerow(['','', datos.NOMBRE.upper()])
   
    writer.writerow([''])


    writer.writerow(['', '', 'LISTADO DE CLIENTES'])
    writer.writerow(['FECHA:','%s/%s/%s'%(tiempo.day,tiempo.month, tiempo.year)])
    writer.writerow([''])


    writer.writerow(['N','NOMBRE', 'C.I./R.I.F.','DOMICILIO FISCAL', 'TELEFONO', 'CELULAR', 'REF']) 
    cont =0
    ref =''
    for p in model:
    	cont+=1
    	ref = p.referencia_folder
    	if ref == '0':
    		ref = 'S/R'
        writer.writerow([cont,p.nombre_o_razon_social.upper(),p.documentoId.upper(), p.domicilio_fiscal.upper(), p.telefono, p.celular, ref])
    return response

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Add_Cliente(request):
	info=''
	if request.method=='POST':
		form = FormCliente(request.POST)
		if form.is_valid():
			try:

				nombre =  form.cleaned_data['nombre_o_razon_social']

				documentoId=  form.cleaned_data['documentoId']
				#informacion de Contactos
				domicilio_fiscal=  form.cleaned_data['domicilio_fiscal']
				telefono=  form.cleaned_data['telefono']
				celular=  form.cleaned_data['celular']

				referencia_folder= form.cleaned_data['referencia_folder']
				# Datos bancarios

				cuenta_bancaria=  form.cleaned_data['cuenta_bancaria']
				tipo_cuenta=  form.cleaned_data['tipo_cuenta']
				banco= form.cleaned_data['banco']
				observacion=  form.cleaned_data['observacion']

				model= Cliente()
			
				model.nombre_o_razon_social= nombre

				model.documentoId= documentoId
				model.domicilio_fiscal =domicilio_fiscal

				model.telefono =telefono
				model.celular =celular
				model.referencia_folder= referencia_folder
				model.cuenta_bancaria =cuenta_bancaria
				model.tipo_cuenta = tipo_cuenta
				model.banco =banco
				model.observacion = observacion
				model.save()
			finally:

				return HttpResponseRedirect('/agregado/cliente/edit/%s'%model.pk)


	else:
		form = FormCliente()
	return render(request, 'clientes/AddClientes.html', {'form':form, info:info})

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Edit_Cliente(request, pk):
	try:
		int(pk)
	except ValueError:
		raise Http404()
	info =""
	model = Cliente.objects.get(pk=pk, null=False)
	if request.method=='POST':
		if 'eliminar' in request.POST.keys() and  request.POST['eliminar']== 'delete-selected':
			
			model.null= False
			model.save()
			return HttpResponseRedirect(raiz)
	if request.method=='POST':
		form = FormCliente(request.POST, instance=model)

		if form.is_valid():

			nombre =  form.cleaned_data['nombre_o_razon_social']
			documentoId=  form.cleaned_data['documentoId']

			#informacion de Contactos
			domicilio_fiscal=  form.cleaned_data['domicilio_fiscal']

			telefono=  form.cleaned_data['telefono']
			celular=  form.cleaned_data['celular']
			referencia_folder= form.cleaned_data['referencia_folder']

			# Datos bancarios
			cuenta_bancaria=  form.cleaned_data['cuenta_bancaria']
			tipo_cuenta=  form.cleaned_data['tipo_cuenta']
			banco= form.cleaned_data['banco']
			observacion=  form.cleaned_data['observacion']

		
			model.nombre_o_razon_social= nombre

			model.documentoId= documentoId
			model.domicilio_fiscal =domicilio_fiscal

			model.telefono =telefono
			model.celular =celular
			model.referencia_folder= referencia_folder
			model.cuenta_bancaria =cuenta_bancaria
			model.tipo_cuenta = tipo_cuenta
			model.banco =banco
			model.observacion = observacion
			model.save()
			return HttpResponseRedirect('.')
	else:
		form= FormCliente(instance=model)

	return render(request, 'clientes/EditClientes.html',{'form':form, 'model':model})
