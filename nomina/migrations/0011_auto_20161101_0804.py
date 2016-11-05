# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nomina', '0010_auto_20161101_0728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bonodealimentacionsemanalempleados',
            old_name='obreros',
            new_name='empleados',
        ),
        migrations.AlterField(
            model_name='fechapagosasignados',
            name='semana',
            field=models.IntegerField(default=0),
        ),
    ]
