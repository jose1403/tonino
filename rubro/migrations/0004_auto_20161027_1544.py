# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rubro', '0003_auto_20161024_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='rubro',
            name='null',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tiporubro',
            name='null',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='variedadrubro',
            name='null',
            field=models.BooleanField(default=False),
        ),
    ]
