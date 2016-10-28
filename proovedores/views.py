#-*- encoding: utf-8 -*-
from django.shortcuts import render
#==========================
from django.contrib.auth.decorators import login_required, permission_required

from django.http import HttpResponseRedirect, HttpResponse, Http404
import datetime
#============================
from .models import Productor, ZonaProductor
from nucleo.models import DATOS_DE_LA_EMPRESA
from proovedores.forms import FormProductor, FormZonaProductor, FormEditProductor
from gestion.views import delete_model, paginacion,get_query,desabilite_model
from PIL import Image
import os
raiz ='/agregado/proovedor/ver'
tiempo = datetime.datetime.now()

# Create your views here.
import csv 



@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Agregar_Productor(request):
	return render(rquest, 'AgregarProductor.html')
 
#==============================================================================

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Ver_Productor(request):
	form= Productor.objects.filter(habilitado=True, null=False)
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
		paginator = paginacion(request, form, 20)
		contacts = paginator['modelo']
		lista = paginator['paginas']
		cantidad= paginator['cantidad']
	return render(request, 'productor/VerProductores.html',{'form':contacts,
		                                                    'info':info,		                                                    
															'lista':lista,
															'cantidad':cantidad,'q':q})

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def lista_productores_csv(request): 
    # Crea un objeto HttpResponse con las cabeceras del CVS correctas. 
    cvs_name='LISTADO-PROOVEDORES'
    response = HttpResponse(content_type='application/csv')
    response['Content-Disposition'] = 'attachment; filename=%s-%s/%s/%s.pdf'%(cvs_name,
    																		 tiempo.day,
    																		 tiempo.month,
    																		 tiempo.year)
 
    # Crea el escritor CSV usando un HttpResponse como "archivo." 
    model= Productor.objects.all()
    datos = DATOS_DE_LA_EMPRESA.objects.get(pk=1, null=False)
    writer = csv.writer(response)
    writer.writerow([''])

    writer.writerow(['','', datos.NOMBRE.upper()])
   
    writer.writerow([''])


    writer.writerow(['', '', 'LISTADO DE PROOVEDORES'])
    writer.writerow(['FECHA:','%s/%s/%s'%(tiempo.day,tiempo.month, tiempo.year)])
    writer.writerow([''])

    ref =''
    writer.writerow(['N','NOMBRE', 'C.I./R.I.F.','DOMICILIO FISCAL', 'TELEFONO', 'CELULAR', 'REF']) 
    cont =0
    for p in model:
    	cont+=1
    	ref= p.model.referencia_folder
    	if ref=='0':
    		ref='S/N'

        writer.writerow([cont,p.nombre_o_razon_social.upper(),p.documentoId.upper(), p.domicilio_fiscal.upper(), p.telefono, p.celular, ref])
    return response



@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Add_Productor(request):
	info=''
	if request.method=='POST':
		form = FormProductor(request.POST)
		#return HttpResponse(request.POST['nombre_o_razon_social'])
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
				try:
					model= Productor()
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
					return HttpResponseRedirect('/agregado/rubro-proovedor/edit/%s'%model.id)

	else:
		form = FormProductor()

	return render(request, 'productor/AddProductor.html', {'form':form})



