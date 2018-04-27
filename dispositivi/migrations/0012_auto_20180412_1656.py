# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivi', '0011_auto_20180412_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='modello',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dispositivo',
            name='produttore',
            field=models.IntegerField(),
        ),
    ]
