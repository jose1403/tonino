# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0002_auto_20161024_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagorecepcion',
            name='pago',
        ),
        migrations.AddField(
            model_name='pagorecepcion',
            name='pagado',
            field=models.BooleanField(default=False),
        ),
    ]