@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Rubro_Productor_Edit(request, pk):
	try:
		int(pk)
	except ValueError:
		raise Http404()
	info =""
	model = Productor.objects.get(pk=pk, null=False)
	if request.method=='POST':
		if 'eliminar' in request.POST.keys() and  request.POST['eliminar']== 'delete-selected':
			
			model.null=True
			model.save()
			return HttpResponseRedirect(raiz)

		form = FormProductor(request.POST, instance=model)
		if form.is_valid():	
			nombre =  form.cleaned_data['nombre_o_razon_social']
			documentoId=  form.cleaned_data['documentoId']
			#informacion de Contactos
			domicilio_fiscal=  form.cleaned_data['domicilio_fiscal']
			telefono=  form.cleaned_data['telefono']
			celular=  form.cleaned_data['celular']
			# Datos bancarios
			observacion=  form.cleaned_data['observacion']
			model.nombre_o_razon_social= nombre
			model.documentoId= documentoId
			model.domicilio_fiscal =domicilio_fiscal

			model.telefono =telefono
			model.celular =celular

			#model.cuenta_bancaria =cuenta_bancaria
			#model.tipo_cuenta = tipo_cuenta
			#model.banco =banco
			model.observacion = observacion
			model.save()
			return HttpResponseRedirect('.')
	else:
		form= FormProductor(instance=model)

	return render(request, 'productor/EditProductor.html',{'form':form, 'model':model})

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Ver_Zonas_Productor(request, pk):
	try:
		int(pk)
	except ValueError:
		raise Http404()
	form= ZonaProductor.objects.filter(productor__pk=pk, null=False)
	productor= Productor.objects.get(pk=pk)
	if request.method=='POST':
		if request.POST['eliminar'] == 'delete-selected':
			a=request.POST.getlist('seleccion')
			return desabilite_model(a, form, '')

		else:
			pass
	else:
		q=''
		if 'q' in request.GET and request.GET['q'].strip():
			q= request.GET['q']
			query = get_query(q,['zona', 'estado', 'municipio', 'hectareas'])
			#return HttpResponse(query)
			form = form.filter(query)
		info =''
		paginator = paginacion(request, form, 20)
		contacts = paginator['modelo']
		lista = paginator['paginas']
		cantidad= paginator['cantidad']

	return render(request, 'productor/VerZonasProductor.html', {'form':contacts, 'productor':productor,
																'lista':lista,'cantidad':cantidad,'q':q})


@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Add_Zonas_Productor(request, pk):
	try:
		int(pk)
	except ValueError:
		raise Http404()
	info=''
	productor= Productor.objects.get(pk=pk, null=False)
	if request.method=='POST':
		form = FormZonaProductor(request.POST)
		if form.is_valid():
			try:
				
				#except IntegrityError:
				#	raise formrubro.Error('El nombre de rubro ya esta registrado')
				info = 'Por favor corrija los sigientes campos'
				estado = form.cleaned_data['estado']
				municipio = form.cleaned_data['municipio']
				zona = form.cleaned_data['zona']
				hectareas = form.cleaned_data['hectareas']

				model= ZonaProductor()
				model.estado = estado
				model.municipio =  municipio
				model.productor = productor
				model.zona = zona
				model.hectareas = hectareas

				model.save()
			finally:
				return HttpResponseRedirect('/agregado/proovedor/%s/zona/%s'%(productor.pk, model.pk))
		else:
			info = 'Por favor corrija los sigientes campos'
			
	else:
		form = FormZonaProductor()
	
	return render(request, 'productor/AddZonasProductor.html', {'form':form, 'info':info, 'productor':productor})

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Edit_Zona_Productor(request, pkpro, pkzona):
	try:
		int(pkpro)
		int(pkzona)
	except ValueError:
		raise Http404()
	info =""
	model = ZonaProductor.objects.get(productor__pk=pkpro, pk=pkzona,null=False )
	productor= Productor.objects.get(pk= pkpro, null=False)
	if request.method=='POST':

		if 'eliminar' in request.POST.keys() and  request.POST['eliminar']== 'delete-selected':
			
			model.null= True
			model.save()
			return HttpResponseRedirect(raiz)

		form = FormZonaProductor(request.POST, instance=model)

		if form.is_valid():
			estado = form.cleaned_data['estado']
			municipio = form.cleaned_data['municipio']
			zona = form.cleaned_data['zona']
			hectareas = form.cleaned_data['hectareas']

			model.estado = estado
			model.municipio =  municipio 
			model.productor = productor
			model.zona = zona
			model.hectareas = hectareas
			model.save()
			return HttpResponseRedirect('.')
	
	else:
		form= FormZonaProductor(instance=model)

	return render(request, 'productor/EditZonaProductor.html',{'form':form, 'model':model, 'productor':productor})
