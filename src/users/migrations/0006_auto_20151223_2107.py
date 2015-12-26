# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-23 21:07
from __future__ import unicode_literals

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_member_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='edu_level',
            field=models.CharField(blank=True, choices=[('UG', 'Undergraduate'), ('GR', 'Graduate'), ('AL', 'Alumni')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='expected_grad_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='major',
            field=models.CharField(blank=True, choices=[('CS', 'Computer Science'), ('CE', 'Computer Engineering'), ('EE', 'Electrical Engineering')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=users.models.user_directory_path),
        ),
    ]
