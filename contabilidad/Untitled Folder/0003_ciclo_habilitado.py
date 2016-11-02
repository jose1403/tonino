# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0002_delete_impuesto'),
    ]

    operations = [
        migrations.AddField(
            model_name='ciclo',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
    ]
