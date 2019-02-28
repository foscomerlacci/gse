# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anagrafica', '0003_auto_20180405_1412'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attivo',
            options={'ordering': ['attivo'], 'verbose_name_plural': 'utenti'},
        ),
    ]
