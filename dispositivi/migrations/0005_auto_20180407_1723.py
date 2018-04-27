# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivi', '0004_allegato_descrizione'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allegato',
            options={'verbose_name_plural': 'allegati', 'verbose_name': 'allegato'},
        ),
        migrations.RenameField(
            model_name='allegato',
            old_name='datestamp',
            new_name='inserito_il',
        ),
    ]
