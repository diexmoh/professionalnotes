# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-09-08 19:37
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('idAlumno', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apePat', models.CharField(max_length=50)),
                ('apeMat', models.CharField(max_length=50)),
                ('asesorias', multiselectfield.db.fields.MultiSelectField(choices=[('0', '0'), ('1', '1')], max_length=3)),
                ('asesoriaDesc', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]