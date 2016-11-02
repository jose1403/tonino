# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0007_remove_pagorecepcion_pago'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuentasxpagarrecepcion',
            name='recepcion',
        ),
        migrations.RemoveField(
            model_name='pagorecepcion',
            name='precio',
        ),
        migrations.RemoveField(
            model_name='pagorecepcion',
            name='recepcion',
        ),
        migrations.RemoveField(
            model_name='totalrecepcion',
            name='ingreso',
        ),
        migrations.DeleteModel(
            name='CuentasXpagarRecepcion',
        ),
        migrations.DeleteModel(
            name='PagoRecepcion',
        ),
        migrations.DeleteModel(
            name='TotalRecepcion',
        ),
    ]
