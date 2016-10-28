from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
#******===================================================================*********

from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import auth
#*****]===================================================================*********
from gestion.forms import Secion
# Create your views here.
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from io import BytesIO
#class IndexView(ListView):
#    template_name = "index.html"
#    model = Clientes
#    context_object_name = "c"


@permission_required('auth.acceso_limit',login_url="/accounts/login/")
def Sitio_Base(request):
	return render(request, 'procesos/page_submit_line.html')

@permission_required('auth.acceso_limit',login_url="/accounts/login/")
def inicio_prinsipal(request):
	return render(request, 'base2.html')

@permission_required('auth.acceso_limit',login_url="/accounts/login/")
class Create(CreateView):
   """ template_name = "create.html"
    form_class = GroupForm
    success_url = 'create'
create = Create.as_view()"""

def login(request):
	errors= False
	info=''
	if request.user.is_authenticated():
		return HttpResponseRedirect('/agregado/nuevo')
	else:
		if request.method=='POST':
			form= Secion(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
    			password = form.cleaned_data['password']
    			user = auth.authenticate(username=username, 
    									password=password) 
    			if user is not None and user.is_active: 
        # Contrasena correcta y usuario marcado como "activo" 
        			auth.login(request, user) 
 
        # Redireccciona a una pagina de entrada correcta. 
        			return HttpResponseRedirect("/agregado/nuevo") 
	    		else:
	    			errors = True
	    			info= u'Por favor introduce el nombre de usuario y la clave correctos para una cuenta de personal. Observa que campos pueden ser sensibles a mayusculas.'
	    			return render(request, 'admin/login.html', {'form':form,
	    														'info':info,
																'errors':errors})
		else:
			form = Secion()
		return render(request, 'admin/login.html', {'form':form, 'info':info})
def logout(request): 
    auth.logout(request) 
    # Redireccciona a una pagina de entrada correcta.    
    return HttpResponseRedirect('/accounts/login')
@permission_required('auth.acceso_empleado',login_url="/accounts/login/")
def agregado(request):
	return render(request, 'base.html')

@login_required
def proceso(request):
	print 'funciona'
	return render(request, 'procesos/index.html')


