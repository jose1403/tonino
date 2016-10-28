# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plantas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='silos',
            name='en_inventario',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='silos',
            name='resto',
            field=models.FloatField(default=0),
        ),
    ]
