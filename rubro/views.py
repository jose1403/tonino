# -*- encodind: utf-8 -*-
import datetime
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context 

from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required 
from django.contrib import auth
#=================================
from nucleo.models import DATOS_DE_LA_EMPRESA
from gestion.views import get_query,desabilite_model,delete_model, paginacion
from rubro.models import Rubro, VariedadRubro,  TipoRubro
from rubro.forms import FormRubro, FormEditarRubro, FormVariedadRubro, FormEditVariedadRubro,FormTipoRubro, FormEditTipoRubro#, FormProductor, FormZonaProductor
from django.http import HttpResponseRedirect, HttpResponse, Http404

tiempo = datetime.datetime.now()
raiz= '/agregado/rubro/ver'

	

def rubros(request):
	return render(request, 'rubros/InicialRubro.html')



@permission_required('auth.acceso_limit',login_url="/accounts/login/")
def Mostrar_Rubros(request):
	info =''
	lista= ''
	forms=Rubro.objects.filter(null=False)
	nombre = Rubro.__name__.lower() 
	if request.method=='POST' and request.user.has_perm('auth.empleado'):
		if request.POST['eliminar'] == 'delete-selected':
			a=request.POST.getlist('seleccion')
			return desabilite_model(a, forms, '')

		else:
			return HttpResponseRedirect('.')

	else:
		q= ''

		if 'q' in request.GET and request.GET['q'].strip():
			q= request.GET['q']
			query = get_query(q,['nombre','pk', 'nombre_cientifico'])
			#return HttpResponse(query)
			forms = forms.filter(query)
			#return HttpResponse(forms)
		info =''
		paginator = paginacion(request, forms, 20)
		contacts = paginator['modelo']
		lista = paginator['paginas']
		cantidad= paginator['cantidad']
		#q= request.GET.get('q', "")
		

	return render(request, 'rubros/MostrarRubros.html', {'forms': contacts,
														'info':info,
														'lista':lista,
														'cantidad':cantidad,
														'nombre':nombre,
														'q': q})

import csv 
@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def rubro_csv(request):
    
    # Crea un objeto HttpResponse con las cabeceras del CVS correctas.
    response = HttpResponse(content_type='application/csv')
    response['Content-Disposition'] = 'attachment; filename=Listado_de_rubros-%s/%s/%s.csv'%(tiempo.day,tiempo.month, tiempo.year)
 
    # Crea el escritor CSV usando un HttpResponse como "archivo." 
    datos= DATOS_DE_LA_EMPRESA.objects.get(pk=1)
    model= Rubro.objects.filter(null=False)
    variedad= VariedadRubro.objects.all()
    writer = csv.writer(response)
    writer.writerow([datos.NOMBRE])
    writer.writerow([]) 

    writer.writerow(['Codigo En Sistema', 'Nombre', 'Nombre Cientifico', 'T/Humedad', 'T/Impureza']) 
    for p in model:
 
        writer.writerow([p.codigo_en_sistema(), p.nombre, p.nombre_cientifico, p.tolerancia_humedad, p.tolerancia_impureza])


    return response

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Agregar_Rubros(request):
	info = ""
	if request.method=='POST':
		form = FormRubro(request.POST,request.FILES)

		if form.is_valid():
			nombre= form.cleaned_data['nombre']
			nombre_cientifico = form.cleaned_data['nombre_cientifico']
			tolerancia_humedad = form.cleaned_data['tolerancia_humedad']
			diferencia_humedad= form.cleaned_data['diferencia_humedad']
			tolerancia_impureza= form.cleaned_data['tolerancia_impureza']

			foto= form.cleaned_data['foto']
			
			try:
				rubro= Rubro()
				rubro.nombre= nombre.capitalize()
				rubro.nombre_cientifico= nombre_cientifico.capitalize()
				rubro.tolerancia_humedad= tolerancia_humedad
				rubro.diferencia_humedad= diferencia_humedad
				rubro.tolerancia_impureza= tolerancia_impureza
				rubro.foto= foto

				rubro.save()
			#except IntegrityError:
			#	raise formrubro.Error('El nombre de rubro ya esta registrado')
			finally:
				return HttpResponseRedirect('/agregado/rubro/editar/%s'%(rubro.id))
		else:
			info = 'Por favor corrija los sigientes campos'
	else:
		form = FormRubro()
		
	return render(request, 'rubros/AgregarRubro.html', {'form':form})

