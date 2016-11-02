# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('despacho', '0003_auto_20161025_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='CuentasXcobrarDespacho',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deuda', models.FloatField()),
                ('abono', models.FloatField(default=0)),
                ('saldo_deudor', models.FloatField()),
                ('pagado', models.BooleanField(default=False)),
                ('fecha_agregado', models.DateField(auto_now_add=True)),
                ('fecha_vencimiento', models.DateField()),
                ('despacho', models.OneToOneField(to='despacho.TotalDespacho')),
            ],
        ),
    ]
