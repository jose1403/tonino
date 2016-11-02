# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0003_auto_20161004_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos_de_la_empresa',
            name='LOGO',
            field=models.ImageField(default=b'/imagenes/empresa/logo.jpg', upload_to=b'imagenes/empresa'),
        ),
    ]
