# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20170828_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contracts',
            name='current_bid',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='email',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
    ]
