# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('plantas', '0003_auto_20161027_1623'),
        ('despacho', '0005_auto_20161027_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='despacho',
            name='planta',
            field=models.ForeignKey(to='plantas.Plantas', null=True),
        ),
        migrations.AddField(
            model_name='despacho',
            name='silo',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'plantas', to='plantas.Silos', chained_field=b'planta', null=True, auto_choose=True),
        ),
    ]
