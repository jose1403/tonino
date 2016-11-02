# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0009_auto_20161025_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuentasxpagarrecepcion',
            name='fecha_vencimiento',
            field=models.DateField(),
        ),
    ]
