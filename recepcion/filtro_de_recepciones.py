from django.http import HttpResponse
from .models import Recepcion, CuentasXpagarRecepcion
from .recepcion_pdf import lista_recepcion_pdf
from django.views.generic import DayArchiveView
from django.views.generic import MonthArchiveView
from django.views.generic import YearArchiveView
from gestion.views import delete_model, paginacion,get_query,desabilite_model

class RecepcionesAnuales(YearArchiveView): 
	#queryset = Recepcion.objects.all()
	paginate_by = 25
	template_name='recepcion/recepcion_ano.html'
	date_field = "fecha_llegada"
	context_object_name='form'
	make_object_list = True
	allow_future=True

	q=''
	def get(self, request, *args, **kwargs):
		queryset= Recepcion.objects.filter(null=False)
		q= ''
		model=self.model
		if 'q' in request.GET and request.GET['q'].strip():
			q= request.GET['q']
			query = get_query(q,['pk', 'producto__nombre', 'variedad__nombre',
								'tipo__nombre', 'ciclo_asociado__nombre', 'silo__nombre',
								'proovedor__nombre_o_razon_social',
								'zona_de_cosecha__zona'])
			#return HttpResponse(query)
			queryset = queryset.filter(query)
		
		self.object = queryset
		return super(RecepcionesAnuales, self).get(request, *args, **kwargs)
	def get_context_data(self, **kwargs):
		context = super(RecepcionesAnuales, self).get_context_data(**kwargs)
		context['form'] = self.object
		context['q']= self.q
		return context 
	def get_queryset(self):
		return self.object
	
	def post(self, request, *args, **kwargs):
		if request.POST['lista-pdf'] == 'lista-selected':

			a=request.POST.getlist('seleccion')
			return lista_recepcion_pdf(request, a, Recepcion.objects.filter(null=False))
	
		else:
			return HttpResponseRedirect('.')
class RecepcionesMes(MonthArchiveView):
	'''Entradas por mes'''
	queryset=Recepcion.objects.order_by('fecha_llegada')
	template_name='recepcion/recepcion_mes.html'
	paginate_by = 25
	date_field = 'fecha_llegada'
	month_format = '%m'
	context_object_name='form'
	allow_future=True

	q=''
	def get(self, request, *args, **kwargs):
		queryset= Recepcion.objects.filter(null=False)
		q= ''
		model=self.model
		if 'q' in request.GET and request.GET['q'].strip():
			q= request.GET['q']
			query = get_query(q,['pk', 'producto__nombre', 'variedad__nombre',
								'tipo__nombre', 'ciclo_asociado__nombre', 'silo__nombre',
								'proovedor__nombre_o_razon_social',
								'zona_de_cosecha__zona'])
			#return HttpResponse(query)
			queryset = queryset.filter(query)
		
		self.object = queryset
		return super(RecepcionesMes, self).get(request, *args, **kwargs)
	def get_context_data(self, **kwargs):
		context = super(RecepcionesMes, self).get_context_data(**kwargs)
		context['form'] = self.object
		context['q']= self.q
		return context 
	def get_queryset(self):
		return self.object
	
	def post(self, request, *args, **kwargs):
		if request.POST['lista-pdf'] == 'lista-selected':

			a=request.POST.getlist('seleccion')
			return lista_recepcion_pdf(request, a, Recepcion.objects.filter(null=False))
	
		else:
			return HttpResponseRedirect('.')
class RecepcionesDiarias(DayArchiveView):
	queryset=Recepcion.objects.order_by('fecha_llegada')
	template_name='recepcion/recepcion_dia.html'
	paginate_by = 25
	date_field = 'fecha_llegada'
	context_object_name='form'
	month_format = '%m'
	allow_future=True
	
	q=''
	def get(self, request, *args, **kwargs):
		queryset= Recepcion.objects.filter(null=False)
		q= ''
		model=self.model
		if 'q' in request.GET and request.GET['q'].strip():
			q= request.GET['q']
			query = get_query(q,['pk', 'producto__nombre', 'variedad__nombre',
								'tipo__nombre', 'ciclo_asociado__nombre', 'silo__nombre',
								'proovedor__nombre_o_razon_social',
								'zona_de_cosecha__zona'])
			#return HttpResponse(query)
			queryset = queryset.filter(query)
		
		self.object = queryset
		return super(RecepcionesDiarias, self).get(request, *args, **kwargs)
	def get_context_data(self, **kwargs):
		context = super(RecepcionesDiarias, self).get_context_data(**kwargs)
		context['form'] = self.object
		context['q']= self.q
		return context 
	def get_queryset(self):
		return self.object
	
	def post(self, request, *args, **kwargs):
		if request.POST['lista-pdf'] == 'lista-selected':

			a=request.POST.getlist('seleccion')
			return lista_recepcion_pdf(request, a, Recepcion.objects.filter(null=False))
	
		else:
			return HttpResponseRedirect('.')
		

class CuentasMensuales(MonthArchiveView):
	'''Entradas por mes'''
	queryset=CuentasXpagarRecepcion.objects.order_by('fecha_llegada')
	template_name='cuentas/CuentasMensuales.html'
	paginate_by = 25
	date_field = 'fecha_llegada'
	month_format = '%m'
	context_object_name='form'
	allow_future=True

	q=''
	def get(self, request, *args, **kwargs):
		queryset= Recepcion.objects.filter(null=False)
		q= ''
		model=self.model
		if 'q' in request.GET and request.GET['q'].strip():
			q= request.GET['q']
			query = get_query(q,['pk', 'producto__nombre', 'variedad__nombre',
								'tipo__nombre', 'ciclo_asociado__nombre', 'silo__nombre',
								'proovedor__nombre_o_razon_social',
								'zona_de_cosecha__zona'])
			#return HttpResponse(query)
			queryset = queryset.filter(query)
		
		self.object = queryset
		return super(RecepcionesAnuales, self).get(request, *args, **kwargs)
	def get_context_data(self, **kwargs):
		context = super(RecepcionesAnuales, self).get_context_data(**kwargs)
		context['form'] = self.object
		context['q']= self.q
		return context 
	def get_queryset(self):
		return self.object
	
	def post(self, request, *args, **kwargs):
		if request.POST['lista-pdf'] == 'lista-selected':

			a=request.POST.getlist('seleccion')
			return lista_recepcion_pdf(request, a, Recepcion.objects.filter(null=False))
	
		else:
			return HttpResponseRedirect('.')

		







# Create your views here.
