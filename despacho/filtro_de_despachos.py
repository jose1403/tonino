from django.http import HttpResponse
from .models import Despacho
#from .recepcion_pdf import lista_recepcion_pdf
from django.views.generic import DayArchiveView
from django.views.generic import MonthArchiveView
from django.views.generic import YearArchiveView

class DespachosAnuales(YearArchiveView): 
	queryset = Despacho.objects.all()
	paginate_by = 25
	template_name='despacho/despacho_ano.html'
	date_field = "fecha_salida"
	context_object_name='form'
	make_object_list = True
	allow_future=True

	def post(self, request, *args, **kwargs):
		if request.POST['lista-pdf'] == 'lista-selected':
			a=request.POST.getlist('seleccion')
			return lista_recepcion_pdf(request, a, self.queryset)
	
		else:
			return HttpResponseRedirect('.')
class DespachosMes(MonthArchiveView):
	'''Entradas por mes'''
	queryset=Despacho.objects.order_by('fecha_salida')
	template_name='despacho/despacho_mes.html'
	paginate_by = 25
	date_field = 'fecha_salida'
	month_format = '%m'
	context_object_name='form'
	allow_future=True

	def post(self, request, *args, **kwargs):
		if request.POST['lista-pdf'] == 'lista-selected':
			a=request.POST.getlist('seleccion')
			return lista_recepcion_pdf(request, a, self.queryset)
	
		else:
			return HttpResponseRedirect('.')
class DespachosDiarios(DayArchiveView):
	queryset=Despacho.objects.order_by('fecha_salida')
	template_name='despacho/despacho_dia.html'
	paginate_by = 25
	date_field = 'fecha_salida'
	context_object_name='form'
	month_format = '%m'
	allow_future=True
	
	def post(self, request, *args, **kwargs):
		if request.POST['lista-pdf'] == 'lista-selected':
			a=request.POST.getlist('seleccion')
			return lista_recepcion_pdf(request, a, self.queryset)
	
		else:
			return HttpResponseRedirect('.') 
		







# Create your views here.
