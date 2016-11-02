# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nomina', '0013_remove_cobrosemanalempleado_fecha_hasta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nominatotalempleados',
            old_name='Empleados',
            new_name='empleados',
        ),
        migrations.AlterField(
            model_name='bonodealimentacionsemanalobreros',
            name='fecha',
            field=models.ForeignKey(to='nomina.FechaPagosAsignados'),
        ),
        migrations.AlterField(
            model_name='cobrosemanalempleado',
            name='fecha',
            field=models.ForeignKey(to='nomina.FechaPagosAsignados'),
        ),
        migrations.AlterField(
            model_name='nominatotalobreros',
            name='fecha_generado',
            field=models.DateField(),
        ),
    ]
