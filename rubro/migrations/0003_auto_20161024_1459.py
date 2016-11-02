# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rubro', '0002_auto_20161024_1458'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rubro',
            old_name='tolerancia_impuerezas',
            new_name='tolerancia_impureza',
        ),
    ]
