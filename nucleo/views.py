from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
#******===================================================================*********

from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import auth
#*****]===================================================================*********
from gestion.forms import Secion
# Create your views here.
from rubro.models import Rubro
from contabilidad.models import Ciclo, PrecioDeRubroPorCiclo
from recepcion.models import Recepcion, TotalRecepcion, PagoRecepcion, CuentasXpagarRecepcion
from despacho.models import Despacho, TotalDespacho, IngresoDespacho, CuentasXcobrarDespacho
from clientes.models import Cliente
from proovedores.models import Productor, ZonaProductor

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


def GananciasDelCicloTotal(request):
	ciclo = Ciclo.objects.filter(null=False)
	recepcion = ciclo.recepcion_set.filter(null=False)
	ingreso_total=0
	for i in recepcion:
		pago =PagoRecepcion.objects.get(recepcion=i)
		total=TotalRecepcion.objects.get(ingreso=pago)
		ingreso_total+= total.total_Bs

def GananciasDelCiclo(request, pk):
	try:
		int(pk)

	except ValueError:
		raise Http404()
	ciclo = Ciclo.objects.get(pk=pk, null=False)
	print ciclo
	recepcion = ciclo.recepcion_set.filter(null=False)
	despacho= ciclo.despacho_set.filter(null=False)
	ingreso_total=0
	invercion_total=0
	deuda=0
	cobro=0
	lista_rubror=[]
	rubro = Rubro.objects.filter(null=False)

	for i in rubro:
		producto= i.recepcion_set.filter(null=False, ciclo_asociado__pk=pk)
		if producto.count() > 0:
			lista_rubror.append(i)


	for i in recepcion:
		pago =PagoRecepcion.objects.get(recepcion=i)
		total=TotalRecepcion.objects.get(ingreso=pago)
		invercion_total+= total.total_Bs
		if pago.p==False:
			cuentas= CuentasXpagarRecepcion.objects.get(recepcion=total, pagado=False)
			deuda += cuentas.saldo_deudor


	for e in despacho:
		pago= IngresoDespacho.objects.get(despacho=e)
		total= TotalDespacho.objects.get(ingreso=pago)
		ingreso_total += total.total_Bs
		if pago.pagado==False:
			cuentas= CuentasXcobrarDespacho.objects.get(despacho=total, pagado=False)
			cobro += cuentas.saldo_deudor


	ganancia_neta= ingreso_total - invercion_total

	deudas= CuentasXpagarRecepcion.objects.filter(pagado=False)
	cobros= CuentasXcobrarDespacho.objects.filter(pagado=False)



	return render(request, 'procesos/cuentas/GananciasDelCiclo.html', {'form':ciclo, 
															'invercion_total':invercion_total,
															'ingreso_total':ingreso_total,
															'ganancia_neta':ganancia_neta,
															'deuda':deuda, 'cobro':cobro,
															'lista_rubror':lista_rubror})
def GananciasDelCicloXRubro(request, pkciclo, pkrubro):
	try:
		int(pkciclo)
		int(pkrubro)

	except ValueError:
		raise Http404()
	ciclo = Ciclo.objects.get(pk=pkciclo, null=False)
	print ciclo
	recepcion = ciclo.recepcion_set.filter(null=False, producto__pk=pkrubro)
	despacho= ciclo.despacho_set.filter(null=False, producto__pk=pkrubro)
	ingreso_total=0
	invercion_total=0
	deuda=0
	cobro=0
	lista_rubror=[]
	rubro = Rubro.objects.get(pk=pk,null=False)


	for i in recepcion:
		pago =PagoRecepcion.objects.get(recepcion=i)
		total=TotalRecepcion.objects.get(ingreso=pago)
		invercion_total+= total.total_Bs
		if pago.p==False:
			cuentas= CuentasXpagarRecepcion.objects.get(recepcion=total, pagado=False)
			deuda += cuentas.saldo_deudor


	for e in despacho:
		pago= IngresoDespacho.objects.get(despacho=e)
		total= TotalDespacho.objects.get(ingreso=pago)
		ingreso_total += total.total_Bs
		if pago.pagado==False:
			cuentas= CuentasXcobrarDespacho.objects.get(despacho=total, pagado=False)
			cobro += cuentas.saldo_deudor


	ganancia_neta= ingreso_total - invercion_total

	return render(request, 'procesos/cuentas/GananciasDelCiclo.html', {'form':ciclo,

															'invercion_total':invercion_total,
															'ingreso_total':ingreso_total,
															'ganancia_neta':ganancia_neta,
															'deuda':deuda, 'cobro':cobro,
															'rubro':rubro})
