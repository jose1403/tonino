# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0003_auto_20161027_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bancos',
            name='nombre',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='tipocuenta',
            name='nombre',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
