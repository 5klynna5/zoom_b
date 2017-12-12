# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0012_auto_20171211_1614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='activity_date',
            new_name='complete_date',
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(choices=[('Email', 'EMAIL'), ('Call', 'CALL'), ('Mail', 'MAIL'), ('Text', 'TEXT'), ('Facebook', 'FACEBOOK')], null=True, blank=True, max_length=8),
        ),
    ]
