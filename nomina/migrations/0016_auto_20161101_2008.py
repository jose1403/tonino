# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nomina', '0015_auto_20161101_1638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nominatotalempleados',
            old_name='total_obreros',
            new_name='total_empleados',
        ),
        migrations.AlterField(
            model_name='cobrosemanalobrero',
            name='fecha',
            field=models.ForeignKey(to='nomina.FechaPagosAsignados'),
        ),
    ]
