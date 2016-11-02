# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0005_auto_20161024_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagorecepcion',
            name='pagado',
        ),
        migrations.AlterField(
            model_name='pagorecepcion',
            name='pago',
            field=models.CharField(max_length=6, choices=[(b'Pagado', b'Pagado'), (b'Deuda', b'Deuda')]),
        ),
    ]
