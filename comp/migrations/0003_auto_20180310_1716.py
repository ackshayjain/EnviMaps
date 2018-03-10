# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0002_auto_20180309_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='lat',
            field=models.FloatField(default=b'28.475127'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='lon',
            field=models.FloatField(default=b'76.995267'),
        ),
    ]
