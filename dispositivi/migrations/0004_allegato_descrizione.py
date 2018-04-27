# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivi', '0003_auto_20180405_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='allegato',
            name='descrizione',
            field=models.CharField(null=True, max_length=30, blank=True),
        ),
    ]
