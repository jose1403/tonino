# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos_de_la_empresa',
            name='LOGO',
            field=models.ImageField(default=b'imagenes/empresa/logo.jpeg', upload_to=b''),
        ),
    ]
