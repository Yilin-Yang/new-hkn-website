# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-21 02:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eecSpeaks', '0003_auto_20170120_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publicationDate',
            field=models.DateField(null=True, verbose_name='Publication Date'),
        ),
    ]