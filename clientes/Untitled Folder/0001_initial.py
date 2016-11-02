# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_o_razon_social', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('documentoId', models.CharField(unique=True, max_length=20)),
                ('domicilio', models.TextField()),
                ('fecha_de_nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=12)),
                ('celular', models.CharField(max_length=12)),
                ('cuenta_bancaria', models.CharField(max_length=100, blank=True)),
                ('Tipo_Cuenta', models.CharField(blank=True, max_length=3, choices=[(b'Aho', b'Ahorro'), (b'Cor', b'Corriente')])),
                ('Banco', models.CharField(max_length=100, blank=True)),
                ('observacion', models.TextField(blank=True)),
            ],
        ),
    ]