@permission_required('auth.acceso_analista',login_url="/accounts/login/")
def Editar_Rubro(request, pk):
	info =""
	try:
		int(pk)
	except ValueError:
		raise Http404()
	model = Rubro.objects.get(pk=pk, null=False)
	cuenta = Rubro.cuenta.contar_rubro(pk=pk)
	
	if request.method=='POST' :

		if 'eliminar' in request.POST.keys() and  request.POST['eliminar']== 'delete-selected':
			
			model.null= True
			model.save()
			return HttpResponseRedirect(raiz)

		formrubro = FormRubro(request.POST,request.FILES, instance=model)

		if formrubro.is_valid():
			nombre= formrubro.cleaned_data['nombre']
			nombre_cientifico = formrubro.cleaned_data['nombre_cientifico']
			tolerancia_humedad = form.cleaned_data['tolerancia_humedad']
			diferencia_humedad= form.cleaned_data['diferencia_humedad']
			tolerancia_impureza= form.cleaned_data['tolerancia_impureza']
			foto= formrubro.cleaned_data['foto']
			
			#try:
			model.nombre= nombre.capitalize()
			model.nombre_cientifico= nombre_cientifico.capitalize()
			model.tolerancia_humedad= tolerancia_humedad
			model.diferencia_humedad= diferencia_humedad
			model.tolerancia_impureza= tolerancia_impureza
			if foto == None:
				model.foto = rubro.foto
			else:
				model.foto = foto

			model.save()
			#except IntegrityError:
			#	raise formrubro.Error('El nombre de rubro ya esta registrado')
			return HttpResponseRedirect('.')
	else:
		formrubro= FormRubro(instance=model)

	return render(request, 'rubros/EditarRubro.html', {'formrubro':formrubro,
														'model':model,
														'info': info,'cuenta':cuenta})

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def rubro_id_csv(request,pk):
    response = HttpResponse(content_type='application/csv')
    response['Content-Disposition'] = 'attachment; filename=Listado_de_rubros-%s/%s/%s.csv'%(tiempo.day,tiempo.month, tiempo.year)
 
    # Crea el escritor CSV usando un HttpResponse como "archivo." 
    datos= DATOS_DE_LA_EMPRESA.objects.get(pk=1)
    model= Rubro.objects.get(pk=pk, null=False)

    variedad= VariedadRubro.objects.filter(rubro=model, null=False)
    tipo= TipoRubro.objects.filter(rubro=model, null=False)

    writer = csv.writer(response)
    writer.writerow([datos.NOMBRE])
    writer.writerow(['', 'RUBRO Y CARACTERISTICAS']) 

    writer.writerow(['Codigo En Sistema', 'Nombre', 'Nombre Cientifico']) 
    writer.writerow([model.codigo_en_sistema(), model.nombre, model.nombre_cientifico])
    writer.writerow([])
    writer.writerow(['','VARIEDADES'])
    writer.writerow(['Nombre', 'Descripcion'])

    for p in variedad:
    	writer.writerow([p.nombre, p.descripcion])

    writer.writerow([])
    writer.writerow(['','TIPOS'])
    writer.writerow(['Nombre', 'Descripcion'])

    for p in tipo:
    	writer.writerow([ str(p.nombre), str(p.descripcion)])





    return response


@permission_required('auth.acceso_limit',login_url="/accounts/login/")
def Rubro_Variedades_Ver(request, pk):
	try:
		int(pk)
	except ValueError:
		raise Http404()
	forms = VariedadRubro.objects.filter(rubro__pk=pk, null=False)
	rubro= Rubro.objects.get(pk=pk)
	if request.method=='POST' and request.user.has_perm('auth.empleado'):
		if request.POST['eliminar'] == 'delete-selected':
			a=request.POST.getlist('seleccion')
			return desabilite_model(a, forms, '')

		else:
			pass
	else:
		info=''
	return render(request, 'rubros/VerVariedadRubro.html',{'forms':forms, 'rubro':rubro})
	
