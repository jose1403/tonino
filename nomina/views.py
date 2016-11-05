from django.shortcuts import render
from .models import Obrero, Empleado, Puesto, FechaPagosAsignados, CobroSemanalObrero, CobroSemanalEmpleado, BonoDeAlimentacionSemanalEmpleados, BonoDeAlimentacionSemanalObreros, NominaTotalObreros, NominaTotalEmpleados
from .forms import FormCobroSemanalEmpleador
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView 
#from biblioteca.models import Editor 
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.core.urlresolvers import reverse_lazy 
from django.views.generic.dates import ArchiveIndexView
#from biblioteca.models import Autor 
 
def ver_nomina(request):
 	return render(request, 'nomina/VerNomina.html')
class AddEmpleado(CreateView): 
    model = Empleado 
    fields = ['nombre', 'apellido', 'documentoID','fecha_de_nacimiento', 'domicilio', 'genero',
    		'fecha_ingreso', 'contrato', 'referecia_contrato', 'puesto', 'sueldo_mensual'] 
    template_name= 'nomina/AddEmpleados.html'

class ActualizarEmpleado(UpdateView): 
    model = Empleado 
    fields =['nombre', 'apellido', 'documentoID','fecha_de_nacimiento','domicilio', 'genero',
    		'fecha_ingreso', 'contrato', 'referecia_contrato', 'puesto', 'sueldo_mensual']
    template_name= 'nomina/EditEmpleados.html'
 
class BorrarEmpleado(DeleteView): 
    model = Empleado 
    success_url = reverse_lazy('ver-empleado') 

class VerEmpleado(ListView): 
    model = Empleado 
    context_object_name = 'form' 
    template_name= 'nomina/VerEmpleados.html'

class AddObrero(CreateView): 
    model = Obrero 
    fields = ['nombre', 'apellido', 'documentoID','fecha_de_nacimiento', 'domicilio', 'genero',
    		'fecha_ingreso', 'contrato', 'referecia_contrato', 'puesto', 'sueldo_mensual'] 
    template_name= 'nomina/AddObrero.html'

class ActualizarObrero(UpdateView): 
    model = Obrero 
    fields =['nombre', 'apellido', 'documentoID','fecha_de_nacimiento','domicilio', 'genero',
    		'fecha_ingreso', 'contrato', 'referecia_contrato', 'puesto', 'sueldo_mensual']
    template_name= 'nomina/EditObrero.html'
 
class BorrarObrero(DeleteView): 
    model = Obrero 
    success_url = reverse_lazy('ver-empleado') 

class VerObrero(ListView): 
    model = Obrero 
    context_object_name = 'form' 
    template_name= 'nomina/VerObrero.html'


class AddPuestos(CreateView): 
    model = Puesto 
    fields = ['nombre', 'descripcion'] 
    template_name= 'nomina/AddPuestos.html'

class ActualizarPuestos(UpdateView): 
    model = Puesto 
    fields =['nombre', 'descripcion']
    template_name= 'nomina/EditPuestos.html'
 
class BorrarPuestos(DeleteView): 
    model = Puesto 
    success_url = reverse_lazy('ver-empleado') 

class VerPuestos(ListView): 
    model = Puesto 
    context_object_name = 'form' 
    template_name= 'nomina/VerPuestos.html'

class AddFechasAsignadas(CreateView): 
    model = FechaPagosAsignados 
    fields = ['fecha_inicio','fecha_cierre'] 
    template_name= 'nomina/AddFechaAsignada.html'

class ActualizarFechasAsignadas(UpdateView): 
    model = FechaPagosAsignados 
    fields =['fecha_inicio','fecha_cierre', 'semana']
    template_name= 'nomina/EditFechaAsignada.html'
 
class BorrarFechasAsignadas(DeleteView): 
    model = FechaPagosAsignados 
    success_url = reverse_lazy('ver-empleado') 

class VerFechasAsignadas(ListView): 
    model = FechaPagosAsignados 
    context_object_name = 'form' 
    template_name= 'nomina/VerFechaAsignada.html'


