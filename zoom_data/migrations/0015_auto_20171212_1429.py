# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0014_auto_20171212_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(null=True, choices=[('Text', 'TEXT'), ('Mail', 'MAIL'), ('Call', 'CALL'), ('Email', 'EMAIL'), ('Facebook', 'FACEBOOK')], max_length=8, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_call',
            field=models.CharField(null=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_email',
            field=models.CharField(null=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_facebook',
            field=models.CharField(null=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_mail',
            field=models.CharField(null=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_photo',
            field=models.CharField(null=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_text',
            field=models.CharField(null=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3, blank=True),
        ),
    ]
