from django import template 
 
register = template.Library() 
@register.inclusion_tag('buscador.html', take_context=True)
def display_buscador_form(context):
	return {
	'q':context['q'],
	}