from django import forms

from rubro.models import Rubro, VariedadRubro, TipoRubro
from proovedores.models import Productor, ZonaProductor
from plantas.models import Plantas, Silos
from contabilidad.models import Ciclo
from .models import Obrero, Empleado, Puesto, FechaPagosAsignados, CobroSemanalObrero, CobroSemanalEmpleado, BonoDeAlimentacionSemanalEmpleados, BonoDeAlimentacionSemanalObreros, NominaTotalObreros, NominaTotalEmpleados



saludos=('hola', 'mundo')
tipo_de_cuenta= (('Aho', 'Ahorro'), ('Cor', 'Corriente'))


estado=(('', '------------'),
		('Por', 'Portuguesa'),
		('Bar', 'Barinas'),
		('Coj', 'Cojedes'),
		('Gua', 'Guarico'))
 

class FormCobroSemanalEmpleador(forms.ModelForm):
	class Meta:
		model= CobroSemanalEmpleado
		fields='__all__'
		exclude= ['null']
			

"""class FormRecepcion(forms.ModelForm):
	
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

"""
#=============Cliente========
#COLOCAR UN CAMPO PARA VER SI ES EMPRESA O PERSONA
