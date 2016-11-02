# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proovedores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productor',
            name='null',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='zonaproductor',
            name='null',
            field=models.BooleanField(default=False),
        ),
    ]
