# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0025_auto_20180104_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='ethnicity',
            field=models.CharField(choices=[('HISPANIC', 'Hispanic'), ('NON-HISPANIC', 'Non-Hispanic')], null=True, max_length=12, blank=True),
        ),
        migrations.AddField(
            model_name='resident',
            name='race',
            field=models.CharField(choices=[('AFRICAN_AMERICAN', 'African American'), ('WHITE', 'White'), ('MULTIRACIAL', 'Multiracial'), ('AMER_INDIAN', 'American Indian'), ('PAC_ISLANDER', 'Native Hawaiian or Pacific Islander'), ('ASIAN_AMERICAN', 'Asian American')], null=True, max_length=16, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(choices=[('Mail', 'MAIL'), ('Text', 'TEXT'), ('Facebook', 'FACEBOOK'), ('Email', 'EMAIL'), ('Call', 'CALL')], null=True, max_length=8, blank=True),
        ),
    ]
