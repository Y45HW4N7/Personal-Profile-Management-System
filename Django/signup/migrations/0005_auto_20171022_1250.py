# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 07:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_auto_20171022_1248'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserProfile',
        ),
    ]