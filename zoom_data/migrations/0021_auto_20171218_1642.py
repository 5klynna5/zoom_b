# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0020_auto_20171212_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(null=True, max_length=8, blank=True, choices=[('Email', 'EMAIL'), ('Mail', 'MAIL'), ('Text', 'TEXT'), ('Call', 'CALL'), ('Facebook', 'FACEBOOK')]),
        ),
    ]
