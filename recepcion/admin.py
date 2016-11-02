from django.contrib import admin
from .models import Recepcion, PagoRecepcion, TotalRecepcion, CuentasXpagarRecepcion
# Register your models here., p
#======Recepcion===============
class RecepcionesAdmin(admin.ModelAdmin): 
	list_display = ('codigo_en_sistema', 'producto', 'ciclo_asociado', 'proovedor', 'cantidad_en_Kg')
	search_fields = ['codigo', 'fecha_llegada']
	list_filter = ('fecha_llegada',) 
	date_hierarchy = 'fecha_llegada'

admin.site.register(Recepcion, RecepcionesAdmin)
admin.site.register(PagoRecepcion)
admin.site.register(TotalRecepcion)
admin.site.register(CuentasXpagarRecepcion)
