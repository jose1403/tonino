# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nomina', '0009_auto_20161101_0725'),
    ]

    operations = [
        migrations.AddField(
            model_name='bonodealimentacionsemanalempleados',
            name='null',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bonodealimentacionsemanalobreros',
            name='null',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cobrosemanalempleado',
            name='null',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cobrosemanalobrero',
            name='null',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='empleado',
            name='null',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fechapagosasignados',
            name='null',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='nominatotalempleados',
            name='null',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='nominatotalobreros',
            name='null',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='obrero',
            name='null',
            field=models.BooleanField(default=False),
        ),
    ]
