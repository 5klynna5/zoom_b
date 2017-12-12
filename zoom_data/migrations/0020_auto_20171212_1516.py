# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0019_auto_20171212_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(choices=[('Facebook', 'FACEBOOK'), ('Call', 'CALL'), ('Text', 'TEXT'), ('Email', 'EMAIL'), ('Mail', 'MAIL')], null=True, blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_call',
            field=models.CharField(choices=[('No', 'NO'), ('Yes', 'YES')], null=True, blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_email',
            field=models.CharField(choices=[('No', 'NO'), ('Yes', 'YES')], null=True, blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_facebook',
            field=models.CharField(choices=[('No', 'NO'), ('Yes', 'YES')], null=True, blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_mail',
            field=models.CharField(choices=[('No', 'NO'), ('Yes', 'YES')], null=True, blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_photo',
            field=models.CharField(choices=[('No', 'NO'), ('Yes', 'YES')], null=True, blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_text',
            field=models.CharField(choices=[('No', 'NO'), ('Yes', 'YES')], null=True, blank=True, max_length=3),
        ),
    ]
