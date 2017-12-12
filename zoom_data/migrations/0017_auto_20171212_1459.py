# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0016_auto_20171212_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('complete_date', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='activity',
            name='complete_date',
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(null=True, choices=[('Text', 'TEXT'), ('Facebook', 'FACEBOOK'), ('Call', 'CALL'), ('Mail', 'MAIL'), ('Email', 'EMAIL')], blank=True, max_length=8),
        ),
        migrations.AddField(
            model_name='attendance',
            name='activity',
            field=models.ForeignKey(to='zoom_data.Activity'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='resident',
            field=models.ForeignKey(to='zoom_data.Resident'),
        ),
        migrations.AddField(
            model_name='activity',
            name='members',
            field=models.ManyToManyField(to='zoom_data.Resident', through='zoom_data.Attendance'),
        ),
    ]
