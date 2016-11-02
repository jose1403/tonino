# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rubro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=50)),
                ('nombre_cientifico', models.CharField(unique=True, max_length=100)),
                ('tolerancia_humedad', models.FloatField(default=0)),
                ('diferencia_humedad', models.FloatField(default=0)),
                ('tolrancia_impuerezas', models.FloatField(default=0)),
                ('foto', models.ImageField(default=b'imagenes/icon_miau.gif', upload_to=b'imagenes/rubro', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoRubro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=50)),
                ('descripcion', models.TextField()),
                ('rubro', models.ForeignKey(to='rubro.Rubro')),
            ],
        ),
        migrations.CreateModel(
            name='VariedadRubro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=50)),
                ('descripcion', models.TextField()),
                ('rubro', models.ForeignKey(to='rubro.Rubro')),
            ],
        ),
    ]
