from django import forms
from .models import Recepcion, PagoRecepcion, TotalRecepcion, CuentasXpagarRecepcion
from rubro.models import Rubro, VariedadRubro, TipoRubro
from proovedores.models import Productor, ZonaProductor
from plantas.models import Plantas, Silos
from contabilidad.models import Ciclo



saludos=('hola', 'mundo')
tipo_de_cuenta= (('Aho', 'Ahorro'), ('Cor', 'Corriente'))


estado=(('', '------------'),
		('Por', 'Portuguesa'),
		('Bar', 'Barinas'),
		('Coj', 'Cojedes'),
		('Gua', 'Guarico'))
 

class FormRecepcion(forms.ModelForm):
	
	def __init__(self, filter, *args, **kwargs):
		super(FormRecepcion, self).__init__(*args, **kwargs)
		#print self.fields['ciclo_asociado'].query_set
		self.fields['ciclo_asociado'].queryset = Ciclo.objects.filter(filter, null=False)
		self.fields['producto'].queryset = Rubro.objects.filter(null=False)
		self.fields['variedad'].queryset = VariedadRubro.objects.filter(null=False)
		self.fields['tipo'].queryset = TipoRubro.objects.filter(null=False)
		self.fields['proovedor'].queryset = Productor.objects.filter(null=False)
		self.fields['zona_de_cosecha'].queryset = ZonaProductor.objects.filter(null=False)
		self.fields['planta'].queryset = Plantas.objects.filter(null=False)
		self.fields['silo'].queryset = Silos.objects.filter(null=False)
	

	class Meta:
		model = Recepcion
		fields= '__all__'
		exclude=['null']


pagos=(('Pagado', 'Pagado'),('Deuda', 'Deuda'))

class FormRecepcionesEdit(forms.ModelForm):
	def __init__(self, filter, *args, **kwargs):
		super(FormRecepcionesEdit, self).__init__(*args, **kwargs)
		#print self.fields['ciclo_asociado'].query_set
		self.fields['ciclo_asociado'].queryset = Ciclo.objects.filter(filter, null=False)
		self.fields['producto'].queryset = Ciclo.objects.filter(null=False)
		self.fields['variedad'].queryset = Ciclo.objects.filter(null=False)
		self.fields['tipo'].queryset = Ciclo.objects.filter(null=False)
		self.fields['proovedor'].queryset = Ciclo.objects.filter(null=False)
		self.fields['zona_de_cosecha'].queryset = Ciclo.objects.filter(null=False)
		
	class Meta:
		model = Recepcion
		fields = '__all__'
		exclude= ['silo', 'planta','null']

class FormCuentasXpagarRecepcion(forms.ModelForm):
	class Meta:
		model = CuentasXpagarRecepcion
		fields= '__all__'
		exclude= ['recepcion']


class FormTotalRecepcion(forms.Form):
	class Meta:
		model = TotalRecepcion
		fields= '__all__'

#=============Cliente========
#COLOCAR UN CAMPO PARA VER SI ES EMPRESA O PERSONA
