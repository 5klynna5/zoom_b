# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0015_auto_20171212_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(choices=[('Mail', 'MAIL'), ('Email', 'EMAIL'), ('Facebook', 'FACEBOOK'), ('Call', 'CALL'), ('Text', 'TEXT')], max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_call',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_email',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_facebook',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_mail',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_photo',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_text',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3, null=True, blank=True),
        ),
    ]
