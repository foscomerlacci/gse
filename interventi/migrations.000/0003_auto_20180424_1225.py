# Generated by Django 2.0.4 on 2018-04-24 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interventi', '0002_auto_20180424_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intervento',
            name='numero_ticket',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]