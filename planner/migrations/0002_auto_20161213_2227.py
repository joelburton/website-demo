# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
    ]
