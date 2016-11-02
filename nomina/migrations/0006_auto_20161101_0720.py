# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nomina', '0005_remove_empleado_null'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='documentoID',
            field=models.CharField(max_length=50),
        ),
    ]
