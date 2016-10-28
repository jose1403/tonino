from dejango.template.
@register.inclusion_tag('libros_por_autor.html')
@register.inclusion_tag('template_tags/buscador.html', take_context=True)
def display_buscador_form(context):
	return {
	'q':context['q'],
	}