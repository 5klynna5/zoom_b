# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0026_auto_20180109_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='ethnicity',
            field=models.CharField(choices=[('HISPANIC', 'Hispanic'), ('NON-HISPANIC', 'Non-Hispanic')], null=True, blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='child',
            name='race',
            field=models.CharField(choices=[('AFRICAN_AMERICAN', 'African American'), ('WHITE', 'White'), ('MULTIRACIAL', 'Multiracial'), ('AMER_INDIAN', 'American Indian'), ('PAC_ISLANDER', 'Native Hawaiian or Pacific Islander'), ('ASIAN_AMERICAN', 'Asian American')], null=True, blank=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(choices=[('Call', 'CALL'), ('Text', 'TEXT'), ('Facebook', 'FACEBOOK'), ('Mail', 'MAIL'), ('Email', 'EMAIL')], null=True, blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_call',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], null=True, blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_email',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], null=True, blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_facebook',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], null=True, blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_mail',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], null=True, blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_photo',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], null=True, blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_text',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], null=True, blank=True, max_length=3),
        ),
    ]