class AddPagosSemanalesObrero(CreateView): 
    model = CobroSemanalObrero 
    fields = ['fecha','obrero','descuento_faov','sueldo_diario', 'dias_trabajados', 'bono_nocturno', 'total_asignacion',
    			'descuento_ivss', 'total_deducciones','total_a_cobrar' ] 
    template_name= 'nomina/pagos/AddPagoSemanalObrero.html'





class ActualizarPagosSemanalesObrero(UpdateView): 
    model = CobroSemanalObrero 
    fields =['fecha','obrero','descuento_faov','sueldo_diario', 'dias_trabajados', 'bono_nocturno', 'total_asignacion',
    			'descuento_ivss', 'total_deducciones','total_a_cobrar' ]
    template_name= 'nomina/pagos/EditPagoSemanalObrero.html'
 
class BorrarPagosSemanalesObrero(DeleteView): 
    model = CobroSemanalObrero 
    success_url = reverse_lazy('ver-empleado') 

class VerPagosSemanalesObrero(ListView): 
    model = CobroSemanalObrero 
    context_object_name = 'form' 
    template_name= 'nomina/pagos/VerPagoSemanalObrero.html'

def AddPagosSemanalesEmpleado(request): 
    form = FormCobroSemanalEmpleador
    #context_object_name= 'form'
    #fields = ['fecha','empleado','sueldo_diario', 'dias_trabajados', 'bono_nocturno', 'total_asignacion',
    #           'descuento_ivss','descuento_faov', 'total_deducciones','total_a_cobrar' ] 
    #template_name= 'nomina/pagos/AddPagoSemanalEmpleado.html'
    #q=''
   
    if request.method=='POST':
        r= CobroSemanalEmpleado()

        form= FormCobroSemanalEmpleador(request.POST, instance=r)
        if form.is_valid():
            empleado=form.cleaned_data['empleado']
            fecha= form.cleaned_data['fecha']

            model =  CobroSemanalEmpleado.objects.filter(empleado=empleado, fecha=fecha, null=False)
            if model.count()>0:
                info = 'Este Empleado ya Tiene Pago Asignado'
                return render(request, 'nomina/pagos/AddPagoSemanalEmpleado.html', {'form':form,'info':info})
            form.save()
            nomina= NominaTotalEmpleados.objects.filter(fecha=fecha)
            if nomina.count() <0:
                namina = NominaTotalEmpleados.objects.create(fecha=fecha, empleados=empleado, total_nomina=1, total_empleados=1)
            else:
                for i in nomina:
                    i.empleados += empleado
                    i.total_nomina += r.total_a_cobrar
                    i.total_empleados +=1

            #model =  CobroSemanalEmpleado.objects.filter(empleado=empleado, fecha=fecha)
            return HttpResponse('valid')
    else:
        info =''
   
    return render(request, 'nomina/pagos/AddPagoSemanalEmpleado.html', {'form':form,'info':info})
    model = CobroSemanalEmpleado 
    fields =['fecha','empleado','sueldo_diario', 'dias_trabajados', 'bono_nocturno', 'total_asignacion',
                'descuento_ivss','descuento_faov' ,'total_deducciones','total_a_cobrar' ]
    template_name= 'nomina/pagos/EditPagoSemanalEmpleado.html'

class ActualizarPagosSemanalesEmpleado(UpdateView): 
    model = CobroSemanalEmpleado 
    fields =['fecha','empleado','descuento_faov','sueldo_diario', 'dias_trabajados', 'bono_nocturno', 'total_asignacion',
                'descuento_ivss', 'total_deducciones','total_a_cobrar' ]
    template_name= 'nomina/pagos/EditPagoSemanalEmpleado.html' 
class BorrarPagosSemanalesEmpleado(DeleteView): 
    model = CobroSemanalEmpleado 
    success_url = reverse_lazy('ver-empleado') 

