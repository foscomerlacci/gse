# Generated by Django 2.0.4 on 2018-05-24 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestiti', '0009_auto_20180523_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestito',
            name='note',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]