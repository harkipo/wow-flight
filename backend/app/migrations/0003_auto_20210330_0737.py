# Generated by Django 3.1.6 on 2021-03-30 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210330_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='arrival_time',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_time',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
