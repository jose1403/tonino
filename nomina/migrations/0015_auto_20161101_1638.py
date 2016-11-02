# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nomina', '0014_auto_20161101_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='obrero',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
    ]
