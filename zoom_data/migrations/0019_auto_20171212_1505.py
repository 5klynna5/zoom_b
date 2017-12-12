# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0018_auto_20171212_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(blank=True, max_length=8, choices=[('Call', 'CALL'), ('Mail', 'MAIL'), ('Text', 'TEXT'), ('Facebook', 'FACEBOOK'), ('Email', 'EMAIL')], null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_call',
            field=models.CharField(blank=True, max_length=3, choices=[('Yes', 'YES'), ('No', 'NO')], null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_email',
            field=models.CharField(blank=True, max_length=3, choices=[('Yes', 'YES'), ('No', 'NO')], null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_facebook',
            field=models.CharField(blank=True, max_length=3, choices=[('Yes', 'YES'), ('No', 'NO')], null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_mail',
            field=models.CharField(blank=True, max_length=3, choices=[('Yes', 'YES'), ('No', 'NO')], null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_photo',
            field=models.CharField(blank=True, max_length=3, choices=[('Yes', 'YES'), ('No', 'NO')], null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_text',
            field=models.CharField(blank=True, max_length=3, choices=[('Yes', 'YES'), ('No', 'NO')], null=True),
        ),
    ]
