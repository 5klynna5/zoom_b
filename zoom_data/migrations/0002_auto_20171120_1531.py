# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='percent_progress',
            field=models.CharField(default='less than 25%', max_length=13, choices=[('less than 25%', 'less than 25%'), ('25%', '25%'), ('50%', '50%'), ('75%', '75%'), ('100%', '100%')], blank=True),
        ),
    ]
