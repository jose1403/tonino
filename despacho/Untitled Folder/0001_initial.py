# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('rubro', '__first__'),
        ('clientes', '__first__'),
        ('contabilidad', '0003_ciclo_habilitado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Despacho',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio', models.FloatField()),
                ('fecha_salida', models.DateTimeField()),
                ('tipo_vehiculo', models.CharField(max_length=100)),
                ('placa', models.CharField(max_length=50)),
                ('dirigido_a', models.CharField(max_length=300)),
                ('referencia_folder', models.CharField(default=0, max_length=20)),
                ('cantidad_en_Kg', models.FloatField()),
                ('humedad', models.FloatField()),
                ('impureza', models.FloatField()),
                ('granos_danados_totales', models.FloatField()),
                ('granos_partidos', models.FloatField()),
                ('temperatura_promedio', models.FloatField()),
                ('otros', models.FloatField()),
                ('despachado_por', models.CharField(max_length=100)),
                ('fecha_agregado', models.DateTimeField(auto_now=True)),
                ('observacion', models.TextField()),
                ('Tipo', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'rubro', to='rubro.TipoRubro', chained_field=b'producto', auto_choose=True)),
                ('ciclo_asociado', models.ForeignKey(to='contabilidad.Ciclo')),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
                ('producto', models.ForeignKey(to='rubro.Rubro')),
                ('variedad', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'rubro', to='rubro.VariedadRubro', chained_field=b'producto', auto_choose=True)),
            ],
        ),
        migrations.CreateModel(
            name='IngresoDespacho',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio', models.FloatField()),
                ('pagado', models.BooleanField(default=False)),
                ('despacho', models.OneToOneField(to='despacho.Despacho')),
            ],
        ),
        migrations.CreateModel(
            name='TotalDespacho',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_neto', models.FloatField()),
                ('total_Bs', models.FloatField()),
                ('ingreso', models.OneToOneField(to='despacho.IngresoDespacho')),
            ],
        ),
    ]
