from django.contrib import admin
from .models import Obrero, Empleado, Puesto, FechaPagosAsignados, CobroSemanalObrero, CobroSemanalEmpleado, BonoDeAlimentacionSemanalEmpleados, BonoDeAlimentacionSemanalObreros, NominaTotalObreros, NominaTotalEmpleados

admin.site.register(Obrero)
admin.site.register(Empleado)
admin.site.register(Puesto)


admin.site.register(FechaPagosAsignados)
admin.site.register(CobroSemanalObrero)
admin.site.register(CobroSemanalEmpleado)
admin.site.register(BonoDeAlimentacionSemanalEmpleados)
admin.site.register(BonoDeAlimentacionSemanalObreros)
admin.site.register(NominaTotalEmpleados)
admin.site.register(NominaTotalObreros)
