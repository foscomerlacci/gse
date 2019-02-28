# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='data_dismissione',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
