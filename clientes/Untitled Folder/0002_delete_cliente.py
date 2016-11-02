# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('despacho', '0002_auto_20160928_1909'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]
