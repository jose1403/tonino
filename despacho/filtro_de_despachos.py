from django.http import HttpResponse
from .models import Despacho
#from .recepcion_pdf import lista_recepcion_pdf
from django.views.generic import DayArchiveView
from django.views.generic import MonthArchiveView
from django.views.generic import YearArchiveView
from gestion.views import get_query, desabilite_model

class DespachosAnuales(YearArchiveView): 
	#queryset = Despacho.objects.all()
	paginate_by = 25
	template_name='despacho/despacho_ano.html'
	date_field = "fecha_salida"
	context_object_name='form'
	make_object_list = False
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
		return super(DespachosAnuales, self).get(request, *args, **kwargs)
	def get_context_data(self, **kwargs):
		context = super(DespachosAnuales, self).get_context_data(**kwargs)
		context['form'] = self.object
		context['q']= self.q
		return context 
	def get_queryset(self):
		return self.object
	def post(self, request, *args, **kwargs):
		if request.POST['lista-pdf'] == 'lista-selected':
			a=request.POST.getlist('seleccion')
			return lista_recepcion_pdf(request, a, self.queryset)
	
		else:
			return HttpResponseRedirect('.')

class DespachosMes(MonthArchiveView):
	'''Entradas por mes'''
	#queryset=Despacho.objects.order_by('fecha_salida')
	template_name='despacho/despacho_mes.html'
	paginate_by = 25
	date_field = 'fecha_salida'
	month_format = '%m'
	#context_object_name='form'
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
		return super(DespachosMes, self).get(request, *args, **kwargs)
	def get_context_data(self, **kwargs):
		context = super(DespachosMes, self).get_context_data(**kwargs)
		context['form'] = self.object
		context['q']= self.q
		return context 
	def get_queryset(self):
		return self.object#
	def post(self, request, *args, **kwargs):
		if request.POST['lista-pdf'] == 'lista-selected':
			a=request.POST.getlist('seleccion')
			return lista_recepcion_pdf(request, a, self.queryset)
	
		else:
			return HttpResponseRedirect('.')
class DespachosDiarios(DayArchiveView):
	#queryset=Despacho.objects.order_by('fecha_salida')
	template_name='despacho/despacho_dia.html'
	paginate_by = 25
	date_field = 'fecha_salida'
	#context_object_name='form'
	month_format = '%m'
	allow_future=True
	make_object_list=True
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
		return super(DespachosDiarios, self).get(request, *args, **kwargs)
	def get_context_data(self, **kwargs):
		context = super(DespachosDiarios, self).get_context_data(**kwargs)
		context['form'] = self.object
		context['q']= self.q
		return context 
	def get_queryset(self):
		return self.object
	def post(self, request, *args, **kwargs):
		if request.POST['lista-pdf'] == 'lista-selected':
			a=request.POST.getlist('seleccion')
			return lista_recepcion_pdf(request, a, self.queryset)
	
		else:
			return HttpResponseRedirect('.') 
		







# Create your views here.
