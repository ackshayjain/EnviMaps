# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='lat',
            field=models.FloatField(default=b'28.480837'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='lon',
            field=models.FloatField(default=b'77.080211'),
        ),
    ]
