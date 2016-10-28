# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('despacho', '0002_auto_20161023_0858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='despacho',
            name='ciclo_asociado',
        ),
        migrations.RemoveField(
            model_name='despacho',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='despacho',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='despacho',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='despacho',
            name='variedad',
        ),
        migrations.RemoveField(
            model_name='ingresodespacho',
            name='despacho',
        ),
        migrations.RemoveField(
            model_name='totaldespacho',
            name='ingreso',
        ),
        migrations.DeleteModel(
            name='Despacho',
        ),
        migrations.DeleteModel(
            name='IngresoDespacho',
        ),
        migrations.DeleteModel(
            name='TotalDespacho',
        ),
    ]
