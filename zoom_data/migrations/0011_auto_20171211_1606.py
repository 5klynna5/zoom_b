# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0010_auto_20171211_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=30)),
                ('activity_date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(max_length=8, blank=True, null=True, choices=[('Call', 'CALL'), ('Mail', 'MAIL'), ('Email', 'EMAIL'), ('Text', 'TEXT'), ('Facebook', 'FACEBOOK')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_call',
            field=models.CharField(max_length=3, blank=True, null=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_email',
            field=models.CharField(max_length=3, blank=True, null=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_facebook',
            field=models.CharField(max_length=3, blank=True, null=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_mail',
            field=models.CharField(max_length=3, blank=True, null=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_photo',
            field=models.CharField(max_length=3, blank=True, null=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_text',
            field=models.CharField(max_length=3, blank=True, null=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
    ]
