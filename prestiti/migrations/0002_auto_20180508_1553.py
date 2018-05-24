# Generated by Django 2.0.4 on 2018-05-08 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestiti', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prestiti_dispositivo',
            options={'verbose_name': 'dispositivo', 'verbose_name_plural': 'dispositivi'},
        ),
        migrations.AlterModelOptions(
            name='prestiti_tipo_dispositivo',
            options={'ordering': ['tipo_dispositivo'], 'verbose_name': 'tipo dispositivo', 'verbose_name_plural': 'tipi dispositivo'},
        ),
        migrations.AddField(
            model_name='prestiti_dispositivo',
            name='disponibile',
            field=models.BooleanField(default=True),
        ),
    ]
