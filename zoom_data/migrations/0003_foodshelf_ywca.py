# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0002_auto_20171120_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodShelf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('month', models.CharField(choices=[('01', 'January'), ('02', 'February'), ('03', 'March'), ('04', 'April'), ('05', 'May'), ('06', 'June'), ('07', 'July'), ('08', 'August'), ('09', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], max_length=2)),
                ('year', models.PositiveSmallIntegerField()),
                ('number_visits', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='YWCA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('month', models.CharField(choices=[('01', 'January'), ('02', 'February'), ('03', 'March'), ('04', 'April'), ('05', 'May'), ('06', 'June'), ('07', 'July'), ('08', 'August'), ('09', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], max_length=2)),
                ('year', models.PositiveSmallIntegerField()),
                ('number_visits', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
