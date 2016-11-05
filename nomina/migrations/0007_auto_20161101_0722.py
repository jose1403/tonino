# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nomina', '0006_auto_20161101_0720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bonodealimentacionsemanalempleados',
            name='null',
        ),
        migrations.RemoveField(
            model_name='bonodealimentacionsemanalobreros',
            name='null',
        ),
        migrations.RemoveField(
            model_name='cobrosemanalempleado',
            name='null',
        ),
        migrations.RemoveField(
            model_name='cobrosemanalobrero',
            name='null',
        ),
        migrations.RemoveField(
            model_name='fechapagosasignados',
            name='null',
        ),
        migrations.RemoveField(
            model_name='nominatotalempleados',
            name='null',
        ),
        migrations.RemoveField(
            model_name='nominatotalobreros',
            name='null',
        ),
        migrations.RemoveField(
            model_name='obrero',
            name='null',
        ),
        migrations.AlterField(
            model_name='obrero',
            name='documentoID',
            field=models.CharField(max_length=50),
        ),
    ]
