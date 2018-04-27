# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anagrafica', '0002_utente_attivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utente',
            name='ruolo',
            field=models.CharField(max_length=3, default=('dir', 'dirigenza'), choices=[('dir', 'dirigenza'), ('seg', 'segreteria')]),
        ),
    ]
