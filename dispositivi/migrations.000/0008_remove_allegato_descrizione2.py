# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivi', '0007_allegato_descrizione2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allegato',
            name='descrizione2',
        ),
    ]
