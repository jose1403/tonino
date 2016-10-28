from django import forms
from .models import Plantas, Silos

saludos=('hola', 'mundo')
tipo_de_cuenta= (('Aho', 'Ahorro'), ('Cor', 'Corriente'))


estado=(('', '------------'),
		('Por', 'Portuguesa'),
	    ('Bar', 'Barinas'),
	    ('Coj', 'Cojedes'),
	    ('Gua', 'Guarico'))

#IMPUESTOS


#=== ======================ciclo de recepcion========

class FormPlantas(forms.ModelForm):
	
	class Meta:
		model= Plantas
		fields='__all__' 


#==============================Precio de Ciclo ===============
class FormSilos(forms.ModelForm):

	class Meta:
		model = Silos
		fields= '__all__'

class FormSilosEdit(forms.ModelForm):

	class Meta:
		model = Silos
		fields= '__all__'
		exclude= ['capacidad', 'en_inventario', 'resto', 'plantas' ]
#=======================================recepcion 


# yourapp/lookups.py
class FormSilosAdd(forms.ModelForm):

	class Meta:
		model = Silos
		fields= '__all__'
		exclude=['plantas','en_inventario', 'resto',]