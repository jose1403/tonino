# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0002_auto_20161025_0049'),
        ('recepcion', '0008_auto_20161025_0840'),
    ]

    operations = [
        migrations.CreateModel(
            name='CuentasXpagarRecepcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deuda', models.FloatField()),
                ('abono', models.FloatField(default=0)),
                ('saldo_deudor', models.FloatField()),
                ('pagado', models.BooleanField(default=False)),
                ('fecha_agregado', models.DateField(auto_now_add=True)),
                ('fecha_vencimiento', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PagoRecepcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('p', models.BooleanField()),
                ('precio', models.ForeignKey(to='contabilidad.PrecioDeRubroPorCiclo')),
                ('recepcion', models.OneToOneField(to='recepcion.Recepcion')),
            ],
        ),
        migrations.CreateModel(
            name='TotalRecepcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descuentoH', models.FloatField(default=0)),
                ('descuentoI', models.FloatField(default=1)),
                ('descuentoM', models.FloatField(default=0.25)),
                ('descuentoTotal', models.FloatField(default=0)),
                ('cantidad_descuento', models.FloatField(default=0)),
                ('cantidad_real', models.FloatField(default=0)),
                ('total_neto', models.FloatField(default=0.0)),
                ('total_Bs', models.FloatField()),
                ('ingreso', models.OneToOneField(to='recepcion.PagoRecepcion')),
            ],
        ),
        migrations.AddField(
            model_name='cuentasxpagarrecepcion',
            name='recepcion',
            field=models.OneToOneField(to='recepcion.TotalRecepcion'),
        ),
    ]
