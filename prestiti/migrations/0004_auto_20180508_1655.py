# Generated by Django 2.0.4 on 2018-05-08 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prestiti', '0003_auto_20180508_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestiti_dispositivo',
            name='modello',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prestiti.Prestiti_Modello', verbose_name='modello'),
        ),
        migrations.AlterField(
            model_name='prestiti_dispositivo',
            name='produttore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prestiti.Prestiti_Produttore', verbose_name='produttore'),
        ),
        migrations.AlterField(
            model_name='prestiti_dispositivo',
            name='tipo_dispositivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prestiti.Prestiti_Tipo_Dispositivo', verbose_name='tipo dispositivo'),
        ),
    ]