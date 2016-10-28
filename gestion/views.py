from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import InvalidPage, Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import permission_required

# Create your views here.
def delete_model(lista, queryset, raiz):
	info= 'objetos eliminados correctamente'
	cambio= False
	if type(lista)== int:
		lista= [lista] 
		cambio=True
	model = queryset.filter(id__in=lista)

	model.delete()
	#t = get_template('procesos/delete_model_seleccionados.html') 
	#html = t.render(Context({'queryset': model}))

	if cambio == True:
		return HttpResponseRedirect(raiz)
	else:
		return HttpResponseRedirect('.')

def desabilite_model(lista, queryset, raiz):
    info= 'objetos eliminados correctamente'
    cambio= False
    if type(lista)== int:
        lista= [lista] 
        cambio=True
    model = queryset.filter(id__in=lista)

    for modelo in model:
        modelo.null=True
        modelo.save()

    #t = get_template('procesos/delete_model_seleccionados.html') 
    #html = t.render(Context({'queryset': model}))

    if cambio == True:
        return HttpResponseRedirect(raiz)
    else:
        return HttpResponseRedirect('.')

@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def paginacion(request, model, num):
	paginator = Paginator(model, num)
	page = request.GET.get('page')
	try:
	    forms = paginator.page(page)
	except PageNotAnInteger:

	    forms = paginator.page(1)
	except EmptyPage:
	    forms = paginator.page(paginator.num_pages)

	bum = paginator.num_pages
	lista= []
	for num in range(bum):
	    lista.append(num+1)
	#contenidos.paginator.num_pages
	return {'modelo':forms, 'paginas':lista, 'cantidad':bum}

def get_search_fields(request):
        """
        Returns a sequence containing the fields to be searched whenever
        somebody submits a search query.
        """
        search_fields=()
        return search_fields

from rubro.models import Rubro
from django.db import models
from functools import partial, reduce, update_wrapper
import operator
from django.contrib.admin.utils import (
    NestedObjects, flatten_fieldsets, get_deleted_objects,
    lookup_needs_distinct, model_format_dict, quote, unquote,
)
model=Rubro()
opts = model._meta

def buscador(request, queryset, search_term='arroz'):
        return HttpResponse(request.GET['selec-model'])
        model=request.GET['selec-model']()
        search=request.GET['q']
        queryset=model.objects.all()

        """
        Returns a tuple containing a queryset to implement the search,
        and a boolean indicating if the results may contain duplicates.
        """
        # Apply keyword searches.
        def construct_search(field_name):
            if field_name.startswith('^'):
                return "%s__istartswith" % field_name[1:]
            elif field_name.startswith('='):
                return "%s__iexact" % field_name[1:]
            elif field_name.startswith('@'):
                return "%s__search" % field_name[1:]
            else:
                return "%s__icontains" % field_name

        use_distinct = False
        search_fields = 'nombre' #get_search_fields(request)
        if search_fields and search_term:
            #orm_lookups = [construct_search(str(search_field))
            #               for search_field in search_fields]
            orm_lookups=[construct_search(str(search_fields))]
            for bit in search_term.split():
                or_queries = [models.Q(**{orm_lookup: bit})
                              for orm_lookup in orm_lookups]
                queryset = queryset.filter(reduce(operator.or_, or_queries))
            if not use_distinct:
                for search_spec in orm_lookups:
                    if lookup_needs_distinct(opts, search_spec):
                        use_distinct = True
                        break
        for i in queryset:
        	print i.nombre.upper()
        	print i.nombre_cientifico.upper()

        return HttpResponse(queryset, use_distinct)


import re
from django.db.models import Q
def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    '''hace una busqueda de subcadenas que separa las palabras claves en la busqueda
        por ejemplo si busco 'el amor mio' separara ['el', 'amor', 'mio'] y retornara la lista
    
    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(query_string, search_fields):
    '''busca sobre una lista de campos la lista de palabras probista y debuelve las sentencias q correspondientes

    '''
    query = None        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None 
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query


def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        
        entry_query = get_query(query_string, ['title', 'body',])
        
        found_entries = Entry.objects.filter(entry_query).order_by('-pub_date')

    return render_to_response('search/search_results.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))
#@login_required
def get_full_query(query_string, model):
    """ Returns a query to search in every field of the given model """
    fields = []
    for f in model._meta.fields:
        if not f.rel:
            fields.append(f.name)
        else:
            rel_fields = [ "%s__%s" % (f.name, fr.name) for fr in f.rel.to._meta.fields if not fr.rel ]
            fields.extend(rel_fields)
    return get_query(query_string, fields)
# queryset = MyTable._default_manager.all() # [2]
#if q:
#    query = get_full_query(q, MyTable)
#    queryset = queryset.filter(query)
#
#Este queryset contiene el listado que le pasamos a la plantilla:
#
#return render_to_response("my_list.html",
#    {
#        "object_list": queryset,
#        "q": q,
#    },

"""def buscador(request):
	
    error_pub=''
    error_pro=''
    a = 0
    if request.method=='GET':
        if 'buscar' in request.GET and request.GET['buscar']:
            busqueda = request.GET['buscar']
		
            publicaciones= Publicaciones.objects.filter(titulo__istartswith=busqueda).order_by('titulo')
            numero_pub = publicaciones.count()
            if numero_pub == 0:
                error_pub= 'No se Encontraron Publicaciones'
            productos= Productos.objects.filter(disponible=True, nombre__istartswith=busqueda).order_by('nombre')
            numero_pro = productos.count()
            if numero_pro == 0:
                error_pro = 'No se encontraron Productos'
		
    return render(request, 'inicio/buscador.html', {'publicaciones':publicaciones,
													'productos':productos,
													'numero_pub':numero_pub,
													'numero_pro':numero_pro,
													'error_pro':error_pro,
													'error_pub':error_pub

															})"""