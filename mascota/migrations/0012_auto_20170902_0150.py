# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0011_auto_20170902_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='vacuna',
            field=models.ManyToManyField(db_table='inocuacion2', related_name='inocuacion2', to='mascota.Vacuna'),
        ),
    ]
