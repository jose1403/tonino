# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rubro', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rubro',
            old_name='tolrancia_impuerezas',
            new_name='tolerancia_impuerezas',
        ),
    ]
