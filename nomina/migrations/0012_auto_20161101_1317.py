# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nomina', '0011_auto_20161101_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='cobrosemanalempleado',
            name='descuento_faov',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cobrosemanalobrero',
            name='descuento_faov',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cobrosemanalempleado',
            name='descuento_ivss',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cobrosemanalobrero',
            name='descuento_ivss',
            field=models.FloatField(default=0),
        ),
    ]
