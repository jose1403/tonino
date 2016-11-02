from django.contrib import admin
from .models import  PrecioDeRubroPorCiclo, Ciclo, Bancos, TipoCuenta#CuentasXpagarRecepcion, CuentasXcobrarDespacho
# Register your models here.

#----Contabilidad-----------
admin.site.register(PrecioDeRubroPorCiclo)
admin.site.register(Ciclo)
admin.site.register(Bancos)
admin.site.register(TipoCuenta)
#admin.site.register(CuentasXpagarRecepcion)

#admin.site.register(CuentasXcobrarDespacho)


