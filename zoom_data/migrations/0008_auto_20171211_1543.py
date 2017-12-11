# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0007_auto_20171211_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(null=True, max_length=8, choices=[('Call', 'CALL'), ('Email', 'EMAIL'), ('Text', 'TEXT'), ('Facebook', 'FACEBOOK'), ('Mail', 'MAIL')], blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='resident_phone',
            field=models.CharField(null=True, max_length=10, blank=True),
        ),
    ]
