from django import forms
from .models import Ciclo, PrecioDeRubroPorCiclo, Bancos, TipoCuenta
from rubro.models import Rubro
saludos=('hola', 'mundo')
tipo_de_cuenta= (('Aho', 'Ahorro'), ('Cor', 'Corriente'))


estado=(('', '------------'),
		('Por', 'Portuguesa'),
	    ('Bar', 'Barinas'),
	    ('Coj', 'Cojedes'),
	    ('Gua', 'Guarico'))

#IMPUESTOS


#=== ======================ciclo de recepcion========

class FormCiclo(forms.ModelForm):
	
	class Meta:
		model= Ciclo
		fields='__all__'
		exclude=['null']


#==============================Precio de Ciclo ===============
class FormPrecioDeRubroPorCiclo(forms.ModelForm):
	def __init__(self,  *args, **kwargs):
	    super(FormPrecioDeRubroPorCiclo, self).__init__(*args, **kwargs)
	    self.fields['producto'].queryset = Rubro.objects.filter( null=False)
	class Meta:
		model = PrecioDeRubroPorCiclo
		fields= '__all__'
		exclude= ['ciclo', 'null']
#=======================================recepcion 

class FormBancos(forms.ModelForm):
	class Meta:
		model= Bancos
		fields= '__all__'

class FormTipoCuenta(forms.ModelForm):
	class Meta:
		model= TipoCuenta
		fields='__all__'



# yourapp/lookups.py
