# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0003_auto_20160928_1925'),
        ('clientes', '0002_delete_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_o_razon_social', models.CharField(max_length=100)),
                ('documentoId', models.CharField(unique=True, max_length=20)),
                ('domicilio_fiscal', models.TextField()),
                ('telefono', models.CharField(max_length=12, blank=True)),
                ('celular', models.CharField(max_length=12, blank=True)),
                ('cuenta_bancaria', models.CharField(max_length=100, blank=True)),
                ('fecha_agregado', models.DateTimeField(auto_now=True)),
                ('observacion', models.TextField(blank=True)),
                ('banco', models.ForeignKey(to='contabilidad.Bancos', blank=True)),
                ('tipo_cuenta', models.ForeignKey(to='contabilidad.TipoCuenta', blank=True)),
            ],
        ),
    ]
