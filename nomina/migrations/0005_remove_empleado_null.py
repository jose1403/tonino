# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nomina', '0004_auto_20161101_0715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='null',
        ),
    ]
