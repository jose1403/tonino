from django.contrib import admin

from .models import DATOS_DE_LA_EMPRESA
from django.contrib.auth.models import Permission
admin.site.register(DATOS_DE_LA_EMPRESA)
admin.site.register(Permission)