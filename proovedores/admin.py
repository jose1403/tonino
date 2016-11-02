from django.contrib import admin

# Register your models here.
from .models import Productor, ZonaProductor
# Register your models here.
#-----Productor--------------#
admin.site.register(Productor)
admin.site.register(ZonaProductor)