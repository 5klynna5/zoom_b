# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0022_auto_20180104_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(max_length=6, choices=[('FEMALE', 'Female'), ('MALE', 'Male'), ('ALT', 'Another gender')], blank=True, null=True)),
                ('head_of_household', models.ForeignKey(to='zoom_data.Resident')),
            ],
        ),
        migrations.CreateModel(
            name='ChildAttendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('complete_date', models.DateField(blank=True, null=True)),
                ('activity', models.ForeignKey(to='zoom_data.Activity')),
                ('child', models.ForeignKey(to='zoom_data.Child')),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(max_length=8, choices=[('Call', 'CALL'), ('Mail', 'MAIL'), ('Email', 'EMAIL'), ('Text', 'TEXT'), ('Facebook', 'FACEBOOK')], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='children',
            field=models.ManyToManyField(to='zoom_data.Child', through='zoom_data.ChildAttendance'),
        ),
    ]
