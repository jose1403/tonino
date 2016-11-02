# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0002_auto_20161025_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='bancos',
            name='null',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ciclo',
            name='null',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='precioderubroporciclo',
            name='null',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tipocuenta',
            name='null',
            field=models.BooleanField(default=False),
        ),
    ]
