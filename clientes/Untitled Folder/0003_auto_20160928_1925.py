# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('rubro', '0005_rubro_tiporubro_variedadrubro'),
        ('contabilidad', '0002_auto_20160928_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bancos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CantidadEgresadoDeRubroPorCiclo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad_en_Kg', models.FloatField(default=0)),
                ('cantidad_en_Bs', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CantidadEgresadoTotalRubro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad_en_Kg', models.FloatField(default=0)),
                ('cantidad_en_Bs', models.FloatField(default=0)),
                ('rubro', models.ForeignKey(to='rubro.Rubro')),
            ],
        ),
        migrations.CreateModel(
            name='CantidadIngresadoDeRubroPorCiclo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad_en_Kg', models.FloatField(default=0)),
                ('cantidad_en_Bs', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CantidadIngresadoTotalRubro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad_en_Kg', models.FloatField(default=0)),
                ('cantidad_en_Bs', models.FloatField(default=0)),
                ('rubro', models.ForeignKey(to='rubro.Rubro')),
            ],
        ),
        migrations.CreateModel(
            name='Ciclo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=50)),
                ('fecha_de_inicio', models.DateField()),
                ('fecha_de_cierre', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Impuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('calculo', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PrecioDeRubroPorCiclo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio_por_Kg', models.FloatField()),
                ('ciclo', models.ForeignKey(to='contabilidad.Ciclo')),
                ('producto', models.ForeignKey(to='rubro.Rubro')),
                ('tipo', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'rubro', to='rubro.TipoRubro', chained_field=b'producto', auto_choose=True)),
                ('variedad', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'rubro', to='rubro.VariedadRubro', chained_field=b'producto', auto_choose=True)),
            ],
        ),
        migrations.CreateModel(
            name='RubroDisponible',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad_total', models.FloatField()),
                ('disponible', models.BooleanField()),
                ('rubro', models.ForeignKey(to='rubro.Rubro')),
            ],
        ),
        migrations.CreateModel(
            name='TipoCuenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='cantidadingresadoderubroporciclo',
            name='ciclo',
            field=models.ForeignKey(to='contabilidad.Ciclo'),
        ),
        migrations.AddField(
            model_name='cantidadingresadoderubroporciclo',
            name='rubro',
            field=models.ForeignKey(to='rubro.Rubro'),
        ),
        migrations.AddField(
            model_name='cantidadegresadoderubroporciclo',
            name='ciclo',
            field=models.ForeignKey(to='contabilidad.Ciclo'),
        ),
        migrations.AddField(
            model_name='cantidadegresadoderubroporciclo',
            name='rubro',
            field=models.ForeignKey(to='rubro.Rubro'),
        ),
    ]
