# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0008_auto_20171211_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(max_length=8, null=True, blank=True, choices=[('Text', 'TEXT'), ('Call', 'CALL'), ('Mail', 'MAIL'), ('Facebook', 'FACEBOOK'), ('Email', 'EMAIL')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_call',
            field=models.CharField(max_length=3, null=True, blank=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_email',
            field=models.CharField(max_length=3, null=True, blank=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_facebook',
            field=models.CharField(max_length=3, null=True, blank=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_mail',
            field=models.CharField(max_length=3, null=True, blank=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_photo',
            field=models.CharField(max_length=3, null=True, blank=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_text',
            field=models.CharField(max_length=3, null=True, blank=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='resident_email',
            field=models.EmailField(null=True, blank=True, max_length=254),
        ),
    ]
