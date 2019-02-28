# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anagrafica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allegato',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('allegato', models.FileField(upload_to='')),
                ('datestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'allegati',
            },
        ),
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('asset', models.CharField(unique=True, max_length=10)),
                ('location', models.CharField(choices=[('lau', 'Roma - Laurentina'), ('mat', 'Roma - Mattei')], default=('lau', 'Roma - Laurentina'), max_length=3)),
                ('piano', models.CharField(null=True, blank=True, max_length=10)),
                ('stanza', models.CharField(null=True, blank=True, max_length=3)),
                ('tipo_dispositivo', models.CharField(choices=[('des', 'desktop'), ('lap', 'laptop'), ('tab', 'tablet'), ('sma', 'smartphone'), ('sta', 'stampante'), ('doc', 'docking'), ('mon', 'monitor')], default=('des', 'desktop'), max_length=3)),
                ('seriale', models.CharField(unique=True, max_length=30)),
                ('data_installazione', models.DateField()),
                ('data_dismissione', models.DateTimeField()),
                ('fine_garanzia', models.DateField(null=True, blank=True)),
                ('produttore', models.CharField(max_length=20)),
                ('modello', models.CharField(max_length=20)),
                ('os', models.CharField(null=True, blank=True, max_length=15)),
                ('allegati', models.FileField(null=True, upload_to='static')),
                ('note', models.TextField(null=True, blank=True, max_length=200)),
                ('attivo', models.ForeignKey(to='anagrafica.Utente',on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name_plural': 'dispositivi',
            },
        ),
        migrations.AddField(
            model_name='allegato',
            name='dispositivo',
            field=models.ForeignKey(to='dispositivi.Dispositivo',on_delete=models.CASCADE),
        ),
    ]
