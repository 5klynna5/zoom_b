# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0011_auto_20171211_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='participants',
            field=models.ManyToManyField(to='zoom_data.Resident'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(max_length=8, null=True, blank=True, choices=[('Text', 'TEXT'), ('Mail', 'MAIL'), ('Email', 'EMAIL'), ('Call', 'CALL'), ('Facebook', 'FACEBOOK')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_call',
            field=models.CharField(max_length=3, null=True, blank=True, choices=[('No', 'NO'), ('Yes', 'YES')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_email',
            field=models.CharField(max_length=3, null=True, blank=True, choices=[('No', 'NO'), ('Yes', 'YES')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_facebook',
            field=models.CharField(max_length=3, null=True, blank=True, choices=[('No', 'NO'), ('Yes', 'YES')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_mail',
            field=models.CharField(max_length=3, null=True, blank=True, choices=[('No', 'NO'), ('Yes', 'YES')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_photo',
            field=models.CharField(max_length=3, null=True, blank=True, choices=[('No', 'NO'), ('Yes', 'YES')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_text',
            field=models.CharField(max_length=3, null=True, blank=True, choices=[('No', 'NO'), ('Yes', 'YES')]),
        ),
    ]
