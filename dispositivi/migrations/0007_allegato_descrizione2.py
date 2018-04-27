# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivi', '0006_auto_20180407_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='allegato',
            name='descrizione2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
