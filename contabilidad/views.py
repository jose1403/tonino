from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib import auth

from django.http import HttpResponseRedirect, HttpResponse, Http404

from .models import  Ciclo, PrecioDeRubroPorCiclo, Bancos, TipoCuenta
from .forms import  FormCiclo, FormPrecioDeRubroPorCiclo, FormBancos, FormTipoCuenta
from gestion.views import delete_model, paginacion,get_query,desabilite_model
from django.http import Http404

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Contabilidad(request):
	return render(request, 'contabilidad/contabilidad.html')

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Ver_Ciclos(request):
	form=Ciclo.objects.filter(habilitado=True, null=False)
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
			query = get_query(q,['nombre','pk', 'fecha_de_inicio'])
			#return HttpResponse(query)
			form = form.filter(query)

		info =''
		paginator = paginacion(request, form, 20)
		contacts = paginator['modelo']
		lista = paginator['paginas']
		cantidad= paginator['cantidad']

	return render(request,'ciclo/VerCiclo.html', {'form':contacts,
		                                                    'info':info,		                                                    
															'lista':lista,
															'cantidad':cantidad,
															'q':q})

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Ver_Ciclos_Des(request):
	form=Ciclo.objects.filter(habilitado=False, null=False)
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
			query = get_query(q,['nombre','pk', 'fecha_de_inicio'])
			#return HttpResponse(query)
			form = form.filter(query)
		info =''
		nombre=1
		paginator = paginacion(request, form, 20)
		contacts = paginator['modelo']
		lista = paginator['paginas']
		cantidad= paginator['cantidad']

	return render(request,'ciclo/VerCiclo.html', {'form':contacts,
		                                                    'info':info,		                                                    
															'lista':lista,
															'cantidad':cantidad,
															'nombre': nombre, 'q':q})


@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Add_Ciclos(request):
	info=''
	if request.method=='POST':
		
		form = FormCiclo(request.POST)
		
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			fecha_de_inicio = form.cleaned_data['fecha_de_inicio']
			fecha_de_cierre = form.cleaned_data['fecha_de_cierre']
			habilitado = form.cleaned_data['habilitado']

			try:
				model= Ciclo()
				model.nombre = nombre
				model.fecha_de_inicio = fecha_de_inicio
				model.fecha_de_cierre = fecha_de_cierre
				model.habilitado=habilitado
				model.save()
			finally:
				return HttpResponseRedirect('/agregado/ciclo/ver')
	else:
		form= FormCiclo()
	return render(request, 'ciclo/AddCiclo.html', {'form':form})

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Edit_Ciclos(request, pk):
	try:
		int(pk)
	except ValueError:
		raise Http404()
	info =""
	model = Ciclo.objects.get(pk=pk, null=False)
	if request.method=='POST':
		if 'eliminar' in request.POST.keys() and  request.POST['eliminar']== 'delete-selected':
			
			model.null=True
			model.save()
			return HttpResponseRedirect('/agregado/ciclo/ver')
		form = FormCiclo(request.POST, instance=model)
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			fecha_de_inicio = form.cleaned_data['fecha_de_inicio']
			fecha_de_cierre = form.cleaned_data['fecha_de_cierre']

			habilitado = form.cleaned_data['habilitado']

			model.nombre = nombre
			model.habilitado=habilitado
			model.fecha_de_inicio = fecha_de_inicio
			model.fecha_de_cierre = fecha_de_cierre
			model.save()
			return HttpResponseRedirect('.')
	else:
		form= FormCiclo(instance=model)

	return render(request, 'ciclo/EditCiclo.html',{'form':form, 'model':model})

