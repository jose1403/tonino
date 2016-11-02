# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
        ('contabilidad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='banco',
            field=models.ForeignKey(to='contabilidad.Bancos'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipo_cuenta',
            field=models.ForeignKey(to='contabilidad.TipoCuenta'),
        ),
    ]
