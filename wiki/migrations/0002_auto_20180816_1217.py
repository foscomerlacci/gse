# Generated by Django 2.0.4 on 2018-08-16 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contatto',
            name='note',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
