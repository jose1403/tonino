# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proovedores', '0002_auto_20161027_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='productor',
            name='e_mail',
            field=models.EmailField(default=b'moliven@moliven.com', max_length=254, blank=True),
        ),
    ]