@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Rubro_Variedades_Add(request, pk):
	try:
		int(pk)
	except ValueError:
		raise Http404()
	rubro = Rubro.objects.get(pk=pk, null=False)
	
	info=''
	if request.method=='POST':
		form = FormEditVariedadRubro(request.POST)
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			descripcion = form.cleaned_data['descripcion']
			modelo = VariedadRubro.objects.filter(rubro=rubro, nombre=nombre.capitalize(), null=False)
			print modelo.count()
			if modelo.count() >=1:
				info= 'este nombre ya esta registrado'
				return render(request, 'rubros/VariedadRubro.html', {'form':form,
																  'info':info})
			model= VariedadRubro()
			model.rubro= rubro
			model.nombre= nombre.capitalize()
			model.descripcion= descripcion.capitalize()
			model.save()
			return HttpResponseRedirect('/agregado/rubro/%s/variedades/edit/%s'%(rubro.id, model.id))
	else:
		form = FormEditVariedadRubro()
	return render(request, 'rubros/VariedadRubro.html', {'form':form, 'rubro':rubro})

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Rubro_Variedades_Edit(request, pkrubro, pkvariedad):
	try:
		int(pkrubro)
		int(pkvariedad)
	except ValueError:
		raise Http404()
	info =""
	model = VariedadRubro.objects.get(rubro__pk=pkrubro, pk=pkvariedad, null=False)
	rubro= Rubro.objects.get(pk=pkrubro)
	if request.method=='POST':
		if 'eliminar' in request.POST.keys() and  request.POST['eliminar']== 'delete-selected':
			
			model.null=True
			model.save()
			return HttpResponseRedirect('/agregado/rubro-variedades/ver/')
		form = FormEditVariedadRubro(request.POST, instance=model)

		if form.is_valid():

			nombre = form.cleaned_data['nombre']
			descripcion = form.cleaned_data['descripcion']
			if str(rubro)== 'None':
				pass
			else:
				model.rubro= rubro
			model.nombre= nombre.capitalize()
			model.descripcion= descripcion.capitalize()
			model.save()
			return HttpResponseRedirect('.')
	else:
		form= FormEditVariedadRubro(instance=model)

	return render(request, 'rubros/EditarVariedadRubro.html',{'form':form, 'model':model, 'rubro':rubro})

@permission_required('auth.acceso_limit',login_url="/accounts/login/")
def Rubro_Tipo_Ver(request, pk):
	try:
		int(pk)
	except ValueError:
		raise Http404()
	rubro = Rubro.objects.get(pk=pk, null=False)
	form = TipoRubro.objects.filter(rubro__pk=pk, null=False)
	if request.method=='POST' and request.user.has_perm('auth.empleado'):
		if request.POST['eliminar'] == 'delete-selected':
			a=request.POST.getlist('seleccion')
			return desabilite_model(a, form, '')

		else:
			pass
	else:
		info=''
	return render(request, 'rubros/VerTipoRubro.html',{'form':form, 'rubro':rubro})

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Rubro_Tipo_Add(request, pk):

	info=''
	try:
		int(pk)
	except ValueError:
		raise Http404()
	rubro = Rubro.objects.get(pk=pk, null=False)
	if request.method=='POST':
		form = FormEditVariedadRubro(request.POST)
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			descripcion = form.cleaned_data['descripcion']
			modelo = TipoRubro.objects.filter(rubro=rubro, nombre=nombre.capitalize())

			if modelo.count() >=1:
				info= 'este nombre ya esta registrado'
				return render(request, 'rubros/TipoRubro.html', {'form':form,
																  'info':info})
			model= TipoRubro()
			model.rubro= rubro
			model.nombre= nombre.capitalize()
			model.descripcion= descripcion.capitalize()
			model.save()
			return HttpResponseRedirect('/agregado/rubro/%s/tipo/edit/%s'%(rubro.id, model.id))

	else:
		form = FormEditVariedadRubro()

	return render(request, 'rubros/TipoRubro.html', {'form':form, 'info':info, 'rubro':rubro})

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Rubro_Tipo_Edit(request, pkrubro, pktipo):
	try:
		int(pkrubro)
		int(pktipo)
	except ValueError:
		raise Http404()
	info =""
	rubro= Rubro.objects.get(pk=pkrubro)
	model = TipoRubro.objects.get(rubro__pk=pkrubro, pk=pktipo, null=False)
	if request.method=='POST':
		if 'eliminar' in request.POST.keys() and  request.POST['eliminar']== 'delete-selected':	
			model.null= False
			model.save()
			return HttpResponseRedirect('/agregado/rubro-tipo/ver/')
		form = FormEditVariedadRubro(request.POST, instance=model)

		if form.is_valid():

			nombre = form.cleaned_data['nombre']
			descripcion = form.cleaned_data['descripcion']
			if str(rubro)== 'None':
				pass
			else:
				model.rubro= rubro
			model.nombre= nombre.capitalize()
			model.descripcion= descripcion.capitalize()
			model.save()
			return HttpResponseRedirect('.')
	else:
		form= FormEditVariedadRubro(instance=model)

	return render(request, 'rubros/EditarTipoRubro.html',{'form':form, 'model':model, 'rubro':rubro})


