from django.shortcuts import render
from .models import Plantas, Silos
from .forms import FormSilos, FormPlantas, FormSilosAdd, FormSilosEdit
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse, Http404
from gestion.views import get_query,desabilite_model, delete_model, paginacion
from django.http import Http404

# Create your views here.
def Ver_Plantas(request):
	form=Plantas.objects.filter(null=False)
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
			query = get_query(q,['nombre'])
			#return HttpResponse(query)
			form = form.filter(query)
			#return HttpResponse(forms)

		info =''
		paginator = paginacion(request, form, 20)
		contacts = paginator['modelo']
		lista = paginator['paginas']
		cantidad= paginator['cantidad']

	return render(request,'plantas/VerPlantas.html', {'form':contacts,
		                                                    'info':info,		                                                    
															'lista':lista,
															'cantidad':cantidad, 'q':q})
def Ver_Silos(request, pk):
	try:
		int(pk)
	except ValueError:
		raise Http404()
	form=Silos.objects.filter(plantas__pk=pk, null=False)
	planta= Plantas.objects.get(pk=pk)
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
			query = get_query(q,['nombre','plantas__nombre', 'capacidad', 'descripcion'])
			#return HttpResponse(query)
			form = form.filter(query)
			#return HttpResponse(forms)
		info =''
		paginator = paginacion(request, form, 20)
		contacts = paginator['modelo']
		lista = paginator['paginas']
		cantidad= paginator['cantidad']

	return render(request,'plantas/VerSilos.html', {'form':contacts,
		                                                    'info':info,		                                                    
															'lista':lista,
															'cantidad':cantidad,
															'model':planta,'q':q})

	
@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Add_Plantas(request):
	info=''
	if request.method=='POST':
		
		form = FormPlantas(request.POST)
		
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			cantidad_silos = form.cleaned_data['cantidad_silos']
			descripcion = form.cleaned_data['descripcion']
			
			try:
				model=Plantas()
				model.nombre = nombre
				model.cantidad_silos = cantidad_silos
				model.descripcion=descripcion
				model.save()
			finally:
				return HttpResponseRedirect('/agregado/plantas/edit/%s/'%model.pk)
	else:
		form= FormPlantas()
	return render(request, 'plantas/AddPlantas.html', {'form':form})

def Edit_Plantas(request, pk):
	try:
		int(pk)
	except ValueError:
		raise Http404()
	info =""
	model = Plantas.objects.get(pk=pk, null=False)
	if request.method=='POST':
		if 'eliminar' in request.POST.keys() and  request.POST['eliminar']== 'delete-selected':
			
			model.delete()
			return HttpResponseRedirect('/agregado/ciclo/ver')
		form = FormPlantas(request.POST, instance=model)
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			cantidad_silos = form.cleaned_data['cantidad_silos']
			descripcion = form.cleaned_data['descripcion']
			
			try:
				model.nombre = nombre
				model.cantidad_silos = cantidad_silos
				model.descripcion=descripcion
				model.save()

			finally:
				return HttpResponseRedirect('.')
	else:
		form= FormPlantas(instance=model)

	return render(request, 'plantas/EditPlantas.html',{'form':form, 'model':model})

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def Add_Silos(request, pk):
	info=''
	try:
		int(pk)
	except ValueError:
		raise Http404()
	filtrado= Plantas.objects.get(pk=pk, null=False)
	if request.method=='POST':
		
		form = FormSilosAdd(request.POST)
		
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			capacidad = form.cleaned_data['capacidad']

			descripcion = form.cleaned_data['descripcion']
			
			try:
				model=Silos()
				model.nombre = nombre
				model.capacidad = capacidad
				model.plantas = filtrado
				model.descripcion=descripcion
				model.save()
			finally:
				return HttpResponseRedirect('/agregado/plantas/%s/silos/edit/%s'%(filtrado.pk, model.pk))
	else:
		form= FormSilosAdd()
	return render(request, 'plantas/AddSilos.html', {'form':form, 'model':filtrado})

"""def Edit_Silos(request, pkplanta, pksilo):
	
	if request.method=='POST':
		return HttpResponse('has un post')
	else:
		form= FormSilos()

	return render(request, 'plantas/EditSilos.html',{'form':form, 'model':'model'})"""
def Edit_Silos(request, pkplanta, pksilo):

	info =""
	model = Silos.objects.get(plantas__pk=pkplanta, pk=pksilo, null=False)
	if request.method=='POST':

		if 'eliminar' in request.POST.keys() and  request.POST['eliminar']== 'delete-selected':
			model.null= True
			model.save()
			return HttpResponseRedirect('/agregado/plantas/ver')
		form = FormSilosEdit(request.POST, instance=model)
		
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			
			descripcion = form.cleaned_data['descripcion']
			
			try:
				model.nombre = nombre
				model.descripcion=descripcion
				model.save()

			finally:
				return HttpResponseRedirect('.')
	else:
		form= FormSilosEdit(instance=model)
		#return HttpResponse(request.POST)

	return render(request, 'plantas/EditSilos.html',{'form':form, 'model':model})