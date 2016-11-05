# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nomina', '0002_auto_20161101_0535'),
    ]

    operations = [
        migrations.CreateModel(
            name='BonoDeAlimentacionSemanalEmpleados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bono_mensual', models.FloatField()),
                ('bono_diario', models.FloatField()),
                ('dias_trabajados', models.IntegerField()),
                ('total_a_cobrar', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='BonoDeAlimentacionSemanalObreros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bono_mensual', models.FloatField()),
                ('bono_diario', models.FloatField()),
                ('dias_trabajados', models.IntegerField()),
                ('total_a_cobrar', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CobroSemanalEmpleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_hasta', models.DateField()),
                ('sueldo_diario', models.FloatField()),
                ('dias_trabajados', models.IntegerField()),
                ('bono_nocturno', models.FloatField()),
                ('total_asignacion', models.FloatField()),
                ('descuento_ivss', models.FloatField()),
                ('total_deducciones', models.FloatField()),
                ('total_a_cobrar', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CobroSemanalObrero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sueldo_diario', models.FloatField()),
                ('dias_trabajados', models.IntegerField()),
                ('bono_nocturno', models.FloatField()),
                ('total_asignacion', models.FloatField()),
                ('descuento_ivss', models.FloatField()),
                ('total_deducciones', models.FloatField()),
                ('total_a_cobrar', models.FloatField()),
                ('generado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('documentoID', models.CharField(max_length=50)),
                ('fecha_de_nacimiento', models.DateField()),
                ('domicilio', models.TextField()),
                ('genero', models.CharField(max_length=1, choices=[(b'M', b'Hombre'), (b'F', b'Mujer')])),
                ('fecha_ingreso', models.DateField()),
                ('contrato', models.CharField(max_length=50)),
                ('referecia_contrato', models.CharField(max_length=50)),
                ('sueldo_mensual', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='FechaPagosAsignados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_cierre', models.DateField()),
                ('semana', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NominaTotalEmpleados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_obreros', models.IntegerField()),
                ('total_nomina', models.FloatField()),
                ('fecha_generado', models.DateField(auto_now=True)),
                ('Empleados', models.ManyToManyField(to='nomina.CobroSemanalEmpleado')),
                ('fecha', models.OneToOneField(to='nomina.FechaPagosAsignados')),
            ],
        ),
        migrations.CreateModel(
            name='NominaTotalObreros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_obreros', models.IntegerField()),
                ('total_nomina', models.FloatField()),
                ('fecha_generado', models.DateField(auto_now=True)),
                ('fecha', models.OneToOneField(to='nomina.FechaPagosAsignados')),
                ('obreros', models.ManyToManyField(to='nomina.CobroSemanalObrero')),
            ],
        ),
        migrations.CreateModel(
            name='Obrero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('documentoID', models.CharField(max_length=50)),
                ('fecha_de_nacimiento', models.DateField()),
                ('domicilio', models.TextField()),
                ('genero', models.CharField(max_length=1, choices=[(b'M', b'Hombre'), (b'F', b'Mujer')])),
                ('fecha_ingreso', models.DateField()),
                ('referencia_folder', models.CharField(max_length=30)),
                ('contrato', models.CharField(max_length=50)),
                ('referecia_contrato', models.CharField(max_length=50)),
                ('sueldo_mensual', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('null', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='obrero',
            name='puesto',
            field=models.ForeignKey(to='nomina.Puesto'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='puesto',
            field=models.ForeignKey(to='nomina.Puesto'),
        ),
        migrations.AddField(
            model_name='cobrosemanalobrero',
            name='fecha',
            field=models.OneToOneField(to='nomina.FechaPagosAsignados'),
        ),
        migrations.AddField(
            model_name='cobrosemanalobrero',
            name='obrero',
            field=models.ForeignKey(to='nomina.Obrero'),
        ),
        migrations.AddField(
            model_name='cobrosemanalempleado',
            name='empleado',
            field=models.ForeignKey(to='nomina.Empleado'),
        ),
        migrations.AddField(
            model_name='cobrosemanalempleado',
            name='fecha',
            field=models.OneToOneField(to='nomina.FechaPagosAsignados'),
        ),
        migrations.AddField(
            model_name='bonodealimentacionsemanalobreros',
            name='fecha',
            field=models.OneToOneField(to='nomina.FechaPagosAsignados'),
        ),
        migrations.AddField(
            model_name='bonodealimentacionsemanalobreros',
            name='obreros',
            field=models.ManyToManyField(to='nomina.Obrero'),
        ),
        migrations.AddField(
            model_name='bonodealimentacionsemanalempleados',
            name='fecha',
            field=models.OneToOneField(to='nomina.FechaPagosAsignados'),
        ),
        migrations.AddField(
            model_name='bonodealimentacionsemanalempleados',
            name='obreros',
            field=models.ManyToManyField(to='nomina.Empleado'),
        ),
    ]
