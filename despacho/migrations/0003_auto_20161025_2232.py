# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('despacho', '0002_cuentasxcobrardespacho'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuentasxcobrardespacho',
            name='despacho',
        ),
        migrations.DeleteModel(
            name='CuentasXcobrarDespacho',
        ),
    ]
