# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_o_razon_social', models.CharField(max_length=100)),
                ('documentoId', models.CharField(unique=True, max_length=20)),
                ('domicilio_fiscal', models.TextField()),
                ('telefono', models.CharField(max_length=12, blank=True)),
                ('celular', models.CharField(max_length=12, blank=True)),
                ('referencia_folder', models.CharField(default=b'0', max_length=50)),
                ('cuenta_bancaria', models.CharField(max_length=100, blank=True)),
                ('fecha_agregado', models.DateTimeField(auto_now=True)),
                ('habilitado', models.BooleanField(default=True)),
                ('observacion', models.TextField(blank=True)),
                ('banco', models.ForeignKey(to='contabilidad.Bancos')),
                ('tipo_cuenta', models.ForeignKey(to='contabilidad.TipoCuenta')),
            ],
        ),
        migrations.CreateModel(
            name='ZonaProductor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(default=b'Por', max_length=3, choices=[(b'Por', b'Portuguesa'), (b'Bar', b'Barinas'), (b'Coj', b'Cojedes'), (b'Gua', b'Guarico')])),
                ('municipio', models.CharField(max_length=50)),
                ('zona', models.CharField(unique=True, max_length=50)),
                ('hectareas', models.FloatField()),
                ('productor', models.ForeignKey(to='proovedores.Productor')),
            ],
        ),
    ]
