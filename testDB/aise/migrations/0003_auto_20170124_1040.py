# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aise', '0002_auto_20170124_1027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='details',
            options={'managed': False},
        ),
    ]
