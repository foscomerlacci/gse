# Generated by Django 2.0.4 on 2018-04-27 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivi', '0018_auto_20180423_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='location',
            field=models.CharField(choices=[('Roma - Laurentina', 'Roma - Laurentina'), ('Roma - Mattei', 'Roma - Mattei'), ('Milano - SDM', 'Milano - SDM')], default=('Roma - Laurentina', 'Roma - Laurentina'), max_length=30),
        ),
    ]