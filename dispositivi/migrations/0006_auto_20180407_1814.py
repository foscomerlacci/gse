# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivi', '0005_auto_20180407_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allegato',
            name='inserito_il',
            field=models.DateField(auto_now_add=True),
        ),
    ]