#**********************===============================********************
@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Ver_PresioXCiclo(request, pk):
	form=PrecioDeRubroPorCiclo.objects.filter(ciclo__pk=pk, null=False)
	ciclo = Ciclo.objects.get(pk=pk,null=False)
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
			query = get_query(q,['producto__nombre','pk', 'variedad__nombre', 
								'tipo__nombre', 'precio_por_Kg'])
			#return HttpResponse(query)
			form = form.filter(query, ciclo=ciclo, null=False)
		info ='Ver Todos Los Precios'
		paginator = paginacion(request, form, 20)
		contacts = paginator['modelo']
		lista = paginator['paginas']
		cantidad= paginator['cantidad']
	return render(request,'ciclo/VerPresioXCiclo.html', {'form':contacts,
		                                                    'info':info,		                                                    
															'lista':lista,
															'cantidad':cantidad,
															'ciclo':ciclo,'q':q})

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Ver_Presio_Ciclo(request, nciclo):

	form=PrecioDeRubroPorCiclo.objects.filter(ciclo__nombre=str(nciclo), null=False)
	ciclo = Ciclo.objects.filter(null=True)
	if request.method=='POST':
		if request.POST['eliminar'] == 'delete-selected':
			a=request.POST.getlist('seleccion')
			return delete_model(a, form, '')

		else:
			pass

	else:
		q= ''

		if 'q' in request.GET and request.GET['q'].strip():
			q= request.GET['q']
			query = get_query(q,['rubro','pk', 'variedad', 'tipo', 'precio', 'ciclo'])
			#return HttpResponse(query)
			form = form.filter(query)
		info =str(nciclo)
		nombre= 1
		paginator = paginacion(request, form, 3)
		contacts = paginator['modelo']
		lista = paginator['paginas']
		cantidad= paginator['cantidad']
	return render(request,'ciclo/VerPresioXCiclo.html', {'form':contacts,
		                                                    'info':info,
		                                                    'nombre':nombre,		                                                    
															'lista':lista,
															'cantidad':cantidad,
															'ciclo':ciclo, 'q':q})

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Add_PresioXCiclo(request, pk):
	info=''
	try:
		int(pk)

	except ValueError:
		raise Http404()
	ciclo= Ciclo.objects.get(pk=pk)
	if request.method=='POST':
		form = FormPrecioDeRubroPorCiclo(request.POST)
		
		if form.is_valid():
			producto = form.cleaned_data['producto']
			variedad= form.cleaned_data['variedad']
			tipo = form.cleaned_data['tipo']
			precio_por_Kg = form.cleaned_data['precio_por_Kg']

			filtro= PrecioDeRubroPorCiclo.objects.filter(producto=producto, variedad=variedad, tipo=tipo, ciclo=ciclo)
			if filtro.count() >=1:
				info= 'ya esta registrado este producto en este ciclo'
				return render(request, 'ciclo/AddPresioXCiclo.html', {'form':form,
																	  'info':info, 'ciclo':ciclo})

			try:
				model= PrecioDeRubroPorCiclo()
				model.producto = producto
				model.variedad = variedad
				model.tipo= tipo
				model.ciclo = ciclo
				model.precio_por_Kg = precio_por_Kg

				model.save()
			finally:
				return HttpResponseRedirect('/agregado/ciclo/%s/precios/edit/%s'%(ciclo.pk, model.pk))
	else:
		form= FormPrecioDeRubroPorCiclo()
	return render(request, 'ciclo/AddPresioXCiclo.html', {'form':form, 'info':info, 'ciclo':ciclo})

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Edit_PresioXCiclo(request, pkciclo, pkprecio):
	try:
		int(pkciclo)
		int(pkprecio)
	except ValueError:
		raise Http404()
	info =""
	model= PrecioDeRubroPorCiclo.objects.get(ciclo__pk=pkciclo, pk=pkprecio, null=False)
	if request.method=='POST':
		if 'eliminar' in request.POST.keys() and  request.POST['eliminar']== 'delete-selected':
			
			model.desabilite_model()
			return HttpResponseRedirect('/agregado/ciclo/precios/ver/')
	if request.method=='POST':
		form = FormPrecioDeRubroPorCiclo(request.POST, instance=model)
		if form.is_valid():
			producto = form.cleaned_data['producto']
			variedad= form.cleaned_data['variedad']
			tipo = form.cleaned_data['tipo']
			ciclo = form.cleaned_data['ciclo']
			precio_por_Kg = form.cleaned_data['precio_por_Kg']

			model.producto = producto
			model.variedad = variedad
			model.tipo= tipo
			model.ciclo = ciclo
			model.precio_por_Kg = precio_por_Kg

			model.save()
			return HttpResponseRedirect('.')
	else:
		form= FormPrecioDeRubroPorCiclo(instance=model)
	return render(request, 'ciclo/EditPresioXCiclo.html', {'form':form, 'model':model})

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Ver_Bancos(request):
	form = Bancos.objects.filter(null=False)
	if request.method=='POST':
		if request.POST['eliminar'] == 'delete-selected':
			a=request.POST.getlist('seleccion')
			return desabilite_model(a, form, '')

		else:
			pass
	else:
		info=''
		q= ''

		if 'q' in request.GET and request.GET['q'].strip():
			q= request.GET['q']
			query = get_query(q,['nombre','pk'])
			#return HttpResponse(query)
			form = form.filter(query)

	return render(request, 'contabilidad/VerBancos.html',{'form':form, 'q':q})

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Add_Bancos(request):
	info=''
	if request.method=='POST':
		form = FormBancos(request.POST)
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			descripcion = form.cleaned_data['descripcion']
			
			model= Bancos()
			model.nombre= nombre.capitalize()
			model.descripcion= descripcion.capitalize()
			model.save()
			return HttpResponseRedirect('/agregado/bancos/edit/%s'%model.id)
	else:
		form = FormBancos()
	return render(request, 'contabilidad/AddBancos.html', {'form':form})

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Edit_Bancos(request, pk):

	try:
		int(pk)
	except ValueError:
		raise Http404()
	info =""
	model = Bancos.objects.get(pk=pk, null=False)
	if request.method=='POST':
		if 'eliminar' in request.POST.keys() and  request.POST['eliminar']== 'delete-selected':
			
			model.null=True
			model.save()
			return HttpResponseRedirect('/agregado/bancos/ver/')
		form = FormBancos(request.POST, instance=model)
		
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			descripcion = form.cleaned_data['descripcion']
	
			model.nombre= nombre.capitalize()
			model.descripcion= descripcion.capitalize()

			model.save()
			return HttpResponseRedirect('.')
	else:
		form= FormBancos(instance=model)

	return render(request, 'contabilidad/EditBancos.html',{'form':form, 'model':model})

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Ver_Tipo_Cuenta(request):
	form = TipoCuenta.objects.filter(null=False)
	if request.method=='POST':
		if request.POST['eliminar'] == 'delete-selected':
			a=request.POST.getlist('seleccion')
			return delete_model(a, form, '')

		else:
			pass
	else:
		info=''
	return render(request, 'contabilidad/VerTipoCuenta.html',{'form':form})

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Add_Tipo_Cuenta(request):
	info=''
	if request.method=='POST':
		form = FormTipoCuenta(request.POST)
		if form.is_valid():
			nombre = form.cleaned_data['nombre']

			
			model= TipoCuenta()
			model.nombre= nombre.capitalize()
			model.save()
			return HttpResponseRedirect('/agregado/bancos/tipo-cuenta/edit/%s'%model.id)
	else:
		form = FormTipoCuenta()
	return render(request, 'contabilidad/AddTipoCuenta.html', {'form':form})

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Edit_Tipo_Cuenta(request, pk):
	try:
		int(pk)
	except ValueError:
		raise Http404()
	info =""
	model = TipoCuenta.objects.get(pk=pk, null=False)
	if request.method=='POST':
		if 'eliminar' in request.POST.keys() and  request.POST['eliminar']== 'delete-selected':
			
			model.null=True
			model.save()
			return HttpResponseRedirect('/agregado/bancos/ver/')
		form = FormTipoCuenta(request.POST, instance=model)

		if form.is_valid():

			nombre = form.cleaned_data['nombre']
			model.nombre= nombre.capitalize()
			
			model.save()
			return HttpResponseRedirect('.')
	else:
		form= FormTipoCuenta(instance=model)

	return render(request, 'contabilidad/EditTipoCuenta.html',{'form':form, 'model':model})