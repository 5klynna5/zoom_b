# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0013_auto_20171211_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='participants',
        ),
        migrations.AddField(
            model_name='activity',
            name='skill_area',
            field=models.CharField(blank=True, choices=[('FINANCE', 'Finance'), ('PARENTING', 'Parenting'), ('EMPLOYMENT', 'Employment')], null=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='activity',
            name='complete_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(blank=True, choices=[('Mail', 'MAIL'), ('Call', 'CALL'), ('Email', 'EMAIL'), ('Facebook', 'FACEBOOK'), ('Text', 'TEXT')], null=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_call',
            field=models.CharField(blank=True, choices=[('Yes', 'YES'), ('No', 'NO')], null=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_email',
            field=models.CharField(blank=True, choices=[('Yes', 'YES'), ('No', 'NO')], null=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_facebook',
            field=models.CharField(blank=True, choices=[('Yes', 'YES'), ('No', 'NO')], null=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_mail',
            field=models.CharField(blank=True, choices=[('Yes', 'YES'), ('No', 'NO')], null=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_photo',
            field=models.CharField(blank=True, choices=[('Yes', 'YES'), ('No', 'NO')], null=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_text',
            field=models.CharField(blank=True, choices=[('Yes', 'YES'), ('No', 'NO')], null=True, max_length=3),
        ),
    ]
