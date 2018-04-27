# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivi', '0012_auto_20180412_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='modello',
            field=models.ForeignKey(verbose_name='modello', to='dispositivi.Modello', on_delete=models.CASCADE),
        ),
        migrations.AlterField(
            model_name='dispositivo',
            name='produttore',
            field=models.ForeignKey(verbose_name='produttore', to='dispositivi.Produttore', on_delete=models.CASCADE),
        ),
        migrations.AlterField(
            model_name='dispositivo',
            name='tipo_dispositivo',
            field=models.ForeignKey(verbose_name='tipo dispositivo', to='dispositivi.Tipo_Dispositivo', on_delete=models.CASCADE),
        ),
    ]
