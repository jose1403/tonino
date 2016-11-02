# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0012_auto_20161030_0621'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuentasxpagarrecepcion',
            name='null',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pagorecepcion',
            name='null',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recepcion',
            name='null',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='totalrecepcion',
            name='null',
            field=models.BooleanField(default=False),
        ),
    ]
