# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0005_remove_chain_peer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peer',
            name='address',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
