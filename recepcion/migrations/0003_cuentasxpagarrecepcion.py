# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0002_auto_20161024_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='CuentasXpagarRecepcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deuda', models.FloatField()),
                ('abono', models.FloatField(default=0)),
                ('saldo_deudor', models.FloatField()),
                ('pagaddo', models.BooleanField(default=False)),
                ('recepcion', models.OneToOneField(to='recepcion.TotalRecepcion')),
            ],
        ),
    ]
