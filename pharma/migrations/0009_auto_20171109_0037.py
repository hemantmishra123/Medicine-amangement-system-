# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 19:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('pharma', '0008_auto_20171107_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='c_id',
        ),
        migrations.RemoveField(
            model_name='dealer',
            name='d_id',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='e_id',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='p_id',
        ),
    ]