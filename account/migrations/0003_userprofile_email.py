# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-06-12 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20180611_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
