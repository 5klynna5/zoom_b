# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0005_auto_20171120_1631'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FoodShelf',
        ),
        migrations.DeleteModel(
            name='YMCA',
        ),
        migrations.AddField(
            model_name='resident',
            name='health_ins',
            field=models.CharField(choices=[('NONE', 'None'), ('PRIVATE', 'Private'), ('MEDICAID', 'Medicaid'), ('OTHER', 'Other Insurance')], max_length=8, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resident',
            name='unit_num',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resident',
            name='unit_type',
            field=models.CharField(choices=[('SUPPORTIVE', 'Supportive Housing'), ('MARIF', 'MARIF'), ('STUDIO', 'Studio')], max_length=10, blank=True, null=True),
        ),
    ]
