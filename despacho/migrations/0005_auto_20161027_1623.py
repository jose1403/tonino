# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('despacho', '0004_cuentasxcobrardespacho'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuentasxcobrardespacho',
            name='null',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='despacho',
            name='null',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ingresodespacho',
            name='null',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='totaldespacho',
            name='null',
            field=models.BooleanField(default=False),
        ),
    ]
