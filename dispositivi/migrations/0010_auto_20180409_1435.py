# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivi', '0009_auto_20180408_0153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modello',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('modello', models.CharField(max_length=30)),
                ('attivo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'modello',
                'verbose_name_plural': 'modelli',
                'ordering': ['modello'],
            },
        ),
        migrations.CreateModel(
            name='Produttore',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('produttore', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'produttore',
                'verbose_name_plural': 'produttori',
                'ordering': ['produttore'],
            },
        ),
        migrations.CreateModel(
            name='Tipo_Dispositivo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('tipo_dispositivo', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'dispositivo',
                'verbose_name_plural': 'tipi dispositivo',
                'ordering': ['tipo_dispositivo'],
            },
        ),
        migrations.AddField(
            model_name='modello',
            name='fk_produttore',
            field=models.ForeignKey(verbose_name='produttore', to='dispositivi.Produttore', on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='modello',
            name='fk_tipo_dispositivo',
            field=models.ForeignKey(verbose_name='tipo dispositivo', to='dispositivi.Tipo_Dispositivo', on_delete=models.CASCADE),
        ),
    ]
