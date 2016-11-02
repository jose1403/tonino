# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DATOS_DE_LA_EMPRESA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NOMBRE', models.CharField(max_length=100)),
                ('NOMBRE_DEL_ENCARGADO', models.CharField(max_length=100)),
                ('RIF', models.CharField(max_length=30)),
                ('DIRECCION', models.TextField()),
                ('TELEFONO', models.CharField(max_length=30)),
                ('CELULAR', models.CharField(max_length=30)),
                ('CODIGO_POSTAL', models.CharField(max_length=10)),
                ('FAX', models.CharField(max_length=30, blank=True)),
            ],
        ),
    ]
