# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0003_auto_20161024_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagorecepcion',
            name='precio',
        ),
        migrations.RemoveField(
            model_name='pagorecepcion',
            name='recepcion',
        ),
        migrations.RemoveField(
            model_name='recepcion',
            name='ciclo_asociado',
        ),
        migrations.RemoveField(
            model_name='recepcion',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='recepcion',
            name='proovedor',
        ),
        migrations.RemoveField(
            model_name='recepcion',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='recepcion',
            name='variedad',
        ),
        migrations.RemoveField(
            model_name='recepcion',
            name='zona_de_cosecha',
        ),
        migrations.RemoveField(
            model_name='totalrecepcion',
            name='ingreso',
        ),
        migrations.DeleteModel(
            name='PagoRecepcion',
        ),
        migrations.DeleteModel(
            name='Recepcion',
        ),
        migrations.DeleteModel(
            name='TotalRecepcion',
        ),
    ]
