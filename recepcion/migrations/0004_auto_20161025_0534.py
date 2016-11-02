# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0003_cuentasxpagarrecepcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuentasxpagarrecepcion',
            name='recepcion',
        ),
        migrations.DeleteModel(
            name='CuentasXpagarRecepcion',
        ),
    ]
