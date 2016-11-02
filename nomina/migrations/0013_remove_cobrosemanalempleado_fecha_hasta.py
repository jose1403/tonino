# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nomina', '0012_auto_20161101_1317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cobrosemanalempleado',
            name='fecha_hasta',
        ),
    ]
