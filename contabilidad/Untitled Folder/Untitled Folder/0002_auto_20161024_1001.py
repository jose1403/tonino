# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0002_auto_20161024_1001'),
        ('despacho', '0003_auto_20161024_1001'),
        ('contabilidad', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cantidadegresadoderubroporciclo',
            name='ciclo',
        ),
        migrations.RemoveField(
            model_name='cantidadegresadoderubroporciclo',
            name='rubro',
        ),
        migrations.RemoveField(
            model_name='cantidadegresadototalrubro',
            name='rubro',
        ),
        migrations.RemoveField(
            model_name='cantidadingresadoderubroporciclo',
            name='ciclo',
        ),
        migrations.RemoveField(
            model_name='cantidadingresadoderubroporciclo',
            name='rubro',
        ),
        migrations.RemoveField(
            model_name='cantidadingresadototalrubro',
            name='rubro',
        ),
        migrations.RemoveField(
            model_name='precioderubroporciclo',
            name='ciclo',
        ),
        migrations.RemoveField(
            model_name='precioderubroporciclo',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='precioderubroporciclo',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='precioderubroporciclo',
            name='variedad',
        ),
        migrations.RemoveField(
            model_name='rubrodisponible',
            name='rubro',
        ),
        migrations.DeleteModel(
            name='CantidadEgresadoDeRubroPorCiclo',
        ),
        migrations.DeleteModel(
            name='CantidadEgresadoTotalRubro',
        ),
        migrations.DeleteModel(
            name='CantidadIngresadoDeRubroPorCiclo',
        ),
        migrations.DeleteModel(
            name='CantidadIngresadoTotalRubro',
        ),
        migrations.DeleteModel(
            name='Ciclo',
        ),
        migrations.DeleteModel(
            name='PrecioDeRubroPorCiclo',
        ),
        migrations.DeleteModel(
            name='RubroDisponible',
        ),
    ]
