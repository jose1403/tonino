from django import forms
from .models import Despacho, IngresoDespacho, TotalDespacho, CuentasXcobrarDespacho

from ajax_select.fields import AutoCompleteSelectField, AutoCompleteSelectMultipleField

saludos=('hola', 'mundo')
tipo_de_cuenta= (('Aho', 'Ahorro'), ('Cor', 'Corriente'))


estado=(('', '------------'),
		('Por', 'Portuguesa'),
		('Bar', 'Barinas'),
		('Coj', 'Cojedes'),
		('Gua', 'Guarico'))


pagos=(('Pagado', 'Pagado'),('Deuda', 'Deuda'))
#from a
class FormDespacho(forms.ModelForm):

	class Meta:
		model= Despacho
		fields= '__all__'
class FormCuentasXcobrarDespacho(forms.ModelForm):
	class Meta:
		model= CuentasXcobrarDespacho
		fields= '__all__'
		exclude=['despacho']


class FormTotalDespacho(forms.Form):
	class Meta:
		model= TotalDespacho
		fields = '__all__'

# yourapp/lookups.py
