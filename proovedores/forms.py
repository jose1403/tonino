from django import forms
from .models import  Productor,ZonaProductor

from ajax_select.fields import AutoCompleteSelectField, AutoCompleteSelectMultipleField

saludos=('hola', 'mundo')
tipo_de_cuenta= (('Aho', 'Ahorro'), ('Cor', 'Corriente'))


estado=(('', '------------'),
		('Por', 'Portuguesa'),
	    ('Bar', 'Barinas'),
	    ('Coj', 'Cojedes'),
	    ('Gua', 'Guarico'))
 


#============================================================================================================================0
class FormProductor(forms.ModelForm):
	#Datos Personales
	class Meta:
		model= Productor
		fields= '__all__'
		exclude= ['estado','municipio', 'null']


class FormEditProductor(forms.ModelForm):
	#Datos Personales
	class Meta:
		model= Productor
		fields= ['nombre_o_razon_social','documentoId','domicilio_fiscal', 'telefono', 'celular', 'observacion']
class FormZonaProductor(forms.ModelForm):
	def __init__(self,  *args, **kwargs):
	    super(FormZonaProductor, self).__init__(*args, **kwargs)
	    self.fields['producto'].queryset = Productor.objects.filter( null=False)
	class Meta:
		model = ZonaProductor
		fields='__all__'
		exclude=['productor']
