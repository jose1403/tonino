
from .models import DATOS_DE_LA_EMPRESA
from recepcion.models import Recepcion
import django

SENIAT = 'Seniat'
NOMBRE_DE_LA_EMPRESA= 'SILOS MOLIVEN C.A.'

def DatosDeLaEmpresa(request):
	datos = DATOS_DE_LA_EMPRESA.objects.get(pk=1)
	return datos


def DefinirMeses(request):
	recepcion= Recepcion.objects.all()
	anos, meses, dias= [], [],[]
	mes= {'01':'Enero','02':'Febrero','03':'Marzo', '04':'Abril','05':'Mayo',
		  '06':'Junio', '07':'Julio', '08':'Agosto','09':'Septiembre',
		  '10':'Octubre', '11':'Nombiembre', '12':'Diciembre'}
	lista=[]
	
	
	fechas={'anos':anos, 'meses':meses,'dias':dias}
	return mes
def DefinirDias(request):
	lista=[]
	for i in range(31):
		if i <9:
			lista.append('0%s'%(i+1))
		else:
			lista.append('%s'%(i+1))

	return lista
def my_processor(request):
	context = {"django_version":django.get_version(),
				"get_DatosDeLaEmpresa":DatosDeLaEmpresa(request),
				"get_DefinirMeses":DefinirMeses(request),
				"get_DefinirDias":DefinirDias(request),			

	}
	return context