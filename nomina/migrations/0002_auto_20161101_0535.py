# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nomina', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bonodealimentacionsemanalempleados',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='bonodealimentacionsemanalempleados',
            name='obreros',
        ),
        migrations.RemoveField(
            model_name='bonodealimentacionsemanalobreros',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='bonodealimentacionsemanalobreros',
            name='obreros',
        ),
        migrations.RemoveField(
            model_name='cobrosemanalempleado',
            name='empleado',
        ),
        migrations.RemoveField(
            model_name='cobrosemanalempleado',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='cobrosemanalobrero',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='cobrosemanalobrero',
            name='obrero',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='puesto',
        ),
        migrations.RemoveField(
            model_name='nominatotalempleados',
            name='Empleados',
        ),
        migrations.RemoveField(
            model_name='nominatotalempleados',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='nominatotalobreros',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='nominatotalobreros',
            name='obreros',
        ),
        migrations.RemoveField(
            model_name='obrero',
            name='puesto',
        ),
        migrations.DeleteModel(
            name='BonoDeAlimentacionSemanalEmpleados',
        ),
        migrations.DeleteModel(
            name='BonoDeAlimentacionSemanalObreros',
        ),
        migrations.DeleteModel(
            name='CobroSemanalEmpleado',
        ),
        migrations.DeleteModel(
            name='CobroSemanalObrero',
        ),
        migrations.DeleteModel(
            name='Empleado',
        ),
        migrations.DeleteModel(
            name='FechaPagosAsignados',
        ),
        migrations.DeleteModel(
            name='NominaTotalEmpleados',
        ),
        migrations.DeleteModel(
            name='NominaTotalObreros',
        ),
        migrations.DeleteModel(
            name='Obrero',
        ),
        migrations.DeleteModel(
            name='Puesto',
        ),
    ]
