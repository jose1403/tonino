# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plantas', '0002_auto_20161030_0621'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantas',
            name='null',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='silos',
            name='null',
            field=models.BooleanField(default=False),
        ),
    ]
