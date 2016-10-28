# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0005_cuentasxpagarrecepcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagorecepcion',
            name='pago',
            field=models.BooleanField(),
        ),
    ]
