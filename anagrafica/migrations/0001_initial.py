# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utente',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cognome', models.CharField(max_length=50)),
                ('matricola', models.CharField(unique=True, max_length=10)),
                ('utenza', models.CharField(unique=True, max_length=8)),
                ('divisione', models.CharField(null=True, blank=True, max_length=50)),
                ('ruolo', models.CharField(choices=[('dir', 'dirigente'), ('seg', 'segretaria')], default=('dir', 'dirigente'), max_length=3)),
                ('segretaria_associata', models.ManyToManyField(blank=True, related_name='segretaria_associata_rel_+', to='anagrafica.Utente')),
            ],
            options={
                'verbose_name_plural': 'utenti',
            },
        ),
    ]
