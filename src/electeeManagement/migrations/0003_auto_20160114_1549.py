# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-14 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electeeManagement', '0002_electee_service_hours_social'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_hours',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='social',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
