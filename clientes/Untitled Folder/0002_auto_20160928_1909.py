# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0003_auto_20160928_1909'),
        ('despacho', '0002_auto_20160928_1909'),
        ('contabilidad', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Impuesto',
        ),
        migrations.RemoveField(
            model_name='precioderubroporciclo',
            name='ciclo',
        ),
        migrations.RemoveField(
            model_name='precioderubroporciclo',
            name='clasificacion',
        ),
        migrations.RemoveField(
            model_name='precioderubroporciclo',
            name='producto',
        ),
        migrations.DeleteModel(
            name='Ciclo',
        ),
        migrations.DeleteModel(
            name='PrecioDeRubroPorCiclo',
        ),
    ]
