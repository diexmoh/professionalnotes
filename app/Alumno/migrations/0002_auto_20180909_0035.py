# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-09 00:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumno', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='asesorias',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
