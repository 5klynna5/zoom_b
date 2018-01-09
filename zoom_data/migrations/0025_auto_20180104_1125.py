# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0024_auto_20180104_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='month',
            field=models.CharField(choices=[('Jan', 'January'), ('Feb', 'February'), ('Mar', 'March'), ('Apr', 'April'), ('May', 'May'), ('Jun', 'June'), ('Jul', 'July'), ('Aug', 'August'), ('Sep', 'September'), ('Oct', 'October'), ('Nov', 'November'), ('Dec', 'December')], null=True, blank=True, max_length=3),
        ),
        migrations.AddField(
            model_name='activity',
            name='year',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='skill_area',
            field=models.CharField(choices=[('FINANCE', 'Finance'), ('PARENTING', 'Parenting'), ('EMPLOYMENT', 'Employment'), ('FITNESS', 'Fitness')], null=True, blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(choices=[('Facebook', 'FACEBOOK'), ('Call', 'CALL'), ('Mail', 'MAIL'), ('Text', 'TEXT'), ('Email', 'EMAIL')], null=True, blank=True, max_length=8),
        ),
    ]
