# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
            name='RubroDisponible',
        ),
    ]
