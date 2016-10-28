# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0011_auto_20161030_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recepcion',
            name='silo',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'plantas', to='plantas.Silos', chained_field=b'planta', null=True, auto_choose=True),
        ),
    ]
