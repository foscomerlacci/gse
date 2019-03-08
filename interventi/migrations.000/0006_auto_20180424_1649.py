# Generated by Django 2.0.4 on 2018-04-24 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interventi', '0005_auto_20180424_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intervento',
            name='descrizione_richiesta',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='intervento',
            name='note',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='intervento',
            name='numero_ticket',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='intervento',
            name='soluzione_adottata',
            field=models.TextField(max_length=300),
        ),
    ]