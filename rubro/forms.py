from django import forms
from rubro.models import Rubro, VariedadRubro, TipoRubro


class FormRubro(forms.ModelForm):
	"""nombre= forms.CharField(widget=forms.TextInput())
				nombre_cientifico= forms.CharField(widget=forms.TextInput())
				foto= forms.ImageField(label='Imagen Opcional', required=False)"""

	class Meta:
		model= Rubro
		fields= '__all__'

class FormEditarRubro(forms.ModelForm):
	class meta:
		model= Rubro
		Fields = ['nombre', 'nombre_cientifico', 'foto']

class FormVariedadRubro(forms.Form):
	rubro= forms.ModelChoiceField(queryset=Rubro.objects.all(), empty_label='Defina el rubro')
	nombre=forms.CharField(widget=forms.TextInput())
	descripcion=forms.CharField(widget=forms.Textarea)

class FormEditVariedadRubro(forms.ModelForm):
	class Meta:
		model= VariedadRubro
		fields = '__all__'
		exclude=['rubro']



# Topo dentado o duro
class FormTipoRubro(forms.Form):
	rubro=forms.ModelChoiceField(queryset=Rubro.objects.all(), empty_label='Defina el rubro')
	nombre= forms.CharField(widget=forms.TextInput())
	descripcion=forms.CharField(widget=forms.Textarea)


class FormEditTipoRubro(forms.ModelForm):
	class Meta:
		model= TipoRubro
		fields = '__all__'
		exclude = ['rubro']