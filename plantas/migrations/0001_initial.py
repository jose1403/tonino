# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plantas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('cantidad_silos', models.IntegerField()),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Silos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('capacidad', models.FloatField()),
                ('descripcion', models.TextField()),
                ('plantas', models.ForeignKey(to='plantas.Plantas')),
            ],
        ),
    ]
