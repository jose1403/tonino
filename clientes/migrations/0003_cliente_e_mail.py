# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_cliente_null'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='e_mail',
            field=models.EmailField(default=b'moliven@moliven.com', max_length=254, blank=True),
        ),
    ]
