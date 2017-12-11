# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0003_foodshelf_ywca'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='YWCA',
            new_name='YMCA',
        ),
    ]
