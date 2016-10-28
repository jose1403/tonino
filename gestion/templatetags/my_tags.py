from django.template import Library, defaulttags
from django.utils.deprecation import (
    RemovedInDjango19Warning, RemovedInDjango20Warning,
)

register = Library()
@register.inclusion_tag('buscador.html', takes_context=True)
def display_buscador_form(context):
	return {'q':context['q']}

