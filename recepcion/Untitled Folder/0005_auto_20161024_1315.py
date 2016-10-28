# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0001_initial'),
        ('rubro', '0001_initial'),
        ('proovedores', '0001_initial'),
        ('recepcion', '0004_auto_20161024_1313'),
    ]

    operations = [
        migrations.CreateModel(
            name='PagoRecepcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pago', models.BooleanField(default=True)),
                ('pagado', models.BooleanField(default=False)),
                ('precio', models.ForeignKey(to='contabilidad.PrecioDeRubroPorCiclo')),
            ],
        ),
        migrations.CreateModel(
            name='Recepcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_llegada', models.DateTimeField()),
                ('tipo_vehiculo', models.CharField(max_length=100)),
                ('placa', models.CharField(max_length=50)),
                ('numero_romana', models.CharField(default=0, max_length=20)),
                ('referencia_folder', models.CharField(default=0, max_length=20)),
                ('cantidad_en_Kg', models.FloatField()),
                ('humedad', models.FloatField()),
                ('impureza', models.FloatField()),
                ('granos_danados_totales', models.FloatField()),
                ('granos_partidos', models.FloatField()),
                ('temperatura_promedio', models.FloatField()),
                ('otros', models.FloatField()),
                ('recibido_por', models.CharField(max_length=100)),
                ('fecha_agregado', models.DateTimeField(auto_now=True)),
                ('observacion', models.TextField(default=b'Recepcion Satisfactoria')),
                ('ciclo_asociado', models.ForeignKey(to='contabilidad.Ciclo')),
                ('producto', models.ForeignKey(to='rubro.Rubro')),
                ('proovedor', models.ForeignKey(to='proovedores.Productor')),
                ('tipo', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'rubro', to='rubro.TipoRubro', chained_field=b'producto', auto_choose=True)),
                ('variedad', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'rubro', to='rubro.VariedadRubro', chained_field=b'producto', auto_choose=True)),
                ('zona_de_cosecha', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'productor', to='proovedores.ZonaProductor', chained_field=b'proovedor', auto_choose=True)),
            ],
        ),
        migrations.CreateModel(
            name='TotalRecepcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_neto', models.FloatField(default=0.0)),
                ('total_Bs', models.FloatField()),
                ('ingreso', models.OneToOneField(to='recepcion.PagoRecepcion')),
            ],
        ),
        migrations.AddField(
            model_name='pagorecepcion',
            name='recepcion',
            field=models.OneToOneField(to='recepcion.Recepcion'),
        ),
    ]
