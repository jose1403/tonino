# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='totalrecepcion',
            name='cantidad_descuento',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='totalrecepcion',
            name='cantidad_real',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='totalrecepcion',
            name='descuentoH',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='totalrecepcion',
            name='descuentoI',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='totalrecepcion',
            name='descuentoM',
            field=models.FloatField(default=0.25),
        ),
        migrations.AddField(
            model_name='totalrecepcion',
            name='descuentoTotal',
            field=models.FloatField(default=0),
        ),
    ]
