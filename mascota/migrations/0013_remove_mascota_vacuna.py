# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 06:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0012_auto_20170902_0150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascota',
            name='vacuna',
        ),
    ]
