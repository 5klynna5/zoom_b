# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0006_auto_20171211_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('resident_phone', models.CharField(null=True, max_length=9, blank=True)),
                ('resident_email', models.EmailField(max_length=254)),
                ('permission_text', models.CharField(null=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3, blank=True)),
                ('permission_photo', models.CharField(null=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3, blank=True)),
                ('permission_email', models.CharField(null=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3, blank=True)),
                ('permission_call', models.CharField(null=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3, blank=True)),
                ('permission_mail', models.CharField(null=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3, blank=True)),
                ('permission_facebook', models.CharField(null=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3, blank=True)),
                ('contact_pref', models.CharField(null=True, choices=[('Text', 'TEXT'), ('Mail', 'MAIL'), ('Facebook', 'FACEBOOK'), ('Email', 'EMAIL'), ('Call', 'CALL')], max_length=8, blank=True)),
                ('date_updated', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='resident',
            name='unit_type',
            field=models.CharField(null=True, choices=[('Supportive Housing', 'SUPPORTIVE'), ('MARIF', 'MARIF'), ('Studio', 'STUDIO')], max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_resident',
            field=models.ForeignKey(to='zoom_data.Resident'),
        ),
    ]
