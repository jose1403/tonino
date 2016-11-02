from django.contrib import admin
from .models import Despacho, TotalDespacho, IngresoDespacho, CuentasXcobrarDespacho
# Register your models here.
admin.site.register(Despacho)
admin.site.register(IngresoDespacho)
admin.site.register(TotalDespacho)
admin.site.register(CuentasXcobrarDespacho)
