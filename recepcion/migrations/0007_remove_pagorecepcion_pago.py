# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0006_auto_20161025_0815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagorecepcion',
            name='pago',
        ),
    ]
