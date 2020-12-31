# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharma', '0017_auto_20171111_2134'),
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
            model_name='purchase',
            name='p_id',
        ),
    ]
