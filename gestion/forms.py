from django import forms

from ajax_select.fields import AutoCompleteSelectField, AutoCompleteSelectMultipleField

#from ajax_select.fields import make_ajax_field
#class GroupForm(forms.ModelForm):

    #class Meta:
    #    model = Group
 #   pass

  #  members  = make_ajax_field(Release,'members','person')

class Secion(forms.Form):
	username= forms.CharField(widget=forms.TextInput())
	password= forms.CharField(widget=forms.PasswordInput())

