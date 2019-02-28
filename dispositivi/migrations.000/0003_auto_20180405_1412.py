# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivi', '0002_auto_20180401_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='data_dismissione',
            field=models.DateField(blank=True, null=True),
        ),
    ]
