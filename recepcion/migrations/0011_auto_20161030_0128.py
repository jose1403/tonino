# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('plantas', '0001_initial'),
        ('recepcion', '0010_auto_20161025_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='recepcion',
            name='planta',
            field=models.ForeignKey(to='plantas.Plantas', null=True),
        ),
        migrations.AddField(
            model_name='recepcion',
            name='silo',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'planta', to='plantas.Silos', chained_field=b'planta', null=True, auto_choose=True),
        ),
    ]
