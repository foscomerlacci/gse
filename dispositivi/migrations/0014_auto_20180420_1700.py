# Generated by Django 2.0.4 on 2018-04-20 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivi', '0013_auto_20180412_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='allegati',
            field=models.FileField(blank=True, null=True, upload_to='static'),
        ),
    ]
