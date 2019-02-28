# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivi', '0008_remove_allegato_descrizione2'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispositivo',
            name='palazzo',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dispositivo',
            name='attivo',
            field=models.ForeignKey(to='anagrafica.Utente', verbose_name='assegnatario', on_delete=models.CASCADE),
        ),
    ]
