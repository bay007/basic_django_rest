# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0004_auto_20170901_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='vacuna',
            field=models.ManyToManyField(db_table='inocuacion', related_name='inocuacion', to='mascota.Vacuna'),
        ),
    ]
