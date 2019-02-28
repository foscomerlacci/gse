# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivi', '0010_auto_20180409_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='tipo_dispositivo',
            field=models.IntegerField(),
        ),
    ]
