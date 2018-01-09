# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0023_auto_20180104_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='first_name',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='child',
            name='last_name',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(choices=[('Facebook', 'FACEBOOK'), ('Mail', 'MAIL'), ('Email', 'EMAIL'), ('Call', 'CALL'), ('Text', 'TEXT')], max_length=8, null=True, blank=True),
        ),
    ]
