# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('goal_name', models.CharField(max_length=100)),
                ('goal_date', models.DateField(null=True, blank=True)),
                ('goal_explain', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('date_progress', models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.')),
                ('percent_progress', models.CharField(choices=[('less than 25%', 'less than 25%'), ('25%', '25%'), ('50%', '50%'), ('75%', '75%'), ('100%', '100%')], blank=True, max_length=13)),
                ('notes_progress', models.TextField(blank=True)),
                ('goal', models.ForeignKey(to='zoom_data.Goal')),
            ],
        ),
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('resident_id', models.AutoField(serialize=False, primary_key=True)),
                ('resident_first_name', models.CharField(max_length=20)),
                ('resident_last_name', models.CharField(max_length=20)),
                ('resident_move_in', models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.')),
                ('resident_exit', models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.', null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='goal',
            name='goal_resident',
            field=models.ForeignKey(to='zoom_data.Resident'),
        ),
    ]
