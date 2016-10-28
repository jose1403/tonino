from django import forms
from .models import Cliente#COLOCAR UN CAMPO PARA VER SI ES EMPRESA O PERSONA

saludos=('hola', 'mundo')
tipo_de_cuenta= (('Aho', 'Ahorro'), ('Cor', 'Corriente'))


estado=(('', '------------'),
		('Por', 'Portuguesa'),
	    ('Bar', 'Barinas'),
	    ('Coj', 'Cojedes'),
	    ('Gua', 'Guarico'))
 
class FormCliente(forms.ModelForm):
	class Meta:
		model= Cliente
		fields= '__all__'