class VerPagosSemanalesEmpleado(ListView): 
    model = CobroSemanalEmpleado 
    context_object_name = 'form' 
    template_name= 'nomina/pagos/VerPagoSemanalEmpleado.html'






class AddBonoAlimentacionSemanalObrero(CreateView): 
    model = BonoDeAlimentacionSemanalObreros 
    fields = ['fecha','obreros','bono_mensual', 'bono_diario', 'dias_trabajados', 'total_a_cobrar']
    template_name= 'nomina/pagos/AddBonoAlimentacionSemanalObrero.html'

class ActualizarBonoAlimentacionSemanalObrero(UpdateView): 
    model = BonoDeAlimentacionSemanalObreros 
    fields =['fecha','obreros','bono_mensual', 'bono_diario', 'dias_trabajados', 'total_a_cobrar']
    template_name= 'nomina/pagos/EditBonoAlimentacionSemanalObrero.html'
 
class BorrarBonoAlimentacionSemanalObrero(DeleteView): 
    model = BonoDeAlimentacionSemanalObreros 
    success_url = reverse_lazy('ver-empleado') 

class VerBonoAlimentacionSemanalObrero(ListView): 
    model = BonoDeAlimentacionSemanalObreros 
    context_object_name = 'form' 
    template_name= 'nomina/pagos/VerBonoAlimentacionSemanalObrero.html'
from django.views.generic import DetailView 
#from biblioteca.models import Editor, Libro 
 

class AddBonoAlimentacionSemanalEmpleado(CreateView): 
    model = BonoDeAlimentacionSemanalEmpleados 
    fields = ['fecha','empleados','bono_mensual', 'bono_diario', 'dias_trabajados', 'total_a_cobrar']
    template_name= 'nomina/pagos/AddBonoAlimentacionSemanalEmpleado.html'

class ActualizarBonoAlimentacionSemanalEmpleado(UpdateView): 
    model = BonoDeAlimentacionSemanalEmpleados 
    fields =['fecha','empleados','bono_mensual', 'bono_diario', 'dias_trabajados', 'total_a_cobrar']
    template_name= 'nomina/pagos/EditBonoAlimentacionSemanalEmpleado.html'
 
class BorrarBonoAlimentacionSemanalEmpleado(DeleteView): 
    model = BonoDeAlimentacionSemanalEmpleados
    success_url = reverse_lazy('ver-empleado') 

class VerBonoAlimentacionSemanalEmpleado(ListView): 
    model = BonoDeAlimentacionSemanalEmpleados 
    context_object_name = 'form' 
    template_name= 'nomina/pagos/VerBonoAlimentacionSemanalEmpleado.html'

class MostrarTotalNominaObreros(ArchiveIndexView):
	model=NominaTotalObreros
	context_object_name='form'
	date_field="fecha_generado"
	template_name='nomina/pagos/VerTotalNominaObrero.html'
	paginate_by=25
	make_object_list = True
	allow_empty=True
	allow_future=True
	q=''


class MostrarTotalNominaEmpleados(ArchiveIndexView):
	model=NominaTotalEmpleados
	context_object_name='form'
	date_field="fecha_generado"
	template_name='nomina/pagos/VerTotalNominaEmpleado.html'
	paginate_by=25
	make_object_list = True
	allow_empty=True
	allow_future=True
	q=''


from django.views.generic import DetailView 
class DetallesEditor(DetailView): 
    model = Empleado 
    context_object_name = 'editor' 
 
    def get_context_data(self, **kwargs): 
        
        context = super(DetallesEditor, self).get_context_data(**kwargs) 
        # Agrega un QuerySet para obtener todos los libros 
        context['lista_libros'] = Libro.objects.all() 
        return context 

def get_queryset(self): 
        self.editor = get_object_or_404(Editor, nombre=self.args[0]) 
        return Libro.objects.filter(editor=self.editor) 
 

 
  
 
def get_context_data(self, **kwargs): 
       
        context = super(ListaLibrosEditores, self).get_context_data(**kwargs) 

        context['editor'] =self.edi

