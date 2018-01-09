# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0021_auto_20171218_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='gender',
            field=models.CharField(choices=[('FEMALE', 'Female'), ('MALE', 'Male'), ('ALT', 'Another gender')], max_length=6, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(choices=[('Mail', 'MAIL'), ('Email', 'EMAIL'), ('Call', 'CALL'), ('Text', 'TEXT'), ('Facebook', 'FACEBOOK')], max_length=8, null=True, blank=True),
        ),
    ]
